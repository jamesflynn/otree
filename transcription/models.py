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
    players_per_group = 4
    instructions_template = 'transcription/Instructions.html'
    manager_instructions = 'transcription/Manager_Instructions.html'
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
	pass


GENDER_CHOICES = (('','please select'),('m','Male'),('f','Female'),('o','Other'))
EXP_CHOICES = (('','please select'),('0','no experience'),('12','1-12 months'),('24','1-2 years'),('36','more than 2 years'))
TRANS_CHOICES = (('','please select'),('0','no experience') , ('12','1-12 months') , ('24','1-2 years') , ('36','more than 2 years') )
EDU_CHOICES = (('','please select'),('someHS','some high school'),('HS','completed high school'),('someColl','some college'),('undergrad','undergrad degree'),('postgrad','graduate degree'))
P1_CHOICES = (('1','$12 for five pages transcribed in 2 days'), ('2', '$10 in 2 days from now, without transcription'))
P2_CHOICES = (('1','$15 for five pages transcribed in 2 days'),('2','$10 in 2 days from now, without transcription'))
P3_CHOICES = (('1','$25 for five pages transcribed in 2 days'),('2','$10 in 2 days from now, without transcription'))
P4_CHOICES = (('1','$35 for five pages transcribed in 2 days'),('2','$10 in 2 days from now, without transcription'))
P5_CHOICES = (('1','$45 for five pages transcribed in 2 days'),('2','$10 in 2 days from now, without transcription'))
BID_CHOICES = ((None,'Please select'),('5','$5'),('10','$10'),('15','$15'),('20','$20'),('25','$25'),('30','$30'),('35','$35'),('40','$40'),('45','$45'),)

class Player(BasePlayer):

	def role(self):
	    if self.id_in_group == 1:
	        return 'Manager'
	    else:
	        return 'Employee'

	def string1(self):
		if self.id_in_group == 1:
			return 'employees'
		else:
			return 'you'

	def get_employee1(self):
		return self.get_others_in_group()[0]
	def get_employee2(self):
		return self.get_others_in_group()[1]
	def get_employee3(self):
		return self.get_others_in_group()[2]
#	def get_employee4(self):
#		return self.get_others_in_group()[3]


	MTurkID = models.CharField()
#	paymentOK = models.BooleanField(widget=widgets.CheckboxInput())
	paymentOK = models.BooleanField()
	neverWorked = models.BooleanField()
	yearBorn = models.PositiveIntegerField(min=1916, max=2005)
	gender = models.CharField(widget=widgets.Select(choices=GENDER_CHOICES))
	experience = models.CharField(widget=widgets.Select(choices=EXP_CHOICES))
	transExp = models.CharField(widget=widgets.Select(choices=TRANS_CHOICES))
	eduLevel = models.CharField(widget=widgets.Select(choices=EDU_CHOICES))
	dailyHHEarn = models.FloatField()
	howLong = models.PositiveIntegerField(max=180,widget=widgets.SliderInput(attrs={'step': '5'}))
	pref1 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P1_CHOICES))
	pref2 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P2_CHOICES))
	pref3 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P3_CHOICES))
	pref4 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P4_CHOICES))
	pref5 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P5_CHOICES))
	bid = models.PositiveIntegerField(widget=widgets.Select(choices=BID_CHOICES)) 
