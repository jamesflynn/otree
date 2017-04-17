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


#class ResultsWaitPage(WaitPage):

#    def after_all_players_arrive(self):
 #       pass


class Results(Page):
    pass


page_sequence = [
	Introduction,
	Introduction2,
    MyPage,
#    ResultsWaitPage,
    Results
]
