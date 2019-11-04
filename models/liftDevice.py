from .component import *

class LiftDevice(Component):
	def __init__(self, area, taper_ratio, aspect_ratio, sweep, lift_curve, zero_lift):
		self.area = area
		self.taper_ratio = taper_ratio
		self.aspect_ratio = aspect_ratio
		self.sweep = sweep
		self.lift_curve = lift_curve
		self.zero_lift = zero_lift

	@property
	def mac(self):
		return c_root() * (2/3) * (1 + taper_ratio + taper_ratio ** 2)/(1 + taper_ratio)		

	# TODO
	@property	
	def c_root(self):
		pass

	@property	
	def c_tip(self):
		pass

	@property	
	def span(self):
		pass

	@property	
	def semi_span(self):
		pass

