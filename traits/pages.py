from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.conf import settings

class MyPage(Page):
	form_model = 'player'
	form_fields = ['frndlyHstl','authPhny','nonDfDf','wrmCld','flxRgd','genStgy','hnstDcptv','indpDep','rlxTns','gdHumUnhppy','adltChld','rlstNrcsstc','sexAlvRprsd','outgngInwrd','rspflIntrsv','frAddAdd','acptJdgmntl','gdJdgImplsv','attrSlppy','assrtDny','actvPssv'] 
	def vars_for_template(self):
		return {
				'debug': settings.DEBUG,
                'who': Constants.who[self.round_number-1]
                }

class ResultsWaitPage(WaitPage):
	def is_displayed(self):
		return self.round_number == 2

	def after_all_players_arrive(self):
		pass


class Results1(Page):
	def is_displayed(self):
		return self.round_number == 2
	def vars_for_template(self):
			return {
			'v01': self.player.in_round(1).frndlyHstl,
			'v02': self.player.in_round(1).authPhny,
			'v03': self.player.in_round(1).nonDfDf,
			'v04': self.player.in_round(1).wrmCld,
			'v05': self.player.in_round(1).flxRgd,
			'v06': self.player.in_round(1).genStgy,
			'v07': self.player.in_round(1).hnstDcptv,
			'v08': self.player.in_round(1).indpDep,
			'v09': self.player.in_round(1).rlxTns,
			'v10': self.player.in_round(1).gdHumUnhppy,
			'v11': self.player.in_round(1).adltChld,
			'v12': self.player.in_round(1).rlstNrcsstc,
			'v13': self.player.in_round(1).sexAlvRprsd,
			'v14': self.player.in_round(1).outgngInwrd,
			'v15': self.player.in_round(1).rspflIntrsv,
			'v16': self.player.in_round(1).frAddAdd,
			'v17': self.player.in_round(1).acptJdgmntl,
			'v18': self.player.in_round(1).gdJdgImplsv,
			'v19': self.player.in_round(1).attrSlppy,
			'v20': self.player.in_round(1).assrtDny,
			'v21': self.player.in_round(1).actvPssv,
			'w01': self.player.get_partner().in_round(2).frndlyHstl,
			'w02': self.player.get_partner().in_round(2).authPhny,
			'w03': self.player.get_partner().in_round(2).nonDfDf,
			'w04': self.player.get_partner().in_round(2).wrmCld,
			'w05': self.player.get_partner().in_round(2).flxRgd,
			'w06': self.player.get_partner().in_round(2).genStgy,
			'w07': self.player.get_partner().in_round(2).hnstDcptv,
			'w08': self.player.get_partner().in_round(2).indpDep,
			'w09': self.player.get_partner().in_round(2).rlxTns,
			'w10': self.player.get_partner().in_round(2).gdHumUnhppy,
			'w11': self.player.get_partner().in_round(2).adltChld,
			'w12': self.player.get_partner().in_round(2).rlstNrcsstc,
			'w13': self.player.get_partner().in_round(2).sexAlvRprsd,
			'w14': self.player.get_partner().in_round(2).outgngInwrd,
			'w15': self.player.get_partner().in_round(2).rspflIntrsv,
			'w16': self.player.get_partner().in_round(2).frAddAdd,
			'w17': self.player.get_partner().in_round(2).acptJdgmntl,
			'w18': self.player.get_partner().in_round(2).gdJdgImplsv,
			'w19': self.player.get_partner().in_round(2).attrSlppy,
			'w20': self.player.get_partner().in_round(2).assrtDny,
			'w21': self.player.get_partner().in_round(2).actvPssv

			}
class Results2(Page):
	def is_displayed(self):
		return self.round_number == 2
	def vars_for_template(self):
			return {
			'v01': self.player.in_round(2).frndlyHstl,
			'v02': self.player.in_round(2).authPhny,
			'v03': self.player.in_round(2).nonDfDf,
			'v04': self.player.in_round(2).wrmCld,
			'v05': self.player.in_round(2).flxRgd,
			'v06': self.player.in_round(2).genStgy,
			'v07': self.player.in_round(2).hnstDcptv,
			'v08': self.player.in_round(2).indpDep,
			'v09': self.player.in_round(2).rlxTns,
			'v10': self.player.in_round(2).gdHumUnhppy,
			'v11': self.player.in_round(2).adltChld,
			'v12': self.player.in_round(2).rlstNrcsstc,
			'v13': self.player.in_round(2).sexAlvRprsd,
			'v14': self.player.in_round(2).outgngInwrd,
			'v15': self.player.in_round(2).rspflIntrsv,
			'v16': self.player.in_round(2).frAddAdd,
			'v17': self.player.in_round(2).acptJdgmntl,
			'v18': self.player.in_round(2).gdJdgImplsv,
			'v19': self.player.in_round(2).attrSlppy,
			'v20': self.player.in_round(2).assrtDny,
			'v21': self.player.in_round(2).actvPssv,
			'w01': self.player.get_partner().in_round(1).frndlyHstl,
			'w02': self.player.get_partner().in_round(1).authPhny,
			'w03': self.player.get_partner().in_round(1).nonDfDf,
			'w04': self.player.get_partner().in_round(1).wrmCld,
			'w05': self.player.get_partner().in_round(1).flxRgd,
			'w06': self.player.get_partner().in_round(1).genStgy,
			'w07': self.player.get_partner().in_round(1).hnstDcptv,
			'w08': self.player.get_partner().in_round(1).indpDep,
			'w09': self.player.get_partner().in_round(1).rlxTns,
			'w10': self.player.get_partner().in_round(1).gdHumUnhppy,
			'w11': self.player.get_partner().in_round(1).adltChld,
			'w12': self.player.get_partner().in_round(1).rlstNrcsstc,
			'w13': self.player.get_partner().in_round(1).sexAlvRprsd,
			'w14': self.player.get_partner().in_round(1).outgngInwrd,
			'w15': self.player.get_partner().in_round(1).rspflIntrsv,
			'w16': self.player.get_partner().in_round(1).frAddAdd,
			'w17': self.player.get_partner().in_round(1).acptJdgmntl,
			'w18': self.player.get_partner().in_round(1).gdJdgImplsv,
			'w19': self.player.get_partner().in_round(1).attrSlppy,
			'w20': self.player.get_partner().in_round(1).assrtDny,
			'w21': self.player.get_partner().in_round(1).actvPssv
			}

class Results3(Page):
	def is_displayed(self):
		return self.round_number == 2

	def vars_for_template(self):
			diff01 = (self.player.in_round(2).frndlyHstl - self.player.get_partner().in_round(1).frndlyHstl)
			diff02 = (self.player.in_round(2).authPhny - self.player.get_partner().in_round(1).authPhny)
			diff03 = (self.player.in_round(2).nonDfDf - self.player.get_partner().in_round(1).nonDfDf)
			diff04 = (self.player.in_round(2).wrmCld - self.player.get_partner().in_round(1).wrmCld)
			diff05 = (self.player.in_round(2).flxRgd - self.player.get_partner().in_round(1).flxRgd)
			diff06 = (self.player.in_round(2).genStgy - self.player.get_partner().in_round(1).genStgy)
			diff07 = (self.player.in_round(2).hnstDcptv - self.player.get_partner().in_round(1).hnstDcptv)
			diff08 = (self.player.in_round(2).indpDep - self.player.get_partner().in_round(1).indpDep)
			diff09 = (self.player.in_round(2).rlxTns - self.player.get_partner().in_round(1).rlxTns)
			diff10 = (self.player.in_round(2).gdHumUnhppy - self.player.get_partner().in_round(1).gdHumUnhppy)
			diff11 = (self.player.in_round(2).adltChld - self.player.get_partner().in_round(1).adltChld)
			diff12 = (self.player.in_round(2).rlstNrcsstc - self.player.get_partner().in_round(1).rlstNrcsstc)
			diff13 = (self.player.in_round(2).sexAlvRprsd - self.player.get_partner().in_round(1).sexAlvRprsd)
			diff14 = (self.player.in_round(2).outgngInwrd - self.player.get_partner().in_round(1).outgngInwrd)
			diff15 = (self.player.in_round(2).rspflIntrsv - self.player.get_partner().in_round(1).rspflIntrsv)
			diff16 = (self.player.in_round(2).frAddAdd - self.player.get_partner().in_round(1).frAddAdd)
			diff17 = (self.player.in_round(2).acptJdgmntl - self.player.get_partner().in_round(1).acptJdgmntl)
			diff18 = (self.player.in_round(2).gdJdgImplsv - self.player.get_partner().in_round(1).gdJdgImplsv)
			diff19 = (self.player.in_round(2).attrSlppy - self.player.get_partner().in_round(1).attrSlppy)
			diff20 = (self.player.in_round(2).assrtDny - self.player.get_partner().in_round(1).assrtDny)
			diff21 = (self.player.in_round(2).actvPssv - self.player.get_partner().in_round(1).actvPssv)

			xiff01 = (self.player.in_round(1).frndlyHstl - self.player.get_partner().in_round(2).frndlyHstl)
			xiff02 = (self.player.in_round(1).authPhny - self.player.get_partner().in_round(2).authPhny)
			xiff03 = (self.player.in_round(1).nonDfDf - self.player.get_partner().in_round(2).nonDfDf)
			xiff04 = (self.player.in_round(1).wrmCld - self.player.get_partner().in_round(2).wrmCld)
			xiff05 = (self.player.in_round(1).flxRgd - self.player.get_partner().in_round(2).flxRgd)
			xiff06 = (self.player.in_round(1).genStgy - self.player.get_partner().in_round(2).genStgy)
			xiff07 = (self.player.in_round(1).hnstDcptv - self.player.get_partner().in_round(2).hnstDcptv)
			xiff08 = (self.player.in_round(1).indpDep - self.player.get_partner().in_round(2).indpDep)
			xiff09 = (self.player.in_round(1).rlxTns - self.player.get_partner().in_round(2).rlxTns)
			xiff10 = (self.player.in_round(1).gdHumUnhppy - self.player.get_partner().in_round(2).gdHumUnhppy)
			xiff11 = (self.player.in_round(1).adltChld - self.player.get_partner().in_round(2).adltChld)
			xiff12 = (self.player.in_round(1).rlstNrcsstc - self.player.get_partner().in_round(2).rlstNrcsstc)
			xiff13 = (self.player.in_round(1).sexAlvRprsd - self.player.get_partner().in_round(2).sexAlvRprsd)
			xiff14 = (self.player.in_round(1).outgngInwrd - self.player.get_partner().in_round(2).outgngInwrd)
			xiff15 = (self.player.in_round(1).rspflIntrsv - self.player.get_partner().in_round(2).rspflIntrsv)
			xiff16 = (self.player.in_round(1).frAddAdd - self.player.get_partner().in_round(2).frAddAdd)
			xiff17 = (self.player.in_round(1).acptJdgmntl - self.player.get_partner().in_round(2).acptJdgmntl)
			xiff18 = (self.player.in_round(1).gdJdgImplsv - self.player.get_partner().in_round(2).gdJdgImplsv)
			xiff19 = (self.player.in_round(1).attrSlppy - self.player.get_partner().in_round(2).attrSlppy)
			xiff20 = (self.player.in_round(1).assrtDny - self.player.get_partner().in_round(2).assrtDny)
			xiff21 = (self.player.in_round(1).actvPssv - self.player.get_partner().in_round(2).actvPssv)

			alpha = 2
			temp = round(100 * ((336 -  ( pow(diff01,alpha) + pow(diff02,alpha) + pow(diff03,alpha) + pow(diff04,alpha) + pow(diff05,alpha) + pow(diff06,alpha) + pow(diff07,alpha) + pow(diff08,alpha) + pow(diff09,alpha) + pow(diff10,alpha) + pow(diff11,alpha) + pow(diff12,alpha) + pow(diff13,alpha) + pow(diff14,alpha) + pow(diff15,alpha) + pow(diff16,alpha) + pow(diff17,alpha) + pow(diff18,alpha) + pow(diff19,alpha) + pow(diff20,alpha) + pow(diff21,alpha)))/336))
			xemp = round(100 * ((336 -  ( pow(xiff01,alpha) + pow(xiff02,alpha) + pow(xiff03,alpha) + pow(xiff04,alpha) + pow(xiff05,alpha) + pow(xiff06,alpha) + pow(xiff07,alpha) + pow(xiff08,alpha) + pow(xiff09,alpha) + pow(xiff10,alpha) + pow(xiff11,alpha) + pow(xiff12,alpha) + pow(xiff13,alpha) + pow(xiff14,alpha) + pow(xiff15,alpha) + pow(xiff16,alpha) + pow(xiff17,alpha) + pow(xiff18,alpha) + pow(xiff19,alpha) + pow(xiff20,alpha) + pow(xiff21,alpha)))/336))

			return {
				'diff01' : diff01,
				'diff02' : diff02,
				'diff03' : diff03,
				'diff04' : diff04,
				'diff05' : diff05,
				'diff06' : diff06,
				'diff07' : diff07,
				'diff08' : diff08,
				'diff09' : diff09,
				'diff10' : diff10,
				'diff11' : diff11,
				'diff12' : diff12,
				'diff13' : diff13,
				'diff14' : diff14,
				'diff15' : diff15,
				'diff16' : diff16,
				'diff17' : diff17,
				'diff18' : diff18,
				'diff19' : diff19,
				'diff20' : diff20,
				'diff21' : diff21,
				'temp' : temp,
				'xiff01' : xiff01,
				'xiff02' : xiff02,
				'xiff03' : xiff03,
				'xiff04' : xiff04,
				'xiff05' : xiff05,
				'xiff06' : xiff06,
				'xiff07' : xiff07,
				'xiff08' : xiff08,
				'xiff09' : xiff09,
				'xiff10' : xiff10,
				'xiff11' : xiff11,
				'xiff12' : xiff12,
				'xiff13' : xiff13,
				'xiff14' : xiff14,
				'xiff15' : xiff15,
				'xiff16' : xiff16,
				'xiff17' : xiff17,
				'xiff18' : xiff18,
				'xiff19' : xiff19,
				'xiff20' : xiff20,
				'xiff21' : xiff21,
				'xemp' : xemp
			}
page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results1,
    Results2,
    Results3
]
