from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page
from .models import Constants
from django.conf import settings

class Demographics(Page):
    form_model = models.Player
    form_fields = ['yearBorn', 'gender']

class Household(Page):
    form_model = models.Player
    form_fields = ['experience', 'transExp', 'eduLevel', 'dailyHHEarn']

class Preferences(Page):
    form_model = models.Player
    form_fields = ['pref1','pref2','pref3','pref4','pref5']

class ThankYou(Page):
    pass

page_sequence = [
    Demographics,
    Household,
	Preferences,
	ThankYou
	]