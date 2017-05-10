from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.conf import settings

class Introduction(Page):   # extra manager intro
    pass

class Sample(Page):      # transcription sample for manager
    form_model = models.Player
    form_fields = ['howLong']

class Preferences(Page):
    form_model = models.Player
    form_fields = ['pref1','pref2','pref3','pref4','pref5']

class Bid(Page):             
    form_model = models.Player
    form_fields = ['bid']
   
    def before_next_page(self):
        self.participant.vars['bid'] = self.player.bid

page_sequence = [

    Introduction,
    Sample,
    Preferences,
    Bid
]