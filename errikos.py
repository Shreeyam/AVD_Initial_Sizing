from models.aircraft import *
import numpy as np
import pint

u = pint.UnitRegistry()

class WeightEstimator:
	def __init__():
		pass

	# Return weight, and centre of mass
	def CalculateWeights(W_0, aircraft):
		# First, get terms how Errikos likes
		self.W_dg = W_0.to('lb').magnitude

		pass

	def DefineTerms(aircraft):

		# Directory of all terms

		self.AR = aircraft.Wing.aspect_ratio
		self.AR_H = aircraft.HorizontalStabilizer.aspect_ratio
		self.AR_V = aircraft.VerticalStabilizer.aspect_ratio
		
		self.A_fc = 0 		# TODO Cargo hold floor area

		self.B_ht = 0		# Horizontal tailplane span
		self.B_w = 0			# Wingspan

		self.D = aircaft.Fuselage.CentreFuselage.diameter.to('ft').magnitude
		self.F_w = 0			# TODO: Fuselage width at horizontal tail intersection?
		self.H_tH_v = 1.0	# T-tail -> 1.0
		self.I_y	= 0			# Pitching moment of inertia

		# Random ass K terms
		self.K_door = 1.06	# One side cargo door -> 1.06
		self.K_lav = 0.31	# Short haul aircraft -> 0.31
		self.K_Lg = 1.0		# Wing mounted gear -> 1.0
		self.K_mp = 1.0		# Non-kneeling main gear -> 10			 	
		self.K_ng = 1.017	# Pylon mounted nacelle -> 1.017
		self.K_np = 1.0		# Non-kneeling noise gear -> 1.0
		self.K_r = 1.0		# Non-reciprocating engines -> 1.0
		self.K_tp = 1.0		# Not a turboprop -> 1.0
		self.K_uht = 1.0		# Rudder, not all moving -> 1.0

		self.L_a	= 0			# TODO: Generators to avionics to cockpit
		self.L_ec = 0		# TODO: Engine to cockpit distance, total
		self.Lf = aircraft.Fuselage.total_length.to('ft').magnitude
		self.L = Lf			# TODO: Find the difference?
		self.L_ht = 0		# TODO
		self.L_m = 0			# TODO: Main gear distance
		self.L_n = 0			# TODO: Nose gear distance
		self.L_vt = 0		# TODO: Aerodynamic centre to horizontal tailplane aerodynamic centre

		self.N_c = 4			# Number of crew -> 
		self.N_en = 2		# Number of engines -> 2

		self.N_f	= 4			# Number of functions performed by controls -> [4, 7]
		self.N_gear = 2.7	# Ratio of applied load to landing weight [2.7, 3]
		self.N_gen = N_en	# Number of generators
		self.N_l = 1.5 * N_gear
		self.N_Lt = 0		# TODO: Nacelle length
		self.N_m = 0			# Number of mechanical functions performed by controls
		self.N_mss = 2		# Number of main gear shock struts TODO: Find a good answer
		self.N_mw = 4		# Number of main wheels
		self.N_nw = 2		# Number of nose wheels
		self.N_p = 54		# N_crew, passengers
		self.N_seat = 50		# Number of seats
		self.N_t = 3			# TODO: Number of fuel tanks
		self.N_w	= 0			# TODO: Nacelle width
		self.N_z = 			# Ultimate load factor
		self.R_kva = 40		# Electrical rating
		self.S_cs = 0		# TODO: Total control surface area
		self.S_csw = 0		# TODO: Area of wing mounted control surfaces
		self.S_e	= 0			# TODO: Elevator area
		self.S_f = 0			# TODO: Fuselage wetted area
		self.S_ht = 0		# TODO: Horizontal stabilizer area
		self.S_n	= 0			# TODO: Nacelle wetted area
		self.S_w = aircraft.Wing.area
		self.S_vt = aircraft.VerticalStabilizer.area

		self.tc_root = aircraft.Wing.tc
		self.tc_rootv = aircraft.HorizontalStabilizer.tc

		self.Vi = 0			# TODO: Fuel tank volume
		self.V_p	= 0			# TODO: Self sealing tank volume?
		self.V_s	= 0			# TODO: Landing stall weight
		self.V_t	= 0			# TODO: Total fuel tanks volume

		self.W_apu = 0		# TODO: Uninstalled APU weight
		self.W_c = 0			# TODO: Maximum cargo weight

		self.W_en = aircraft.Engine.weight

		self.W_enc = 0		# TODO: Weight of engine and contents
		self.W_l = 0			# TODO: Landing gross weight
	
		self.W_seat = 32		# TODO: Weight of a single seat [lb]
		self.W_uav = 800		# TODO: Uninstalled gross avionics weight [lb]

		self.taper_ratio = 0.3
		self.sweep = 30
		self.sweep_HT = 30
		self.sweep_VT = 30

		# Dependent terms
		self.K_ws = 0 		# TODO
		self.K_y = 0
		self.K_z = 0



	def CalculateWingWeight():
		return 0.0051 * (
			((self.W_dg * self.N_z) ** 0.557) * (self.S_w ** 0.649) * (self.AR ** 0.5) * ((1 + self.taper_ratio) ** 0.1) * (self.S_csw ** 0.1)
		)/(
			np.cos(np.deg2rad(self.sweep)) * self.tc_root
		) * u.lb
		 
	def CalculateHorizontalStabilizerWeight():
		raise NotImplementedError()

	def CalculateVerticalStabilizerWeight():
		raise NotImplementedError()

	def CalculateFuselageWeight():
		raise NotImplementedError()

	def CalculateMainGearWeight():
		raise NotImplementedError()

	def CalculateNoseGearWeight():
		raise NotImplementedError()

	def CalculateNacelleWeight():
		raise NotImplementedError()

	def CalculateEngineControlWeight():
		raise NotImplementedError()

	def CalculateEngineStarterWeight():
		raise NotImplementedError()

	def CalculateFuelSystemWeight():
		raise NotImplementedError()

	def CalculateFlightControlsWeight():
		raise NotImplementedError()

	def CalculateAPUWeight():
		raise NotImplementedError()

	def CalculateInstrumentsWeight():
		raise NotImplementedError()

	def CalculateHydraulicsWeight():
		raise NotImplementedError()

	def CalculateElectricalWeight():
		raise NotImplementedError()

	def CalculateAvionicsWeight():
		raise NotImplementedError()

	def CalculateFurnishingsWeight():
		raise NotImplementedError()

	def CalculateAirconWeight():
		raise NotImplementedError()

	def CalculateAntiIceWeight():
		return 0.002 * self.W_dg

	def CalculateHandlingGearWeight():
		return 0.0003 * self.W_dg
