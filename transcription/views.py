from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.conf import settings


class ResultsWaitPage(WaitPage):
    group_by_arrival_time = True
    
    def is_displayed(self):
        if ( self.round_number == 1 ):
            return True    
    def after_all_players_arrive(self):
        pass


class ManagerChat(Page):
    def is_displayed(self):
        if ( self.player.id_in_group == 1 ) & ( self.round_number == 1 ):
            return True

    def vars_for_template(self):
        bid2 = self.group.get_player_by_id(2).participant.vars['bid']
        bid3 = self.group.get_player_by_id(3).participant.vars['bid']
        bid4 = self.group.get_player_by_id(4).participant.vars['bid']
        return {
                'bid2': bid2,
                'bid3': bid3,
                'bid4': bid4
                }

    form_model = models.Player
    form_fields = ['agree2','agree3','agree4']

class EmployeeChat(Page):
    def is_displayed(self):
        if ( self.player.id_in_group != 1 ) & ( self.round_number == 1 ):
            return True
    def vars_for_template(self):
        bid = self.player.participant.vars['bid']
        return { 'bid': bid,
                 'enum': self.player.id_in_group -1 }

    form_model = models.Player
    form_fields = ['agree1']



class Transcribe(Page):

    def is_displayed(self):        
        if (((self.player.in_round(1).iQuit == 1)|(self.player.in_round(2).iQuit == 1)|(self.player.in_round(3).iQuit == 1)|(self.player.in_round(4).iQuit == 1)|(self.player.in_round(5).iQuit == 1)) | ( self.player.id_in_group == 1)):
            return False
        else:
            return True

    form_model = models.Player
    form_fields = ['transcribed_text','iQuit']

    def vars_for_template(self):

        return {
            'image_path': 'https://dl.dropboxusercontent.com/u/1688949/trx/{}_{}.png'.format(self.player.id_in_group,
                self.round_number),
            'debug': settings.DEBUG,
            'skipping': self.player.in_round(1).devSkip        }


page_sequence = [
    ResultsWaitPage,
    ManagerChat,
    EmployeeChat,
    Transcribe
]