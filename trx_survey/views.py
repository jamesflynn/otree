from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player
from django.conf import settings

#------
from otree.views.abstract import get_view_from_url
from otree.api import widgets
import random
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from otree.models_concrete import (
    PageCompletion, CompletedSubsessionWaitPage,
    CompletedGroupWaitPage, PageTimeout, UndefinedFormModel,
    ParticipantLockModel, GlobalLockModel, ParticipantToPlayerLookup
)
import time
import channels
import json
#------

class Introduction(Page):   # extra manager intro
    pass

class Sample(Page):      # transcription sample for manager
    form_model = models.Player
    form_fields = ['howLong']

class Preferences(Page):
    form_model = models.Player
    form_fields = ['pref1','pref2','pref3','pref4','pref5']

class Bid(Page):             
    form_model = models.Player
    form_fields = ['bid']
   
    def before_next_page(self):
        self.participant.vars['bid'] = self.player.bid

page_sequence = [

    Introduction,
    Sample,
    Preferences,
    Bid
]