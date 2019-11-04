from .component import *
from .afterbody import *
from .centreFuselage import *
from .engine import *
from .fuselage import *
from .horizontalStabilizer import *
from .nose import *
from .primitives import *
from .verticalStabilizer import *
from .wing import *


class Aircraft(Component):
	def __init__(self, fuselage, wing, engines, tail):

		self.fuselage = fuselage
		self.wing = wing
		self.engines = engines
		self.tail = tail


		self.TW = None
		self.MTOW = None

	def __init__(self, definition):
		# Create aircraft from definitions class

		pass
