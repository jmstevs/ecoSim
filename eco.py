from random import randint, sample
from time import sleep
import sys

def prof():
	""" docstring
		
	doctest
	"""
	
	a = [randint(1, 100) for n in range(4)]
	b = [randint(1, 100) for n in range(4)]
	score = 0

	print('\n{:>6} |{:>6} |{:>6} |{:>6} |{:>6} |{:>9}'.format('Self', 'Comp', 'Dist', 'Diff', 'Score', 'AccTotal'))
	print('{:>6} |{:>6} |{:>6} |{:>6} |{:>6} |{:>9}'.format('','','','','',''))
	
	for x, y in zip(a, b):
		abs_dif = abs(x-y)
		abs_score = abs(abs_dif-100)
		score_mult = abs_score * .25
		dif = (x-y)
		score += score_mult
		print('{:6d} |{:6d} |{:6d} |{:+6d} |{:6.2f} |{:9.2f}'.format(x, y, abs_dif, -dif, score_mult, score))
	print()


def t(runs=10, wait=.1):
	""" docstring
		
	doctest
	"""
	
	for n in range(runs):
		prof()
		sleep(wait)
		
#//////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////

class BANK:
	""" the artificial adversary for the populous
	
	doctest code
	"""
	class IDGEN:
		""" Iterator object to give out ID numbers to newly registered
		civilians.
		
		doctest code
		"""
		def __init__(self):
			self.num = 0
		def __iter__(self):
			return self 
		def __next__(self):
			self.num += 1
			return self.num 
			
	def __init__(self):
		""" docstring
		
		doctest
		"""
	
		# a dictionary containing all the tracking information of the Civilians
		self.archives = {}	
		
		self.items = {}
		self.id_generator = IDGEN()
		self.registered_civilians = {}
		
#---------------------------------------------------------------------------------

	def registerCivilian(self):
		""" docstring
			
		doctest
		"""
		id = str(next(self.id_generator))
		
		while id in self.registered_civilians:
			id = str(next(self.id_generator))
			
		self.registered_civilians[id] = CIV(id)
		

#/////////////////////////////////////////////////////////////////////////////////
		
class CIV:
	""" docstring
		
	doctest
	"""
	
	def __init__(self, id):
		""" docstring
			
		doctest
		"""
		
		self.id = id
		self.profile = [randint(1, 100) for n in range(4)]
		
		self.current_mult = 1
		self.base_credits = 1000
		self.credits = self.current_mult * self.base_credits
		
		self.items = []			# will hold ITEM instances
		self.history = \
		{
		'date & time stamp': '...history information...'
		}
		
#----------------------------------------------------------------------------------
	def civCompare(self, bank, *civ_ids):
		pass
		
#----------------------------------------------------------------------------------
	def manageItems(self):
		pass
		
#----------------------------------------------------------------------------------
	def valueCalc(self):
		""" docstring
			
		doctest
		"""

		from statistics import mean
		if self.items:
			
			# list of scores, to be averaged
			mult_list = []
			
			# for block start, enum for index later
			for enum, item in zip(range(len(self.items)), self.items):
				
				# append next score to list
				mult_list.append(0)
				
				# zipped profiles
				for self_prof, item_prof in zip(self.profile, item.profile):
					
					# calc 'distance'
					abs_dif = abs(self_prof-item_prof)
					
					# calc score: 'dist' - max 'dist'
					abs_score = abs(abs_dif-100)
					
					# give scale 25% weight
					score_mult = abs_score * .25
					
					# significant later for profile changing
					dif = -(self_prof-item_prof)
					mult_list[enum] += score_mult
					
			self.current_mult = (mean(mult_list)/100) + 1
			self.credits = self.base_credits * self.current_mult 
			
		else:
			print('...you\'ve got no items.') 
		return

#----------------------------------------------------------------------------------
	def __call__(self):
		""" docstring
			
		doctest
		"""

		info = [self.id,
				self.profile,
				self.current_mult,
				self.base_credits,
				self.credits,
				(len(self.items), self.items),
				(len(self.history), self.history,)]
		
		return info

#///////////////////////////////////////////////////////////////////////////////////

class ITEM:
	""" docstring
		
	doctest
	"""

	
	def __init__(self):
		""" docstring
			
		doctest
		"""

		self.profile = [randint(1, 100) for n in range(4)]
		return
		
#///////////////////////////////////////////////////////////////////////////////////

class PLAY:
	
	def __init__(self):
		""" docstring
			
		doctest
		"""

		self.profile = [randint(1, 100) for n in range(4)]
		return 

#///////////////////////////////////////////////////////////////////////////////////	
	
class WORK:
	"""Acts as the main producer of items. Employs
	CIVs
	
	doctest
	"""
	
	def __init__(self, owner, registration):
		""" docstring
			
		doctest
		"""

		inception_profile = owner.profile
		profile_range_mod = sample(range(-15, 16), len(owner.profile))
		self.profile = []
		for el in range(len(owner.profile)):
			self.profile[el] = owner.profile - profile_range_mod[el]
		return
#-----------------------------------------------------------------------------------
	def produce(self, grade=1):
		""" docstring
			
		doctest
		"""

		if grade == 1:
			self.poduction_width = 5
			self.production_time = 10		# server actions instead of time
		return
		
#///////////////////////////////////////////////////////////////////////////////////