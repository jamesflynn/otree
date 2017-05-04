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

def levenshtein(a, b):
    """Calculates the Levenshtein distance between a and b."""
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]


def distance_and_ok(transcribed_text, reference_text, max_error_rate):
    error_threshold = len(reference_text) * max_error_rate
    distance = levenshtein(transcribed_text, reference_text)
    ok = distance <= error_threshold
    return distance, ok

class Constants(BaseConstants):
    name_in_url = 'transcription'
    players_per_group = 4
    num_rounds = 5
    reference_texts = [
    	"2,3,4,32,3,2,2,",
    	"2,3,2,2,3,2,1,1,2,3,3,",
    	"234,234,,,23,235,235,,",
		"345345,345,345,34,,22,123,",
		"2342,23,234,25,25,,"   
    ]
    allowed_error_rates = [1,1,1,1,1]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
	pass

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

	transcribed_text = models.TextField(blank=True)
	levenshtein_distance = models.PositiveIntegerField()
	iQuit = models.PositiveIntegerField(min=0,max=1)
	agree1 = models.CurrencyField(min=0,max=100)
	agree2 = models.CurrencyField(min=0,max=5) 
	agree3 = models.CurrencyField(min=0,max=5)
	agree4 = models.CurrencyField(min=0,max=5)


