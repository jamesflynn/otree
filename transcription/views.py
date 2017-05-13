from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, levenshtein, distance_and_ok
from django.conf import settings

class MyWaitPage(WaitPage):
    template_name = 'transcription/MyWaitPage.html'
    group_by_arrival_time = True

    def is_displayed(self):
        if ( self.round_number == 1 ):
            return True    
    def after_all_players_arrive(self):
        pass

class ManagerChat(Page):
    def is_displayed(self):
        if ( self.player.id_in_subsession%4 == 1 ) & ( self.round_number == 1 ):
            self.player.participant.vars['payoff'] = 0
            return True

    def vars_for_template(self):

        bid2 = self.group.get_player_by_id(2).participant.vars.get('bid')
        bid3 = self.group.get_player_by_id(3).participant.vars.get('bid')
        bid4 = self.group.get_player_by_id(4).participant.vars.get('bid')
        if Constants.split_chats:
            channel1 = self.group.id_in_subsession + 1000
            channel2 = self.group.id_in_subsession + 7777
            channel3 = self.group.id_in_subsession + 8989
        else:
            channel1 = self.group.id_in_subsession
            channel2 = self.group.id_in_subsession
            channel3 = self.group.id_in_subsession            

        return {
                'bid2': bid2,
                'bid3': bid3,
                'bid4': bid4,
                'mgr_bonus': self.player.participant.vars['payoff'],
                'channel1': channel1,
                'channel2': channel2,
                'channel3': channel3,
                'split_chats': Constants.split_chats
                }

    form_model = models.Player
    form_fields = ['man_emp1_price','man_emp2_price','man_emp3_price']    
#    form_fields = ['man_emp1_price','man_emp1_accpt','man_emp2_price','man_emp2_accpt','man_emp3_price','man_emp3_accpt']

class EmployeeChat(Page):
    def is_displayed(self):
        if ( self.player.id_in_subsession%4 != 1 ) & ( self.round_number == 1 ):
            return True
    def vars_for_template(self):
        bid = self.player.participant.vars.get('bid')
        if Constants.split_chats:
            if self.player.id_in_subsession%4 == 2:
                channel = self.group.id_in_subsession + 1000
            elif self.player.id_in_subsession%4 == 3:
                channel = self.group.id_in_subsession + 7777
            else:
               channel = self.group.id_in_subsession + 8989
        else:
            channel = self.group.id_in_subsession

        return { 'bid': bid,
                 'enum': (self.player.id_in_subsession-1)%4,
                 'channel': channel,
                 'split_chats': Constants.split_chats }

    form_model = models.Player
    form_fields = ['emp_price']

class Transcribe(Page):

    def is_displayed(self):        
        if (self.player.id_in_subsession%4 != 1) & (self.player.in_round(1).emp_price != 0):
            return True

    form_model = models.Player
    form_fields = ['transcribed_text']

    def vars_for_template(self):

        return {
#            'image_path': 'https://dl.dropboxusercontent.com/u/1688949/trx/{}_{}.png'.format(self.player.id_in_group-1,
#                self.round_number),
            'image_path': 'https://dl.dropboxusercontent.com/u/1688949/trx/1_{}.png'.format(self.round_number),
#            'reference_text': safe_json(Constants.reference_texts[self.player.id_in_group-2,self.round_number - 1]),
            'reference_text': safe_json(Constants.reference_texts[0,self.round_number - 1]),
            'debug': settings.DEBUG,
            'required_accuracy': 100 * (1 - Constants.allowed_error_rates[self.round_number - 1]),
            'agreed': self.player.in_round(1).emp_price
        }

    def transcribed_text_error_message(self, transcribed_text):
#        reference_text = Constants.reference_texts[self.player.id_in_group-2,self.round_number - 1]
        reference_text = Constants.reference_texts[0,self.round_number - 1]
        allowed_error_rate = Constants.allowed_error_rates[self.round_number - 1]
        clean_trx_text = ''.join(e for e in transcribed_text if e.isalnum())
        clean_trx_text = clean_trx_text.replace('\n', ' ').replace('\r', '')
        distance, ok = distance_and_ok(clean_trx_text, reference_text,
                                       allowed_error_rate)
        if ok:
            self.player.levenshtein_distance = distance
        else:
            if allowed_error_rate == 0:
                return "The transcription should be exactly the same as on the image."
            else:
                return "This transcription appears to contain too many errors."

class Results(Page):

#    form_model = models.Group
#    form_fields = ['mgr_bonus']

    def is_displayed(self):
        if ( self.player.id_in_subsession%4 != 1) & ( self.round_number == Constants.num_rounds )  & (self.player.in_round(1).emp_price != 0):
            return True

    def vars_for_template(self):
        table_rows = []
        num_good = 0
        for prev_player in self.player.in_all_rounds():
#            accuracy = (1 - prev_player.levenshtein_distance / len(Constants.reference_texts[self.player.id_in_group-2,prev_player.round_number - 1]))*100
            accuracy = (1 - prev_player.levenshtein_distance / len(Constants.reference_texts[0,prev_player.round_number - 1]))*100
            if ( accuracy < 0 ):
                accuracy = 0
            clean_trx_text = ''.join(e for e in prev_player.transcribed_text if e.isalnum())
            clean_trx_text = clean_trx_text.replace('\n', ' ').replace('\r', '')
            row = {
                'round_number': prev_player.round_number,
                #'reference_text_length': len(Constants.reference_texts[self.player.id_in_group-2,prev_player.round_number - 1]),
                'reference_text_length': len(Constants.reference_texts[0,prev_player.round_number - 1]),
                'transcribed_text_length': len(clean_trx_text),
                'distance': prev_player.levenshtein_distance,
                'accuracy': round(accuracy,2)
            }
            table_rows.append(row)
            if (accuracy >= 95.0):
                num_good += 1

        self.group.get_player_by_id(1).payoff += round(num_good * ( 5 - self.player.in_round(1).emp_price ),2)
        self.player.payoff = round(num_good * self.player.in_round(1).emp_price,2)

        return {'table_rows': table_rows,
                'num_good': num_good,
                'emp_price': self.player.in_round(1).emp_price,
                'bonus': self.player.payoff,
                'mgr_bonus' : self.group.get_player_by_id(1).payoff}

class ManagerResults(Page):
    def is_displayed(self):
        if ( self.player.id_in_subsession%4 == 1) & ( self.round_number == Constants.num_rounds ):
            return True

page_sequence = [
    MyWaitPage,
    ManagerChat,
    EmployeeChat,
    Transcribe,
    Results,
    ManagerResults
]