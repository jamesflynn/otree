from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'transcription'
    players_per_group = None
    instructions_template = 'transcription/Instructions.html'
    instructions_template2 = 'transcription/Instructions2.html'
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
	MTurkID = models.CharField()
	paymentOK = models.BooleanField(required=True,widget=widgets.CheckboxInput())
	neverWorked = models.BooleanField()
	yearBorn = models.PositiveIntegerField()
	gender = models.CharField()
	experience = models.CharField()
	eduLevel = models.CharField()
	dailyHHEarn = models.FloatField()
	howLong = models.PositiveIntegerField()
	pref1 = models.PositiveIntegerField()
	pref2 = models.PositiveIntegerField()
	pref3 = models.PositiveIntegerField()
	pref4 = models.PositiveIntegerField()
	pref5 = models.PositiveIntegerField()
	bid = models.PositiveIntegerField() 
