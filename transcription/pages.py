from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, levenshtein, distance_and_ok
from django.conf import settings
##
from .models import Constants, Player
from otree.common import safe_json
import time


class CustomWaitPage(WaitPage):
    template_name = 'transcription/CustomWaitPage.html'


class StartWP(CustomWaitPage):
    _allow_custom_attributes = True
    group_by_arrival_time = True
    template_name = 'transcription/FirstWaitPage.html'

    def get_mturk_group_name(self):
        return 'mturkchannel_{}_{}'.format(self.session.pk, self._index_in_pages)

    def is_displayed(self):
        try:
            post_dict = self.request.POST.dict()
            endofgame = post_dict.get('endofgame')
            if endofgame:
                self.player.outofthegame = True
        except AttributeError:
            ...
        return self.subsession.round_number == 1

    def vars_for_template(self):
        now = time.time()
        self.player.payoff = 0
        self.participant.vars['payoff'] = 0
        
        if not self.player.startwp_timer_set:
            self.player.startwp_timer_set = True
            self.player.startwp_time = time.time()
        time_left = self.player.startwp_time + Constants.startwp_timer - now
        return {'time_left': round(time_left),
                'index_in_pages': self._index_in_pages}

    def get_players_for_group(self, waiting_players):
        out_of_the_gamers = [p for p in waiting_players if p.outofthegame]
        if len(out_of_the_gamers) > 0:
            return out_of_the_gamers
        if len(waiting_players) == Constants.players_per_group:
            return waiting_players


class ManagerChat(Page):
    def is_displayed(self):
        if self.player.id_in_group == 1 and not self.player.outofthegame:
            return True

    def vars_for_template(self):

        if self.group.get_player_by_id(2).participant.vars.get('bid') is None:
            bid2 = 0
        else:
            bid2 = self.group.get_player_by_id(2).participant.vars.get('bid')

        if self.group.get_player_by_id(3).participant.vars.get('bid') is None:
            bid3 = 0
        else:
            bid3 = self.group.get_player_by_id(3).participant.vars.get('bid')

        if self.group.get_player_by_id(4).participant.vars.get('bid') is None:
            bid4 = 0
        else:
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
                'fbid2': float(bid2),
                'bid2': bid2,
                'fbid3': float(bid3),
                'bid3': bid3,
                'fbid4': float(bid4),
                'bid4': bid4,

                'channel1': channel1,
                'channel2': channel2,
                'channel3': channel3,
                'split_chats': Constants.split_chats,
                'budget' : Constants.budget,
                'budgetminus2times15' : (Constants.budget - c(2)) * 15
                }


    form_model = models.Player
    form_fields = ['man_emp1_price','man_emp1_nodeal','man_emp2_price','man_emp2_nodeal','man_emp3_price','man_emp3_nodeal']  

    def error_message(self, values):
        if values["man_emp1_nodeal"]==False:
            if values["man_emp1_price"] is None:
                return 'Please enter a price for Employee 1, or check box for no deal'
            elif (values["man_emp1_price"] < 0):
                return 'Your price for Employee 1 cannot be less than 0'
            elif  (values["man_emp1_price"] > Constants.budget ):
                return 'Your price for Employee 1 must be less than or equal to the budget!'

        if values["man_emp2_nodeal"]==False:
            if values["man_emp2_price"] is None:
                return 'Please enter a price for Employee 2, or check box for no deal'
            elif (values["man_emp2_price"] < 0):
                return 'Your price for Employee 2 cannot be less than 0'
            elif  (values["man_emp2_price"] > Constants.budget ):
                return 'Your price for Employee 2 must be less than or equal to the budget!'

        if values["man_emp3_nodeal"]==False:
            if values["man_emp3_price"] is None:
                return 'Please enter a price for Employee 3, or check box for no deal'
            elif (values["man_emp3_price"] < 0):
                return 'Your price for Employee 3 cannot be less than 0'
            elif  (values["man_emp3_price"] > Constants.budget ):
                return 'Your price for Employee 3 must be less than or equal to the budget!'

    def before_next_page(self):
        if self.player.id_in_group == 1:

            if self.player.man_emp1_nodeal == True :
                self.participant.vars['man_emp1_price'] = 0
            else:
                self.participant.vars['man_emp1_price'] = self.player.man_emp1_price

            if self.player.man_emp2_nodeal == True :
                self.participant.vars['man_emp2_price'] = 0
            else:
                self.participant.vars['man_emp2_price'] = self.player.man_emp2_price

            if self.player.man_emp3_nodeal == True :
                self.participant.vars['man_emp3_price'] = 0
            else:
                self.participant.vars['man_emp3_price'] = self.player.man_emp3_price


class EmployeeChat(Page):
    def is_displayed(self):
        if self.player.id_in_group != 1 and not self.player.outofthegame:
            return True

    def vars_for_template(self):
        if self.player.participant.vars.get('bid') is None:
            bid = 0
        else:
            bid = self.player.participant.vars.get('bid')
#        match = bid <= 9.0
        if Constants.split_chats:
            if self.player.id_in_group == 2:
                channel = self.group.id_in_subsession + 1000
            elif self.player.id_in_group == 3:
                channel = self.group.id_in_subsession + 7777
            else:
                channel = self.group.id_in_subsession + 8989
        else:
            channel = self.group.id_in_subsession

        return {'fbid': float(bid),
                'bid': bid,
 #               'match': match,
                'enum': self.player.id_in_group - 1,
                'channel': channel,
                'split_chats': Constants.split_chats,
                'budget': Constants.budget}
#                    'kickin': Constants.kickin}

    form_model = 'player'
    form_fields = ['emp_price','emp_nodeal']

    def error_message(self, values):

        if values["emp_nodeal"]==False:
            if values["emp_price"] is None:
                return 'Please enter a value for the confirmed price, or check box for no deal'
            elif (values["emp_price"] < 0):
                return 'Your price must be greater than 0!'



    def before_next_page(self):
        if self.player.id_in_group != 1:
            if self.player.emp_nodeal == False:
                self.participant.vars['emp_price'] = max(self.player.emp_price,0)
            else:
                self.participant.vars['emp_price'] = 0
    
class OptIn(Page):
    def is_displayed(self):
        if self.round_number == 1: # and not self.player.outofthegame:
            return True

    def vars_for_template(self):
        if self.player.id_in_group != 1:
            return {'esurvey_text': "After the exit survey you will proceed to transcription if you came to an agreement."}
        else :
            return {'esurvey_text': ""}

class Demographics(Page):
    def is_displayed(self):
        if self.round_number == 1: # and not self.player.outofthegame:
            return True

    form_model = 'player'
    form_fields = ['yearBorn', 'gender']

class Household(Page):
    def is_displayed(self):
        if self.round_number == 1: # and not self.player.outofthegame:
            return True

    form_model = 'player'
    form_fields = ['experience', 'transExp', 'eduLevel', 'dailyHHEarn']

#<<<<<
#<<<<<    Transcribe 1
#<<<<<

class Transcribe_1(Page):
    def is_displayed(self):
        if self.player.id_in_group != 1 and not self.player.outofthegame and self.player.emp_nodeal == False and self.player.emp_price > 0 and self.player.emp_price <= Constants.budget :
            return True

    form_model = 'player'
    form_fields = ['transcribed_text_1']      #  INDEXED

    def vars_for_template(self):
        return {
            'image_path': 'transcription/1_{}.png'.format(1),   # INDEXED
 #           'reference_text': safe_json(Constants.reference_text_1),   # INDEX -1
            'reference_text': safe_json(Constants.reference_text[0]),   # INDEX -1
            'header_text': 'You will be shown 5 pages of transcription, one on each screen.  When you click next, your transcription of the first page will be submitted and you will be presented with a fresh link to a second page of transcription and a blank text box, and so on until the fifth page. After you submit the fifth page your HIT will be finished.',
            'debug': settings.DEBUG,
            'required_accuracy': 100 * (1 - Constants.allowed_error_rate),  # INDEX -1
            'agreed': self.player.emp_price
        }

    def transcribed_text_1_error_message(self, transcribed_text):
        reference_text = Constants.reference_text[0]
        allowed_error_rate = Constants.allowed_error_rate
        clean_trx_text = ''.join(e for e in transcribed_text if e.isalnum())
        clean_trx_text = clean_trx_text.replace('\n', ' ').replace('\r', '')
        distance, ok = distance_and_ok(clean_trx_text, reference_text,
                                       allowed_error_rate)
        if ok:
            self.player.levenshtein_distance_1 = distance
        else:
            if allowed_error_rate == 0:
                return "The transcription should be exactly the same as on the image."
            else:
                return "This transcription appears to contain too many errors."

#<<<<<
#<<<<<    Transcribe 2
#<<<<<

class Transcribe_2(Page):
    def is_displayed(self):
        if self.player.id_in_group != 1 and not self.player.outofthegame and self.player.emp_nodeal == False and self.player.emp_price > 0 and self.player.emp_price <= Constants.budget :
            return True

    form_model = 'player'
    form_fields = ['transcribed_text_2']      #  INDEXED

    def vars_for_template(self):
        return {
            'image_path': 'transcription/1_{}.png'.format(2),   # INDEXED
            'reference_text': safe_json(Constants.reference_text[1]),   # INDEX -1
            'header_text': '',
            'debug': settings.DEBUG,
            'required_accuracy': 100 * (1 - Constants.allowed_error_rate),  # INDEX -1
            'agreed': self.player.emp_price
        }

    def transcribed_text_2_error_message(self, transcribed_text):
        reference_text = Constants.reference_text[1]
        allowed_error_rate = Constants.allowed_error_rate
        clean_trx_text = ''.join(e for e in transcribed_text if e.isalnum())
        clean_trx_text = clean_trx_text.replace('\n', ' ').replace('\r', '')
        distance, ok = distance_and_ok(clean_trx_text, reference_text,
                                       allowed_error_rate)
        if ok:
            self.player.levenshtein_distance_2 = distance
        else:
            if allowed_error_rate == 0:
                return "The transcription should be exactly the same as on the image."
            else:
                return "This transcription appears to contain too many errors."


#<<<<<
#<<<<<    Transcribe 3
#<<<<<

class Transcribe_3(Page):
    def is_displayed(self):
        if self.player.id_in_group != 1 and not self.player.outofthegame and self.player.emp_nodeal == False and self.player.emp_price > 0 and self.player.emp_price <= Constants.budget :
            return True

    form_model = 'player'
    form_fields = ['transcribed_text_3']      #  INDEXED

    def vars_for_template(self):
        return {
            'image_path': 'transcription/1_{}.png'.format(3),   # INDEXED
            'reference_text': safe_json(Constants.reference_text[2]),   # INDEX -1
            'header_text': '',
            'debug': settings.DEBUG,
            'required_accuracy': 100 * (1 - Constants.allowed_error_rate),  # INDEX -1
            'agreed': self.player.emp_price
        }

    def transcribed_text_3_error_message(self, transcribed_text):
        reference_text = Constants.reference_text[2]
        allowed_error_rate = Constants.allowed_error_rate
        clean_trx_text = ''.join(e for e in transcribed_text if e.isalnum())
        clean_trx_text = clean_trx_text.replace('\n', ' ').replace('\r', '')
        distance, ok = distance_and_ok(clean_trx_text, reference_text,
                                       allowed_error_rate)
        if ok:
            self.player.levenshtein_distance_3 = distance
        else:
            if allowed_error_rate == 0:
                return "The transcription should be exactly the same as on the image."
            else:
                return "This transcription appears to contain too many errors."


#<<<<<
#<<<<<    Transcribe 4
#<<<<<

class Transcribe_4(Page):
    def is_displayed(self):
        if self.player.id_in_group != 1 and not self.player.outofthegame and self.player.emp_nodeal == False and self.player.emp_price > 0 and self.player.emp_price <= Constants.budget :
            return True

    form_model = 'player'
    form_fields = ['transcribed_text_4']      #  INDEXED

    def vars_for_template(self):
        return {
            'image_path': 'transcription/1_{}.png'.format(4),   # INDEXED
            'reference_text': safe_json(Constants.reference_text[3]),   # INDEX -1
            'header_text': '',
            'debug': settings.DEBUG,
            'required_accuracy': 100 * (1 - Constants.allowed_error_rate),  # INDEX -1
            'agreed': self.player.emp_price
        }

    def transcribed_text_4_error_message(self, transcribed_text):
        reference_text = Constants.reference_text[3]
        allowed_error_rate = Constants.allowed_error_rate
        clean_trx_text = ''.join(e for e in transcribed_text if e.isalnum())
        clean_trx_text = clean_trx_text.replace('\n', ' ').replace('\r', '')
        distance, ok = distance_and_ok(clean_trx_text, reference_text,
                                       allowed_error_rate)
        if ok:
            self.player.levenshtein_distance_4 = distance
        else:
            if allowed_error_rate == 0:
                return "The transcription should be exactly the same as on the image."
            else:
                return "This transcription appears to contain too many errors."


#<<<<<
#<<<<<    Transcribe 5
#<<<<<

class Transcribe_5(Page):
    def is_displayed(self):
        if self.player.id_in_group != 1 and not self.player.outofthegame and self.player.emp_nodeal == False and self.player.emp_price > 0 and self.player.emp_price <= Constants.budget :
            return True

    form_model = 'player'
    form_fields = ['transcribed_text_5']      #  INDEXED

    def vars_for_template(self):
        return {
            'image_path': 'transcription/1_{}.png'.format(5),   # INDEXED
            'reference_text': safe_json(Constants.reference_text[4]),   # INDEX -1
            'header_text': '',
            'debug': settings.DEBUG,
            'required_accuracy': 100 * (1 - Constants.allowed_error_rate),  # INDEX -1
            'agreed': self.player.emp_price

        }

    def transcribed_text_5_error_message(self, transcribed_text):
        reference_text = Constants.reference_text[4]
        allowed_error_rate = Constants.allowed_error_rate
        clean_trx_text = ''.join(e for e in transcribed_text if e.isalnum())
        clean_trx_text = clean_trx_text.replace('\n', ' ').replace('\r', '')
        distance, ok = distance_and_ok(clean_trx_text, reference_text,
                                       allowed_error_rate)
        if ok:
            self.player.levenshtein_distance_5 = distance
        else:
            if allowed_error_rate == 0:
                return "The transcription should be exactly the same as on the image."
            else:
                return "This transcription appears to contain too many errors."



class Results(Page):

    def is_displayed(self):
        if self.player.id_in_group != 1 and not self.player.outofthegame and self.player.emp_nodeal == False and self.player.emp_price > 0 and self.player.emp_price <= Constants.budget :
            return True

    def vars_for_template(self):
        table_rows = []
        transcribed_list = []
        levenshteins = []
        num_good = 0
        transcribed_list.append(self.player.transcribed_text_1)
        transcribed_list.append(self.player.transcribed_text_2)
        transcribed_list.append(self.player.transcribed_text_3)
        transcribed_list.append(self.player.transcribed_text_4)
        transcribed_list.append(self.player.transcribed_text_5)
        levenshteins.append(self.player.levenshtein_distance_1)
        levenshteins.append(self.player.levenshtein_distance_2)
        levenshteins.append(self.player.levenshtein_distance_3)
        levenshteins.append(self.player.levenshtein_distance_4)
        levenshteins.append(self.player.levenshtein_distance_5)


        # =======  loop 1
        for i in range(5):
            accuracy = (1 - levenshteins[i] / len(Constants.reference_text[i])) * 100
            if (accuracy < 0):
                accuracy = 0
            clean_trx_text = ''.join(e for e in transcribed_list[i] if e.isalnum())
            clean_trx_text = clean_trx_text.replace('\n', ' ').replace('\r', '')
            row = {
                'round_number': 1,
                'reference_text_length': len(Constants.reference_text[i]),
                'transcribed_text_length': len(clean_trx_text),
                'distance': levenshteins[i],
                'accuracy': round(accuracy, 2)
            }
            table_rows.append(row)  
            if (accuracy >= 95.0):
                num_good += 1

        if self.player.id_in_group == 2:
            man_price = self.group.get_player_by_id(1).participant.vars.get('man_emp1_price',0)
        elif self.player.id_in_group == 3:
            man_price = self.group.get_player_by_id(1).participant.vars.get('man_emp2_price',0)
        elif self.player.id_in_group == 4:
            man_price = self.group.get_player_by_id(1).participant.vars.get('man_emp3_price',0)
        else: 
            man_price = 0

        man_payoff = self.group.get_player_by_id(1).participant.vars.get('payoff',0)
                 
        if self.player.emp_price > 0 and self.player.emp_price <= Constants.budget and man_price == self.player.emp_price :
            self.group.get_player_by_id(1).payoff += round(num_good * (Constants.budget - self.player.emp_price), 2)
            self.group.get_player_by_id(1).participant.vars['payoff'] = man_payoff + round(num_good * (Constants.budget - self.player.emp_price), 2)
        else:
            self.group.get_player_by_id(1).payoff += 0
            self.group.get_player_by_id(1).participant.vars['payoff'] = man_payoff
            
        self.player.payoff = round(num_good * self.player.emp_price, 2)

        self.player.participant_vars_dump = str(self.participant.vars)
        self.player.man_participant_vars_dump = str(self.group.get_player_by_id(1).participant.vars)
        
        return {'table_rows': table_rows,
                'num_good': num_good,
                'emp_price': self.player.emp_price,
                'emp_bonus': self.player.payoff,
                'mgr_bonus': self.group.get_player_by_id(1).payoff,
                'transcribed_list': transcribed_list}


class Finish(Page):
    def is_displayed(self):
        if ( self.player.id_in_group != 1 and not self.player.outofthegame ) and ( self.player.emp_price == 0 or self.player.emp_nodeal == True )  :
            return True

class Feedback(Page):
    form_model = 'player'
    form_fields = ['feedback_form']      #  INDEXED

page_sequence = [
    StartWP,
#    ManagerPreChat,
    ManagerChat,
    EmployeeChat,
    OptIn,
    Demographics,
    Household,
    Transcribe_1,
    Transcribe_2,
    Transcribe_3,
    Transcribe_4,
    Transcribe_5,
    Results,
    Finish,
    Feedback
]
