from .liftDevice import *

class Wing(LiftDevice):
	def __init__(self, area, taper_ratio, aspect_ratio, sweep, lift_curve, zero_lift, dihedral, ultimate_load_factor):
		super().__init__(area, taper_ratio, aspect_ratio, sweep, lift_curve, zero_lift)
		self.dihedral = dihedral
		self.limit_load_factor = limit_load_factor

