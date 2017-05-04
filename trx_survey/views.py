from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.conf import settings

class Introduction(Page):   # extra manager intro
    def is_displayed(self):
        if ( self.player.devSkip == None ):
            return True

class Sample(Page):      # transcription sample for manager
    def is_displayed(self):
        if ( self.player.devSkip == None ):
            return True
    form_model = models.Player
    form_fields = ['howLong']

class Bid(Page):             
    form_model = models.Player
    form_fields = ['bid']
   
    def before_next_page(self):
        self.participant.vars['bid'] = self.player.bid

page_sequence = [

    Introduction,
    Sample,
    Bid
]