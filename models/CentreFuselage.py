from .component import *
# Defines parameters for the main body fuselage

class CentreFuselage(Component):
	def __init__(self, length, diameter):
		self.length = length
		self.diameter = diameter
