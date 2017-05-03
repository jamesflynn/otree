from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.conf import settings

class AcceptTerms(Page):
    timeout_seconds = 180
    form_model = models.Player
    form_fields = ['paymentOK', 'neverWorked', 'yearBorn', 'gender']


class Introduction(Page):   # extra manager intro
    timeout_seconds = 180
    def is_displayed(self):
        if ( self.player.devSkip == None ):
            return True

class Survey(Page):      # survey for manager
    timeout_seconds = 180
    def is_displayed(self):
        if ( self.player.devSkip == None ):
            return True
    form_model = models.Player
    form_fields = ['experience', 'transExp', 'eduLevel', 'dailyHHEarn']

class Sample(Page):      # transcription sample for manager
    def is_displayed(self):
        if ( self.player.devSkip == None ):
            return True
    timeout_seconds = 180
    form_model = models.Player
    form_fields = ['howLong']

class Preferences(Page):    # preferences survey for eployee
    def is_displayed(self):
        if ( self.player.devSkip == None ):
            return True
    timeout_seconds = 180
    form_model = models.Player
    form_fields = ['pref1','pref2','pref3','pref4','pref5']

class Bid(Page):             
    timeout_seconds = 180
    form_model = models.Player
    form_fields = ['bid']
   
    def before_next_page(self):
        self.participant.vars['bid'] = self.player.bid

page_sequence = [

    AcceptTerms,
    Introduction,
    Survey,
    Sample,
    Preferences,
    Bid
]