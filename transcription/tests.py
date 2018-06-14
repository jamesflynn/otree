from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

	def play_round(self):
		yield (pages.Introduction)
		yield (pages.Sample, {'howLong': 25})
		yield (pages.Bid, {'bid': 40.56})
