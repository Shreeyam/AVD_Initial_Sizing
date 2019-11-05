import pint
u = pint.UnitRegistry()

class Definitions:
	# Whole-aircraft definitions

	# Fuselage definitions

	# Diameter
	def __init__(self):
		self.D = 2.55 * u.m

		# Length
		self.L = 28 * u.m

		# Nose length
		self.noseLength = 10 * u.m

		# Afterbody angle
		self.afterbodyAngle = 15 * u.deg

		# Engine definitions
		self.N_E = 2
		self.T = 31000 * u.newton
		self.BPR = 5.7
		# Diameter
		self.D_E = 1.41 * u.m
		# Weight
		self.W_E = 606 * u.kg
		self.cj = 0.4 * u.lbf / u.lb / u.hr

		# Wing definitions
		
		# Area
		self.S = 44.15 * (u.m ** 2)
		# Taper ratio
		self.λ = 0.3
		# AR 
		self.AR = 8
		# Sweep (1/4 chord defined)
		self.Λ = 30 * u.deg
		# Lift curve slope
		self.α = 0
		self.α_0 = 0
		# Thickness to chord ratio
		self.tc = 0.15
		self.dihedral = 5 * u.deg
		self.Nz = 3

		# Flapped area
		self.SfS = 0.6
		# Slatted area
		self.SsS = 0.9
		# Extension ratio
		self.cbar = 1.3
		# Additional C_L from high lift devices
		self.dCl = 1.6
		# Horizontal Stabilizer definitions
		self.Λ_H = 30 * u.deg
		self.AR_H = 8
		self.λ_H = 0.3
		# Volume coefficient
		self.C_HT = 0
		
		# Lift curve slope
		self.α_H = 0
		self.α_0H = 0

		# Vertical Stabilizer definitions
		self.Λ_V = 30 * u.deg
		self.AR_V = 3
		self.λ_V = 0.5
		# Volume coefficient
		self.C_HV = 0
		self.α_V = 0
		self.α_0V = 0


		# Undercarriage definitions

		# lol


