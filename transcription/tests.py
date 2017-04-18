from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

	def play_round(self):
		yield (views.Introduction)
		yield (views.Introduction2)
		yield (views.MyPage, {'MTurkID': 23},{'paymentOK':True},{'neverWorked':True},{'yearBorn':1999},{'gender':'f'})
		yield (views.Results)
