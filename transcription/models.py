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


def distance_and_ok(transcribed_text, reference_text, max_error_rate):
    error_threshold = len(reference_text) * max_error_rate
    distance = levenshtein(transcribed_text, reference_text)
    ok = distance <= error_threshold
    return distance, ok

def get_trx(lookup):
    if ( lookup == '1_1'):
        return '''58177711597413989789449192401349279129120723141031173203322840521170112069231612707413352112996231258421502310726433518818263923914214795635945340183743426550106363373351414341865391554323208118971187261594212235231607150226744424114570362341241411111843424165527128346132312592720344122331812212222671341431369185131961012122451514245814645881986774672618431783426238431034321512211541043462811352535215112281342412111126232198413278641146241371111734451149672625165221388261714184322986420842381222100341021311144695310482051284123625113225612068981566276102816231112027451361282115949464241171123595912996561832315675312762117163901937615261613850291831372305811173631224921491573101712641120270634127155524517452352227111181742634087141796234774185111130634017811106542918323815128326711471293161647382780105746519910513211441130117173891298085227945586256941212987240313118109089639534222157664429131817227621042323114421142176314282211603304811047068107112886614131143351221317247481317409018741194459293160110111966913539258145634810513652671082485114140765449412422701380406449431873038123134010105813116076431432431611493666278124153573243018111311782363737141311256503151149032131661567692580172106491361847254123122232211'''
#        return '''93011388256522661924647511218289797014903143326092121772811322222114465823436308513158863492151280485956723155924475222528978457037015953332519517270831967651859596463207464727105733225637137962552041016402540546624138711755170231203914181568821180110189922743733449506543011111111111111119422171211232132111421111211227251161593221111223111142112111111114121321321111023539157332692722106362024109151166103524161212134214821138231162171262251415557521221132122112031221235241372412112621152131215411115211123488124033116121121311154132163111211312211142461114142511224132113126616331131212425222713121072611321311125467141111857321391086164223171751130745515111133732543761211211'''
    elif ( lookup == '1_2'):
        return '''59361414460252255323751101159511247221342316842111064506901931621155124119227323503925715136511164822472205267110321421110740416532241031121115711121183111114211312231711141231113128411431107214111541312113121112225203111033121129348412634921108111122761419211111007216597114913511221472681231212102421146520533196931112901242161266243118640414826413613212112111053521131351211672114117112113051334112148513281961651811741153211541253166144122211117433413121122611111335332111115175114426171841132149232111112713253312266513'''
#        return '''431243941972184801631738727935661684747139358494862292288636899390615497226629586031096330115712301199135661423651494241026580426720597571224154738933848257517863120433171763823571967251973659517520401109168328954146991553286844503495196536871291491238724706948741211144132312612851081088944497767974011275119352352261129128450316766153001656717113291538603211132111111111111111294912211832111312105311512112221122211132371211111111331133184932222221141121161511421111221143910120146492022145752923810703415113710195322235111364122104356411297741452421191492511517274120942611522111222113212211115353096312621121272213299661153115311633111371166202311627109621254311512211114342115422710762112111141819424413679333181141293141115412246410616110371914994220302541209111211251842121144520106121182172141935477332117226212111611231121111728372918412458929243971620302623115411641182516611'''
    elif ( lookup == '1_3'):
        return '''1571910637388155484550376224112274274813261320761141929134615312215583381010145151791571083772124423196443126127244217711151667313111111431111311415114121121111001740232819531284693925311117471001228118971161192117411214894221151146133342163773312133156814121583526541911874514331882139611172102521242616211413162215224105811662126215722611638126511151113211222492421211933321431123211515536171310362292312111173221238282042223282161411353121151216112871141111111121143122221131762486111151225411111211411111'''
#        return '''2934630846993498112660134628215944151812714775257744779094173711847151956959110580307842439511025275225652660582222681403183717210339223923561547731728112566589809154120921753341534714490356139086291343227112441606166591784797284642302121647364572314309381111623121142112111111211111183411111222111131112161453715411436958741281166421681172754114256564211111913423211510325122211883322114422223317114115345212111466115211195223111115414121211111111'''
    elif ( lookup == '1_4'):
        return '''12991343322263761282046371485618767410788148127331161494480491046015165101823402651251268565321228536368268985122234109471779171363431271036401364451106887361354835542153505405095047087142913164651278337964121822872228111915111117311171121211531131222114211112111111117641616237462671042072111915546144221121114153111113333514661118161244151313111312171266258314771222134162616532331022311128221321201717231163226015917111315667112443124294312478361318113481230834113191211114217791437102534291315211484829104211718716261329257541511182117123454171645252291762662541371073134187273107342485183881595997117852422833109364150140133222411523124371156141223221115412751866421521171837515038914480758496142613528919471715331257353341492315540157227531486383216113159311644511162236416104142141025812835542755139202177756121126121122195234341115113222622333482125094741843112461141731144141755136335351012212703941512134734121203347111297310243521522794104521475121187723214011088212221112617952116211423276'''
#        return '''503212249273120633161030137337881186991556378112926542236855198956610110272487277350114811889207122885219962137217187541972835652872673302735385144694525510798476543011518263251325342742298995388525515537616846445342145831342432119311041698723595910317912611118181711211111151411441441817207631123125311421111491616255922124311117323711118312112011211412111131112271611624111136362135722119121212112312363211131211651'''
    elif ( lookup == '1_5'):
        return '''682156145306785237520141615361344193435661262188225180373811130171137118941749105157124574531302102637552346104951286254888957151525147240265612016551062672346261505961955452325267142083452927148117631170823216131211121124444211114712456922211437112155831111181611192151122211239632321216422448127244103937122516921411210731812112151521943318912222311713214314451008966131423261432273649608981917681171822131124141361518259591621119159243744068191244662214231111221113811614722211216421102275871421417218411313952102846658382236512514551491333241062161441459206621917463361571134413522291651921217164412171033791231837332912192521741234210912688101111285167107591132914933112131580747986503354958699293735110077919262281310434011945322510505427782856183406316121332462066411544512746538124161111358482620118170392462421121411112211114211881311021152194814122611275641073481143123024692124'''
#        return '''455192105101441326313167471351293561339109229371866466833714710824424217121294584975826111159381362370182114481781157535420228833034108117080531999135351962181501610231329825113158214111111111111211111121118104121111111116321111113353113212111153211112111111'''
    else:
        return '''abcdefghijklmnopqrstuvwxyz'''

class Constants(BaseConstants):
    name_in_url = 'transcription'
    players_per_group = 4
    num_rounds = 5
    split_chats = settings.SPLIT
#    split_chats = True
    reference_texts = {}

    reference_texts[0,0] = get_trx("1_1")
    reference_texts[0,1] = get_trx("1_2")
    reference_texts[0,2] = get_trx("1_3")
    reference_texts[0,3] = get_trx("1_4")
    reference_texts[0,4] = get_trx("1_5")

    allowed_error_rates = [3,3,3,3,3]
    startwp_timer = 600

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

    transcribed_text = models.TextField(blank=True)
    levenshtein_distance = models.PositiveIntegerField()
    emp_price = models.CurrencyField()
    man_emp1_price = models.CurrencyField()
    man_emp1_accpt = models.BooleanField()
    man_emp2_price = models.CurrencyField()
    man_emp2_accpt = models.BooleanField()
    man_emp3_price = models.CurrencyField()
    man_emp3_accpt = models.BooleanField()
    startwp_timer_set = models.BooleanField(default=False)
    startwp_time = models.PositiveIntegerField()
    outofthegame = models.BooleanField()


