from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass
class Introduction2(Page):
    pass

class MyPage(Page):
    form_model = models.Player
    form_fields = ['MTurkID', 'paymentOK', 'neverWorked', 'yearBorn', 'gender']

class MyPage2(Page):
    form_model = models.Player
    form_fields = ['experience', 'transExp', 'eduLevel', 'dailyHHEarn']

class MyPage3(Page):
    form_model = models.Player
    form_fields = ['howLong']

class MyPage4(Page):
	pass

class MyPage5(Page):
    form_model = models.Player
    form_fields = ['pref1','pref2','pref3','pref4','pref5']

class MyPage6(Page):
    form_model = models.Player
    form_fields = ['bid']

class MyPage7(Page):
	pass
#    form_fields = ['experience', 'transExp']

#class ResultsWaitPage(WaitPage):

#    def after_all_players_arrive(self):
 #       pass


class Results(Page):
    pass


page_sequence = [
	Introduction,
	Introduction2,
    MyPage,
    MyPage2,
    MyPage4,
    MyPage3,
    MyPage5,
    MyPage6,
    MyPage7,
#    ResultsWaitPage,
    Results
]
