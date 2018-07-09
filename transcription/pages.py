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

class Bid(Page):             

    def is_displayed(self):
        if self.player.id_in_group != 1 and not self.player.outofthegame:
            return True

    form_model = 'player'
    form_fields = ['bid']

    def vars_for_template(self):
        if self.player.participant.vars.get('tax') is None:
            self.player.tax = 0
        else:
            self.player.tax = self.player.participant.vars.get('tax')

        return{
        'tax': c(self.player.tax)
        }
   
    def before_next_page(self):
        self.participant.vars['bid'] = self.player.bid
        self.participant.vars['payoff'] = 0

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
                'budget': Constants.budget,
                'bid2': bid2,
                'bid3': bid3,
                'bid4': bid4,
                'channel1': channel1,
                'channel2': channel2,
                'channel3': channel3,
                'split_chats': Constants.split_chats
                }

    form_model = models.Player
    form_fields = ['man_emp1_price','man_emp1_nodeal','man_emp2_price','man_emp2_nodeal','man_emp3_price','man_emp3_nodeal']  

    def error_message(self, values):
        if values["man_emp1_nodeal"]==False:
            if values["man_emp1_price"] is None:
                return 'Please enter a price for Worker 1, or check box for no deal'
            elif (values["man_emp1_price"] < 0):
                return 'Your price for Worker 1 cannot be less than 0'
            elif  (values["man_emp1_price"] > 5):
                return 'Your price for Worker 1 must be less than or equal to the $5 budget!'

        if values["man_emp2_nodeal"]==False:
            if values["man_emp2_price"] is None:
                return 'Please enter a price for Worker 2, or check box for no deal'
            elif (values["man_emp2_price"] < 0):
                return 'Your price for Worker 2 cannot be less than 0'
            elif  (values["man_emp2_price"] > 5):
                return 'Your price for Worker 2 must be less than or equal to the $5 budget!'

        if values["man_emp3_nodeal"]==False:
            if values["man_emp3_price"] is None:
                return 'Please enter a price for Worker 3, or check box for no deal'
            elif (values["man_emp3_price"] < 0):
                return 'Your price for Worker 3 cannot be less than 0'
            elif  (values["man_emp3_price"] > 5):
                return 'Your price for Worker 3 must be less than or equal to the $5 budget!'

    def before_next_page(self):
        if self.player.id_in_group == 1:
            self.player.payoff = 0

            if self.player.man_emp1_nodeal == True :
                self.player.payoff += 0
            else:
                self.player.payoff += Constants.budget - self.player.man_emp1_price

            if self.player.man_emp2_nodeal == True :
                self.player.payoff += 0
            else:
                self.player.payoff += Constants.budget - self.player.man_emp2_price

            if self.player.man_emp3_nodeal == True :
                self.player.payoff += 0
            else:
                self.player.payoff += Constants.budget - self.player.man_emp3_price

            self.participant.vars['payoff'] = self.player.payoff

class EmployeeChat(Page):
    def is_displayed(self):
        if self.player.id_in_group != 1 and not self.player.outofthegame:
            return True

    def vars_for_template(self):
        if self.player.participant.vars.get('bid') is None:
            bid = 0
        else:
            bid = self.player.participant.vars.get('bid')

        if Constants.split_chats:
            if self.player.id_in_group == 2:
                channel = self.group.id_in_subsession + 1000
            elif self.player.id_in_group == 3:
                channel = self.group.id_in_subsession + 7777
            else:
                channel = self.group.id_in_subsession + 8989
        else:
            channel = self.group.id_in_subsession

        return {'tax': c(self.player.tax),
                'bid': bid,
                'example': c(4.50) - c(self.player.tax),
                'enum': self.player.id_in_group - 1,
                'channel': channel,
                'split_chats': Constants.split_chats,
                'budget': Constants.budget,
                'kickin': Constants.kickin}

    form_model = 'player'
    form_fields = ['emp_price','emp_nodeal']


    def error_message(self, values):

        if values["emp_nodeal"]==False:
            if values["emp_price"] is None:
                return 'Please enter a value for the confirmed price, or check box for no deal'
            elif (values["emp_price"] < self.player.tax):
                return 'Your price must at least cover your {} tax!'.format(self.player.tax)
#            elif  (values["emp_price"] > 5):
#                return 'Your price be less than or equal to the $5 budget!'


    def before_next_page(self):
        if self.player.id_in_group != 1:
            if self.player.emp_nodeal == False:
                self.player.payoff = max(self.player.emp_price - self.player.participant.vars.get('tax'),0) 
                self.participant.vars['payoff'] = max(self.player.emp_price - self.player.participant.vars.get('tax'),0)
            else:
                self.player.payoff = 0
                self.participant.vars['payoff'] = 0

class OptIn(Page):
    def vars_for_template(self):

        if self.player.participant.vars.get('payoff') is None:
            self.player.participant.vars['payoff'] = 0

        if self.player.payoff is None:
            self.player.payoff = 0

        if self.player.participant.vars.get('payoff') <= 0:
            text = 'You will still be paid for the HIT.'
        else :
            text = 'After it is verified that the amounts agreed, you will be paid via MTurk.'

        return {'text' : text,
                'bonus': c(self.player.participant.vars.get('payoff'))  }


class Demographics(Page):

    form_model = 'player'
    form_fields = ['yearBorn', 'gender']

class Household(Page):

    form_model = 'player'
    form_fields = ['experience', 'transExp', 'eduLevel', 'dailyHHEarn']


class Feedback(Page):
    form_model = 'player'
    form_fields = ['feedback_form']      #  INDEXED

page_sequence = [
    StartWP,
    ManagerChat,
    Bid,
    EmployeeChat,
    OptIn,
    Demographics,
    Household,
    Feedback
]
