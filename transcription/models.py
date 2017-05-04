from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            _('%(value)s is not an acceptable answer'),
            params={'value': value},
        )


author = 'James Flynn'

doc = """
Transcription Negotiation
"""

class Constants(BaseConstants):
    name_in_url = 'transcription'
    players_per_group = 4
    num_rounds = 5
    reference_texts = [
    	"Revealed preference",
    	"Revealed preference",
    	"Revealed preference",
		"Revealed preference",
		"Revealed preference"   
    ]
#    allowed_error_rates = [0, 0.03,0.03,0.03,0.03]
    allowed_error_rates = [1,1,1,1,1]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
	pass


GENDER_CHOICES = (('','please select'),('m','male'),('f','female'),('o','other'))
EXP_CHOICES = (('','please select'),('0','no experience'),('12','1-12 months'),('24','1-2 years'),('36','more than 2 years'))
TRANS_CHOICES = (('','please select'),('0','no experience') , ('12','1-12 months') , ('24','1-2 years') , ('36','more than 2 years') )
EDU_CHOICES = (('','please select'),('someHS','some high school'),('HS','completed high school'),('someColl','some college'),('undergrad','undergrad degree'),('postgrad','graduate degree'))
P1_CHOICES = (('3','$3 each page for up to five pages of transcription'),('2','$2 only, without transcription'))
P2_CHOICES = (('4','$4 each page for up to five pages of transcription'),('2','$2 only, without transcription'))
P3_CHOICES = (('5','$5 each page for up to five pages of transcription'),('2','$2 only, without transcription'))
P4_CHOICES = (('6','$6 each page for up to five pages of transcription'),('2','$2 only, without transcription'))
P5_CHOICES = (('7','$7 each page for up to five pages of transcription'),('2','$2 only, without transcription'))
#BID_CHOICES = ((None,'Please select'),('5','$5'),('10','$10'),('15','$15'),('20','$20'),('25','$25'),('30','$30'),('35','$35'),('40','$40'),('45','$45'),)

class Player(BasePlayer):

	def role(self):
	    if self.id_in_group == 1:
	        return 'Manager'
	    else:
	        return 'Employee'
	
	def chat_nickname(self):
		return '{} {}'.format(self.role(), self.id_in_group - 1 )

	def get_employee1(self):
		return self.get_others_in_group()[0]
	def get_employee2(self):
		return self.get_others_in_group()[1]
	def get_employee3(self):
		return self.get_others_in_group()[2]

#	def get_employee4(self):
#		return self.get_others_in_group()[3]

	transcribed_text = models.TextField(blank=True)
#	levenshtein_distance = models.PositiveIntegerField()
#	MTurkID = models.CharField()
#	paymentOK = models.BooleanField(widget=widgets.CheckboxInput())
	devSkip = models.BooleanField(blank=True)
	iQuit = models.PositiveIntegerField(min=0,max=1)
#	paymentOK = models.BooleanField()
#	neverWorked = models.BooleanField()
#	yearBorn = models.PositiveIntegerField(min=1916, max=2005)
#	gender = models.CharField(widget=widgets.Select(choices=GENDER_CHOICES))
#	experience = models.CharField(widget=widgets.Select(choices=EXP_CHOICES))
#	transExp = models.CharField(widget=widgets.Select(choices=TRANS_CHOICES))
#	eduLevel = models.CharField(widget=widgets.Select(choices=EDU_CHOICES))
#	dailyHHEarn = models.CurrencyField()
#	howLong = models.PositiveIntegerField(validators=[validate_nonzero],default=0,min=0,max=180,widget=widgets.SliderInput(attrs={'step': '5'}))
#	pref1 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P1_CHOICES))
#	pref2 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P2_CHOICES))
#	pref3 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P3_CHOICES))
#	pref4 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P4_CHOICES))
#	pref5 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P5_CHOICES))
#	bid = models.PositiveIntegerField(widget=widgets.Select(choices=BID_CHOICES)) 
#	bid = models.CurrencyField()
	agree1 = models.CurrencyField(min=0,max=100)
	agree2 = models.CurrencyField(min=0,max=5) 
	agree3 = models.CurrencyField(min=0,max=5)
	agree4 = models.CurrencyField(min=0,max=5)


