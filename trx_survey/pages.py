from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player
from django.conf import settings
from random import *

class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

class Introduction(Page):   # extra manager intro
    def before_next_page(self):
        self.player.rand = randint(Constants.tax_min,Constants.tax_max)

class Sample(Page):      # transcription sample for manager
    form_model = 'player'
    form_fields = ['howLong']

class Preferences(Page):
    form_model = 'player'
    form_fields = ['pref1','pref2','pref3','pref4','pref5']


class Bid(Page):             

    form_model = 'player'
    form_fields = ['bid']

    def vars_for_template(self):
        self.player.tax = self.player.rand
        self.participant.vars['tax'] = self.player.tax
        return{
        'tax': c(self.player.tax)
        }
   
    def before_next_page(self):
        self.participant.vars['bid'] = self.player.bid
        self.participant.vars['payoff'] = 0

page_sequence = [
#    Consent,
    Introduction,
#    Sample,
#    Preferences,
    Bid
]