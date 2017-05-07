from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

	def play_round(self):
		yield (views.OptIn)
#		yield (views.OptIn,{'optIn',True})
		yield (views.Demographics, {'yearBorn': 2001, 'gender':'m'})
#		yield (views.Household, {'experience':'some', 'transExp':'some', 'eduLevel':'someHS', 'dailyHHEarn': c(40.56)})
		yield (views.Household)
		yield (views.Preferences, {'pref1':'3','pref2':'4','pref3':'5','pref4':'6','pref5':'7'})
		yield (views.ThankYou)
