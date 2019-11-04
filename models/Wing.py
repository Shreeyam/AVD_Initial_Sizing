from .liftDevice import *

class Wing(LiftDevice):
	def __init__(self, area, taper_ratio, aspect_ratio, sweep, lift_curve, zero_lift, dihedral):
		super().__init__(area, taper_ratio, aspect_ratio, sweep, lift_curve, zero_lift)
		self.dihedral = dihedral

