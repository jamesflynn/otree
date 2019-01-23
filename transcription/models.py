from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# from settings import SESSION_CONFIGS


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

def append_string_to_list(mylist,mystring):
    mylist.append(mystring)

def distance_and_ok(transcribed_text, reference_text, max_error_rate):
    error_threshold = len(reference_text) * max_error_rate
    distance = levenshtein(transcribed_text, reference_text)
    ok = distance <= error_threshold
    return distance, ok

class Constants(BaseConstants):
    name_in_url = 'transcription'
    players_per_group = 4
    num_rounds = 1
    split_chats = settings.SPLIT
    reference_text = [ \
    "58177711597413989789449192401349279129120723141031173203322840521170112069231612707413352112996231258421502310726433518818263923914214795635945340183743426550106363373351414341865391554323208118971187261594212235231607150226744424114570362341241411111843424165527128346132312592720344122331812212222671341431369185131961012122451514245814645881986774672618431783426238431034321512211541043462811352535215112281342412111126232198413278641146241371111734451149672625165221388261714184322986420842381222100341021311144695310482051284123625113225612068981566276102816231112027451361282115949464241171123595912996561832315675312762117163901937615261613850291831372305811173631224921491573101712641120270634127155524517452352227111181742634087141796234774185111130634017811106542918323815128326711471293161647382780105746519910513211441130117173891298085227945586256941212987240313118109089639534222157664429131817227621042323114421142176314282211603304811047068107112886614131143351221317247481317409018741194459293160110111966913539258145634810513652671082485114140765449412422701380406449431873038123134010105813116076431432431611493666278124153573243018111311782363737141311256503151149032131661567692580172106491361847254123122232211",\
    "59361414460252255323751101159511247221342316842111064506901931621155124119227323503925715136511164822472205267110321421110740416532241031121115711121183111114211312231711141231113128411431107214111541312113121112225203111033121129348412634921108111122761419211111007216597114913511221472681231212102421146520533196931112901242161266243118640414826413613212112111053521131351211672114117112113051334112148513281961651811741153211541253166144122211117433413121122611111335332111115175114426171841132149232111112713253312266513",\
    "1571910637388155484550376224112274274813261320761141929134615312215583381010145151791571083772124423196443126127244217711151667313111111431111311415114121121111001740232819531284693925311117471001228118971161192117411214894221151146133342163773312133156814121583526541911874514331882139611172102521242616211413162215224105811662126215722611638126511151113211222492421211933321431123211515536171310362292312111173221238282042223282161411353121151216112871141111111121143122221131762486111151225411111211411111",\
    "12991343322263761282046371485618767410788148127331161494480491046015165101823402651251268565321228536368268985122234109471779171363431271036401364451106887361354835542153505405095047087142913164651278337964121822872228111915111117311171121211531131222114211112111111117641616237462671042072111915546144221121114153111113333514661118161244151313111312171266258314771222134162616532331022311128221321201717231163226015917111315667112443124294312478361318113481230834113191211114217791437102534291315211484829104211718716261329257541511182117123454171645252291762662541371073134187273107342485183881595997117852422833109364150140133222411523124371156141223221115412751866421521171837515038914480758496142613528919471715331257353341492315540157227531486383216113159311644511162236416104142141025812835542755139202177756121126121122195234341115113222622333482125094741843112461141731144141755136335351012212703941512134734121203347111297310243521522794104521475121187723214011088212221112617952116211423276",\
    "682156145306785237520141615361344193435661262188225180373811130171137118941749105157124574531302102637552346104951286254888957151525147240265612016551062672346261505961955452325267142083452927148117631170823216131211121124444211114712456922211437112155831111181611192151122211239632321216422448127244103937122516921411210731812112151521943318912222311713214314451008966131423261432273649608981917681171822131124141361518259591621119159243744068191244662214231111221113811614722211216421102275871421417218411313952102846658382236512514551491333241062161441459206621917463361571134413522291651921217164412171033791231837332912192521741234210912688101111285167107591132914933112131580747986503354958699293735110077919262281310434011945322510505427782856183406316121332462066411544512746538124161111358482620118170392462421121411112211114211881311021152194814122611275641073481143123024692124"\
    ]
    allowed_error_rate = 3
    startwp_timer = 300

    budget = c(5.00)
    kickin = c(4.00)
    rate = 2
    basepay = c(2.00)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
#    agreed = models.BooleanField(default=False)
    pass

TEST_CHOICES = (('','please select'),(0.66,'$0.66'),(0.70,'$0.70'),(0.75,'$0.75'),(0.8,'$0.80'),(1.0,'$1.00'))
BOOL_CHOICES = ((True,'Yes'),(False,'No Agreement'))
GENDER_CHOICES = (('','please select'),('m','male'),('f','female'),('o','other'),('opt_out','I\'d rather not say'))
EXP_CHOICES = (('','please select'),('none','no experience'),('some','some experience'),('very','very experienced'),('opt_out','I\'d rather not say'))
TRANS_CHOICES = (('','please select'),('none','no experience') , ('some','some experience') , ('very','very experienced') , ('opt_out','I\'d rather not say'))
EDU_CHOICES = (('','please select'),('someHS','some high school'),('HS','completed high school'),('someColl','some college'),('undergrad','undergrad degree'),('postgrad','graduate degree'),('opt_out','I\'d rather not say'))


class Player(BasePlayer):

    def role(self):
        if self.id_in_group == 1:
            return 'Manager'
        else:
            return 'Employee'
	
    def chat_nickname(self):
        return '{}'.format(self.role())

    transcribed_text_1 = models.LongStringField(blank=True)
    levenshtein_distance_1 = models.PositiveIntegerField()
    transcribed_text_2 = models.LongStringField(blank=True)
    levenshtein_distance_2 = models.PositiveIntegerField()
    transcribed_text_3 = models.LongStringField(blank=True)
    levenshtein_distance_3 = models.PositiveIntegerField()
    transcribed_text_4 = models.LongStringField(blank=True)
    levenshtein_distance_4 = models.PositiveIntegerField()
    transcribed_text_5 = models.LongStringField(blank=True)
    levenshtein_distance_5 = models.PositiveIntegerField()

    bid = models.CurrencyField()

    emp_price = models.CurrencyField(max=5.00,min=0.00)
    test_compre_pr = models.CurrencyField(widget=widgets.Select(choices=TEST_CHOICES))
#    emp_price_accept = models.BooleanField(widget=widgets.RadioSelectHorizontal(choices=BOOL_CHOICES))
    man_emp1_price = models.CurrencyField()
    man_emp1_accpt = models.BooleanField()
    man_emp2_price = models.CurrencyField()
    man_emp2_accpt = models.BooleanField()
    man_emp3_price = models.CurrencyField()
    man_emp3_accpt = models.BooleanField()
    startwp_timer_set = models.BooleanField(default=False)
    startwp_time = models.PositiveIntegerField()
    outofthegame = models.BooleanField()
    yearBorn = models.PositiveIntegerField(min=1916, max=2005)
    gender = models.StringField(widget=widgets.Select(choices=GENDER_CHOICES))
    experience = models.StringField(widget=widgets.Select(choices=EXP_CHOICES))
    transExp = models.StringField(widget=widgets.Select(choices=TRANS_CHOICES))
    eduLevel = models.StringField(widget=widgets.Select(choices=EDU_CHOICES))
    dailyHHEarn = models.CurrencyField()
    feedback_form = models.LongStringField(widget=widgets.Textarea,blank=True)


