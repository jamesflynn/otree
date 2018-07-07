from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player
from django.conf import settings
from random import *

class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def before_next_page(self):
        self.player.tax = randint(Constants.tax_min,Constants.tax_max)
        self.participant.vars['tax'] = self.player.tax

page_sequence = [
    Consent
]