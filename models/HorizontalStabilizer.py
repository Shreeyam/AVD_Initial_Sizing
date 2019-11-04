from .liftDevice import *

class HorizontalStabilizer(LiftDevice):
	def __init__(self, taper_ratio, aspect_ratio, sweep, lift_curve, zero_lift, C_HT):
		super().__init__(0, taper_ratio, aspect_ratio, sweep, lift_curve, zero_lift)
		self.C_HT = C_HT
