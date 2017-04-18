from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
    	yield (views.Introduction)
		yield (views.Introduction2)
#    	yield (views.MyPage, {'MTurkID': 23},{'paymentOK':True},{'neverWorked':True},{'yearBorn':1999},{'gender':'f'})
        yield (views.Results)


#class MyPage2(Page):
#    form_fields = ['experience', 'transExp', 'eduLevel', 'dailyHHEarn']
#class MyPage3(Page):
#    form_fields = ['howLong']
#class MyPage5(Page):
#    form_fields = ['pref1','pref2','pref3','pref4','pref5']
#class MyPage6(Page):
#    form_fields = ['bid']