from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

	def play_round(self):
		yield (views.Introduction)
		yield (views.Sample, {'howLong': 25})
		yield (views.Bid, {'bid': 40.56})
