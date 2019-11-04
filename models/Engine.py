from .component import *

class Engine(Component):
	def __init__(self, N_E, thrust, bypass_ratio, diameter, weight, cj):
		self.N_E = N_E
		self.thrust = thrust
		self.bypass_ratio = bypass_ratio
		self.diameter = diameter
		self.weight = weight
		self.cj = cj

	@property
	def totalThrust():
		return N_E * self.thrust 