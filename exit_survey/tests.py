from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

	def play_round(self):
		yield (pages.OptIn)
#		yield (pages.OptIn,{'optIn',True})
		yield (pages.Demographics, {'yearBorn': 2001, 'gender':'m'})
#		yield (pages.Household, {'experience':'some', 'transExp':'some', 'eduLevel':'someHS', 'dailyHHEarn': c(40.56)})
		yield (pages.Household)
		yield (pages.Preferences, {'pref1':'3','pref2':'4','pref3':'5','pref4':'6','pref5':'7'})
		yield (pages.ThankYou)
