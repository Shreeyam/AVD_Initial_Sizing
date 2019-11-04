import pint
u = pint.UnitRegistry()

class definitions:
	# Whole-aircraft definitions

	# Fuselage definitions

	# Diameter
	D = 2.55 * u.m

	# Length
	L = 28 * u.m

	# Nose length
	noseLength = 10 * u.m

	# Afterbody angle
	afterbodyAngle = 15 * u.deg

	# Wing definitions
	
	# Area
	S = 44.15 * (u.m ** 2)
	# Taper ratio
	λ = 0.3
	# AR 
	AR = 8
	# Sweep (1/4 chord defined)
	Λ = 30 * u.deg
	# Lift curve slope
	α = 0
	α_0 = 0
	# Thickness to chord ratio
	tc = 0.15

	# Flapped area
	SfS = 0.6
	# Slatted area
	SsS = 0.9
	# Extension ratio
	cbar = 1.3
	# Additional C_L
	dCl = 1.6

	# Engine definitions
	N_E = 2
	T = 31 * u.kn
	BPR = 5.7
	# Diameter
	D_E = 1.41 * u.m
	# Weight
	W_E = 606 * u.kg

	# Horizontal Stabilizer definitions
	Λ_h = 30 * u.deg
	AR_h = 8
	λ_h = 0.3
	# Volume coefficient
	C_HT = 0
	
	# Lift curve slope
	α_H = 0
	α_0H = 0

	# Vertical Stabilizer definitions
	Λ_h = 30 * u.deg
	AR_h = 3
	λ_h = 0.5
	# Volume coefficient
	C_HT = 0


	# Undercarriage definitions

	# lol


