from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):       # both
    timeout_seconds = 60
    pass

class Manager_Introduction(Page):   # extra manager intro
    timeout_seconds = 60
    def is_displayed(self):
        if ( self.player.id_in_group == 1 ):
            return True

class AcceptTerms(Page):        # both
    timeout_seconds = 180
    form_model = models.Player
    form_fields = ['MTurkID', 'paymentOK', 'neverWorked', 'yearBorn', 'gender']

class SurveyManager(Page):      # survey for manager
    timeout_seconds = 120
    def is_displayed(self):
        return self.player.id_in_group == 1
    form_model = models.Player
    form_fields = ['experience', 'eduLevel', 'dailyHHEarn']

class SurveyEmployee(Page):     # survey for employee
    timeout_seconds = 120
    def is_displayed(self):
        return self.player.id_in_group != 1
    form_model = models.Player
    form_fields = ['transExp', 'eduLevel', 'dailyHHEarn']

class SampleManager(Page):      # transcription sample for manager
    def is_displayed(self):
        return self.player.id_in_group == 1
    timeout_seconds = 120
    pass
 
class SampleEmployee(Page):     #transcription sample for employee with time estimate
    def is_displayed(self):
        return self.player.id_in_group != 1
    timeout_seconds = 120
    form_model = models.Player
    form_fields = ['howLong']

class PreferencesEmployee(Page):    # preferences survey for eployee
    def is_displayed(self):
        return self.player.id_in_group != 1
    timeout_seconds = 180
    form_model = models.Player
    form_fields = ['pref1','pref2','pref3','pref4','pref5']

class BidManager(Page):             # bid for manager
    def is_displayed(self):
        return self.player.id_in_group == 1
    timeout_seconds = 180
    pass

class BidEmployee(Page):        # bid for employee
    def is_displayed(self):
        return self.player.id_in_group != 1
    timeout_seconds = 180
    form_model = models.Player
    form_fields = ['bid']

class PreChatManager(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1
    timeout_seconds = 300
    pass

class PreChatEmployee(Page):
    def is_displayed(self):
        return self.player.id_in_group != 1
    timeout_seconds = 300
    pass

class ManagerChat(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1
#    timeout_seconds = 1800
    pass

class EmployeeChat(Page):
    def is_displayed(self):
        return self.player.id_in_group != 1
#    timeout_seconds = 1800
    pass

#    form_fields = ['experience', 'transExp']

class ResultsWaitPage(WaitPage):
#    def is_displayed(self):
#        return self.player.id_in_group == 1
    def after_all_players_arrive(self):
        pass


page_sequence = [
	Introduction,
	Manager_Introduction,
    AcceptTerms,
    SurveyManager,
    SurveyEmployee,
    SampleManager,
    SampleEmployee,
    PreferencesEmployee,
    BidManager,
    BidEmployee,
    PreChatManager,
    PreChatEmployee,
    ResultsWaitPage,
    ManagerChat,
    EmployeeChat
]
