from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player
from django.conf import settings

class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

class Introduction(Page):   # extra manager intro
    pass

class Sample(Page):      # transcription sample for manager
    form_model = 'player'
    form_fields = ['howLong']

class Preferences(Page):
    form_model = 'player'
    form_fields = ['pref1','pref2','pref3','pref4','pref5']

class Bid(Page):             

    form_model = 'player'
    form_fields = ['bid']
    
    
    def error_message(self, values):

        if values["bid"] is None:
            return 'Please enter a value for your bid'
        elif (values["bid"] < 0):
            return 'Your bid must be greater than 0'
   
    def before_next_page(self):
        self.participant.vars['bid'] = self.player.bid

page_sequence = [
    Consent,
    Introduction,
    Sample,
    Preferences,
    Bid
]