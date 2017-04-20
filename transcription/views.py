from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    timeout_seconds = 60
    pass

class Manager_Introduction(Page):
    timeout_seconds = 60

    def is_displayed(self):
        return self.player.id_in_group == 1

class MyPage(Page):
    timeout_seconds = 180
    form_model = models.Player
    form_fields = ['MTurkID', 'paymentOK', 'neverWorked', 'yearBorn', 'gender']

class SurveyManager(Page):
    timeout_seconds = 120
    def is_displayed(self):
        return self.player.id_in_group == 1
    form_model = models.Player
    form_fields = ['experience', 'eduLevel', 'dailyHHEarn']

class SurveyEmployee(Page):
    timeout_seconds = 120
    def is_displayed(self):
        return self.player.id_in_group != 1
    form_model = models.Player
    form_fields = ['transExp', 'eduLevel', 'dailyHHEarn']

class MyPage3(Page):
    timeout_seconds = 120
    form_model = models.Player
    form_fields = ['howLong']

class MyPage4(Page):
    timeout_seconds = 120
    def is_displayed(self):
        return self.player.id_in_group == 1

class MyPage5(Page):
    timeout_seconds = 180
    form_model = models.Player
    form_fields = ['pref1','pref2','pref3','pref4','pref5']

class MyPage6(Page):
    timeout_seconds = 180
    form_model = models.Player
    form_fields = ['bid']

class ManagerChat(Page):
    timeout_seconds = 1800
    def is_displayed(self):
        return self.player.id_in_group == 1

class EmployeeChat(Page):
    timeout_seconds = 1800
    def is_displayed(self):
        return self.player.id_in_group != 1

#    form_fields = ['experience', 'transExp']

class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.player.id_in_group == 1
    def after_all_players_arrive(self):
        pass


page_sequence = [
	Introduction,
	Manager_Introduction,
    MyPage,
    SurveyManager,
    SurveyEmployee,
    MyPage4,
    MyPage3,
    MyPage5,
    MyPage6,
    ResultsWaitPage,
    ManagerChat,
    EmployeeChat
]
