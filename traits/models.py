from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django import forms
from django.conf import settings

author = 'Your name here'

doc = """
Your app description
"""

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            _('%(value)s is not an acceptable answer'),
            params={'value': value},
        )
        
class Constants(BaseConstants):
    name_in_url = 'traits'
    players_per_group = None
    num_rounds = 2
    who = ['Your Partner\'s','Your']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
	def get_partner(self):
		return self.get_others_in_group()[0]

	frndlyHstl 	= models.PositiveIntegerField()
	authPhny 	= models.PositiveIntegerField()
	nonDfDf 	= models.PositiveIntegerField()
	wrmCld 		= models.PositiveIntegerField()
	flxRgd 		= models.PositiveIntegerField()
	genStgy 	= models.PositiveIntegerField()
	hnstDcptv 	= models.PositiveIntegerField()
	indpDep 	= models.PositiveIntegerField()
	rlxTns 		= models.PositiveIntegerField()
	gdHumUnhppy = models.PositiveIntegerField()
	adltChld 	= models.PositiveIntegerField()
	rlstNrcsstc = models.PositiveIntegerField()
	sexAlvRprsd = models.PositiveIntegerField()
	outgngInwrd = models.PositiveIntegerField()
	rspflIntrsv = models.PositiveIntegerField()
	frAddAdd 	= models.PositiveIntegerField()
	acptJdgmntl = models.PositiveIntegerField()
	gdJdgImplsv = models.PositiveIntegerField()
	attrSlppy 	= models.PositiveIntegerField()
	assrtDny	= models.PositiveIntegerField()
	actvPssv 	= models.PositiveIntegerField()

#	frndlyHstl 	= models.PositiveIntegerField()
#	authPhny 	= models.PositiveIntegerField()
#	nonDfDf 	= models.PositiveIntegerField()
#	wrmCld 		= models.PositiveIntegerField()
#	flxRgd 		= models.PositiveIntegerField()
#	genStgy 	= models.PositiveIntegerField()
#	hnstDcptv 	= models.PositiveIntegerField()
#	indpDep 	= models.PositiveIntegerField()
#	rlxTns 		= models.PositiveIntegerField()
#	gdHumUnhppy = models.PositiveIntegerField()
#	adltChld 	= models.PositiveIntegerField()
#	rlstNrcsstc = models.PositiveIntegerField()
#	sexAlvRprsd = models.PositiveIntegerField()
#	outgngInwrd = models.PositiveIntegerField()
#	rspflIntrsv = models.PositiveIntegerField()
#	frAddAdd 	= models.PositiveIntegerField()
#	acptJdgmntl = models.PositiveIntegerField()
#	gdJdgImplsv = models.PositiveIntegerField()
#	attrSlppy 	= models.PositiveIntegerField()
#	assrtDny	= models.PositiveIntegerField()
#	actvPssv 	= models.PositiveIntegerField()
	
