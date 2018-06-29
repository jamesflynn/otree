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


class ManagerPreChat(Page):
    def is_displayed(self):
        if self.player.id_in_group == 1 and self.round_number == 1 and not self.player.outofthegame:
            return True

    def vars_for_template(self):

        if self.group.get_player_by_id(2).participant.vars.get('bid') is None:
            bid2 = 4.15
        else:
            bid2 = self.group.get_player_by_id(2).participant.vars.get('bid')

        matched2 = bid2 <= 5.0

        return {
            'bid2': bid2,
            'matched2': matched2,
            'budget' : Constants.budget,
            'kickin' : Constants.kickin,
            'rate' : Constants.rate*100,
            'basepay' : Constants.basepay,
        }

    form_model = 'player'
    form_fields = ['test_compre_pr']

    def test_compre_pr_error_message(self, value):
        if value != 0.75:
            return 'Incorrect'

class ManagerChat(Page):
    def is_displayed(self):
        if self.player.id_in_group == 1 and self.round_number == 1 and not self.player.outofthegame:
            return True

    def vars_for_template(self):

        if self.group.get_player_by_id(2).participant.vars.get('bid') is None:
            bid2 = c(4.15)
        else:
            bid2 = self.group.get_player_by_id(2).participant.vars.get('bid')

        matched2 = bid2 <= 5.0

        channel1 = self.group.id_in_subsession

        return {
            'bid2': bid2,
            'matched2': matched2,
            'budget' : Constants.budget,
            'kickin' : Constants.kickin,
            'rate' : Constants.rate*100,
            'basepay' : Constants.basepay,
            'channel1': channel1
        }

    form_model = 'player'
    form_fields = ['emp_price']


class EmployeeChat(Page):
    def is_displayed(self):
        if self.player.id_in_group != 1 and self.round_number == 1 and not self.player.outofthegame:
            return True

    def vars_for_template(self):
        if self.player.participant.vars.get('bid') is None:
            bid = 0
        else:
            bid = self.player.participant.vars.get('bid')
        match = bid <= 5.0
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
                'match': match,
                'enum': self.player.id_in_group - 1,
                'channel': channel,
                'split_chats': Constants.split_chats,
                'budget': Constants.budget,
                'kickin': Constants.kickin}

    form_model = 'player'
    form_fields = ['emp_price_accept']

class OptIn(Page):
    def is_displayed(self):
        if self.round_number == 1 and not self.player.outofthegame:
            return True

    def vars_for_template(self):
        if self.player.id_in_group != 1:
            return {'esurvey_text': "After the exit survey you will proceed to transcription if you came to an agreement."}
        else :
            return {'esurvey_text': ""}

class Demographics(Page):
    def is_displayed(self):
        if self.round_number == 1 and not self.player.outofthegame:
            return True

    form_model = 'player'
    form_fields = ['yearBorn', 'gender']

class Household(Page):
    def is_displayed(self):
        if self.round_number == 1 and not self.player.outofthegame:
            return True

    form_model = 'player'
    form_fields = ['experience', 'transExp', 'eduLevel', 'dailyHHEarn']

#class ThankYou(Page):
#    pass

#class NormalWaitPage(WaitPage):
#    def is_displayed(self):
#        if self.round_number == 1 and self.player.in_round(1).emp_price > 0:
#            return True

#    def after_all_players_arrive(self):
#        if self.group.get_player_by_id(1).in_round(1).emp_price == self.group.get_player_by_id(2).in_round(1).emp_price and self.group.get_player_by_id(2).in_round(1).emp_price > 0 and self.group.get_player_by_id(2).in_round(1).emp_price <= 5.00 :
#            self.group.agreed = True

class Transcribe(Page):
    def is_displayed(self):
#        if self.player.id_in_group != 1 and self.player.in_round(1).emp_price != 0 and not self.player.outofthegame and self.player.in_round(1).emp_price <= 5.0: # and self.group.in_round(1).agreed == True:
        if self.player.id_in_group != 1 and not self.player.outofthegame and self.player.in_round(1).emp_price_accept == True : # and self.group.in_round(1).agreed == True:
            return True

    form_model = 'player'
    form_fields = ['transcribed_text']

    def vars_for_template(self):
        if self.round_number == 1:
            header_text = 'You will be shown 5 pages of transcription, one on each screen.  When you click next, your transcription of the first page will be submitted and you will be presented with a fresh link to a second page of transcription and a blank text box, and so on until the fifth page. After you submit the fifth page we ask a few basic demographic questions and give you a code to submit your HIT.'
        else:
            header_text = ''
        return {
            'image_path': 'transcription/1_{}.png'.format(self.round_number),
            'reference_text': safe_json(Constants.reference_texts[0, self.round_number - 1]),
            'header_text': header_text,
            'debug': settings.DEBUG,
            'required_accuracy': 100 * (1 - Constants.allowed_error_rates[self.round_number - 1]),
            'agreed': self.group.get_player_by_id(1).in_round(1).emp_price
        }

    def transcribed_text_error_message(self, transcribed_text):
        reference_text = Constants.reference_texts[0, self.round_number - 1]
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
    #    form_model = 'group'
    #    form_fields = ['mgr_bonus']

    def is_displayed(self):
#        if self.player.id_in_group != 1 and self.round_number == Constants.num_rounds and self.player.in_round(
#                1).emp_price != 0 and not self.player.outofthegame and self.player.in_round(1).emp_price <= 5.0: # and self.group.in_round(1).agreed == True:
        if self.player.id_in_group != 1 and self.round_number == Constants.num_rounds and self.player.in_round(1).emp_price_accept == True and not self.player.outofthegame: # and self.group.in_round(1).agreed == True:
            return True

    def vars_for_template(self):
        table_rows = []
        num_good = 0
        for prev_player in self.player.in_all_rounds():
            #            accuracy = (1 - prev_player.levenshtein_distance / len(Constants.reference_texts[self.player.id_in_group-2,prev_player.round_number - 1]))*100
            accuracy = (1 - prev_player.levenshtein_distance / len(
                Constants.reference_texts[0, prev_player.round_number - 1])) * 100
            if (accuracy < 0):
                accuracy = 0
            clean_trx_text = ''.join(e for e in prev_player.transcribed_text if e.isalnum())
            clean_trx_text = clean_trx_text.replace('\n', ' ').replace('\r', '')
            row = {
                'round_number': prev_player.round_number,
                # 'reference_text_length': len(Constants.reference_texts[self.player.id_in_group-2,prev_player.round_number - 1]),
                'reference_text_length': len(Constants.reference_texts[0, prev_player.round_number - 1]),
                'transcribed_text_length': len(clean_trx_text),
                'distance': prev_player.levenshtein_distance,
                'accuracy': round(accuracy, 2)
            }
            table_rows.append(row)
            if (accuracy >= 95.0):
                num_good += 1

        if self.group.get_player_by_id(1).in_round(1).emp_price <= Constants.kickin:
            self.group.get_player_by_id(1).payoff = Constants.basepay * Constants.num_rounds + round(num_good * (Constants.budget - self.group.get_player_by_id(1).in_round(1).emp_price), 2)
        elif self.group.get_player_by_id(1).in_round(1).emp_price > Constants.kickin and self.group.get_player_by_id(1).in_round(1).emp_price <= Constants.budget:
            self.group.get_player_by_id(1).payoff = Constants.basepay * Constants.num_rounds + round(num_good* (Constants.budget - self.group.get_player_by_id(1).in_round(1).emp_price - Constants.rate * ( self.group.get_player_by_id(1).in_round(1).emp_price - Constants.kickin )), 2)
        else:
            self.group.get_player_by_id(1).payoff = 0

        self.player.payoff = round(num_good * self.group.get_player_by_id(1).in_round(1).emp_price, 2)

        return {'table_rows': table_rows,
                'num_good': num_good,
                'emp_price': self.group.get_player_by_id(1).in_round(1).emp_price,
                'emp_bonus': self.player.payoff,
                'mgr_bonus': self.group.get_player_by_id(1).payoff}


class Sorry(Page):
    def is_displayed(self):
        if self.player.id_in_group != 1 and self.round_number == 1 and not self.player.outofthegame and self.player.in_round(1).emp_price_accept == False  : # and not self.group.in_round(1).agreed == True :
            return True


page_sequence = [
    StartWP,
    ManagerPreChat,
    ManagerChat,
    EmployeeChat,
    OptIn,
    Demographics,
    Household,
#    ThankYou,    
#    NormalWaitPage,
    Transcribe,
    Results,
    Sorry
]
