from .component import *

# Fuselage consists of three sections: Nose, CentreFuselage, Afterbody.

class Fuselage(Component):
	def __init__(self, centreFuselage, afterbody, nose, total_length):

		self.centreFuselage = centreFuselage
		self.afterbody = afterbody
		self.nose = nose
		self.total_length = total_length
