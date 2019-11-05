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

import numpy as np

class Aircraft(Component):
	def __init__(self, fuselage, wing, engines, tail):

		self.fuselage = fuselage
		self.wing = wing
		self.engines = engines
		self.tail = tail


		self.TW = None
		self.MTOW = None

	def __init__(self, defs):
		# Create aircraft from definitions class

		# Instance fuselage
		afterbodyLength = defs.D / np.tan(defs.afterbodyAngle)

		self.Fuselage = Fuselage(
			CentreFuselage(
				defs.L - afterbodyLength - defs.noseLength,
				defs.D
			),
			Afterbody(
				afterbodyLength,
				defs.D
			),
			Nose(
				defs.noseLength,
				defs.D
			)
		)


		# Instance engine
		self.Engine = Engine(
			defs.N_E,
			defs.T,
			defs.BPR,
			defs.D_E,
			defs.W_E,
			defs.cj
		)

		# Instance wing
		self.Wing = Wing(
			defs.S,
			defs.λ,
			defs.AR,
			defs.Λ,
			defs.α,
			defs.α_0,
			defs.dihedral,
			defs.N_z
		)

		# Instance horizontal stabilizer

		self.HorizontalStabilizer = HorizontalStabilizer(
			defs.λ_H,
			defs.AR_H,
			defs.Λ_H,
			defs.α_H,
			defs.α_0H,
			defs.C_HT
		)

		# Instance vertical stabilizer
		self.VerticalStabilizer = VerticalStabilizer(
			defs.λ_V,
			defs.AR_V,
			defs.Λ_V,
			defs.α_V,
			defs.α_0V,
			defs.C_HV
		)


