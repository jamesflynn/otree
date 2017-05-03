from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.conf import settings


class ResultsWaitPage(WaitPage):
    group_by_arrival_time = True
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
        return { 'bid': bid }

    form_model = models.Player
    form_fields = ['agree1']



class Transcribe(Page):

    def is_displayed(self):        
        if (( self.round_number > 1 ) & ((self.player.in_round(1).iQuit == 1)|(self.player.in_round(2).iQuit == 1)|(self.player.in_round(3).iQuit == 1)|(self.player.in_round(4).iQuit == 1)|(self.player.in_round(5).iQuit == 1)) ) | ( self.player.id_in_group == 1):
            return False
        else:
            return True

    form_model = models.Player
    form_fields = ['transcribed_text','iQuit']

    def vars_for_template(self):

        return {
            'image_path': 'https://dl.dropboxusercontent.com/u/1688949/trx/{}_{}.png'.format(self.player.id_in_group,
                self.round_number),
            'reference_text': safe_json(Constants.reference_texts[self.round_number - 1]),
            'debug': settings.DEBUG,
            'required_accuracy': 100 * (1 - Constants.allowed_error_rates[self.round_number - 1]),
            'skipping': self.player.in_round(1).devSkip,
            'agreed': self.player.in_round(1).agree1
        }

    def transcribed_text_error_message(self, transcribed_text):
        reference_text = Constants.reference_texts[self.round_number - 1]
        allowed_error_rate = Constants.allowed_error_rates[
            self.round_number - 1]
        distance, ok = distance_and_ok(transcribed_text, reference_text,
                                       allowed_error_rate)
        if ok:
            self.player.levenshtein_distance = distance
        else:
            if allowed_error_rate == 0:
                return "The transcription should be exactly the same as on the image."
            else:
                return "This transcription appears to contain too many errors."

    def before_next_page(self):
        self.player.payoff = 0

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        table_rows = []
        for prev_player in self.player.in_all_rounds():
            row = {
                'round_number': prev_player.round_number,
                'reference_text_length': len(Constants.reference_texts[prev_player.round_number - 1]),
                'transcribed_text_length': len(prev_player.transcribed_text),
                'distance': prev_player.levenshtein_distance,
            }
            table_rows.append(row)

        return {'table_rows': table_rows}


#page_sequence = [Introduction, Transcribe, Results]

page_sequence = [
    ResultsWaitPage,
    ManagerChat,
    EmployeeChat,
    Transcribe
]