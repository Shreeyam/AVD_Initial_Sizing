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
		W_dg = W_0.to('lb').magnitude
		
		pass

	def CalculateCentreOfMass():
		pass


	def CalculateWingWeight():
		return 0.0051 * (
			((self.W_dg * self.N_z) ** 0.557) * (self.S_w ** 0.649) * (self.AR ** 0.5) * ((1 + self.taper_ratio) ** 0.1) * (self.S_csw ** 0.1)
		)/(
			np.cos(np.deg2rad(self.sweep)) * self.tc_root
		) * 
		 
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
