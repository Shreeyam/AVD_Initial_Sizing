from models.aircraft import *

class WeightEstimator:
	def __init__():
		pass

	def CalculateWingWeight(W_0, wing):
		# Get terms how Errikos likes
		Wdg = W_0.to('lb').magnitude
		# N_z =
		 
	def CalculateHorizontalStabilizerWeight(W_0, hstab):
		raise NotImplementedError()

	def CalculateVerticalStabilizerWeight(W_0, hstab):
		raise NotImplementedError()

	def CalculateFuselageWeight(W_0, fuselage):
		raise NotImplementedError()

	def CalculateMainGearWeight(W_0, gear):
		raise NotImplementedError()

	def CalculateNoseGearWeight(W_0, gear):
		raise NotImplementedError()

	def CalculateNacelleWeight(W_0, nacelle):
		raise NotImplementedError()

	def CalculateEngineControlWeight(W_0, engineControl):
		raise NotImplementedError()

	def CalculateEngineStarterWeight(W_0, engineStarter):
		raise NotImplementedError()

	def CalculateFuelSystemWeight(W_0, fuelsys):
		raise NotImplementedError()

	def CalculateFlightControlsWeight(W_0, controls):
		raise NotImplementedError()

	def CalculateAPUWeight(W_0, apu):
		raise NotImplementedError()

	def CalculateInstrumentsWeight(W_0, instruments):
		raise NotImplementedError()

	def CalculateHydraulicsWeight(W_0, hydraulics):
		raise NotImplementedError()

	def CalculateElectricalWeight(W_0, electrical):
		raise NotImplementedError()

	def CalculateAvionicsWeight(W_0, avionics):
		raise NotImplementedError()

	def CalculateFurnishingsWeight(W_0, furnishings):
		raise NotImplementedError()

	def CalculateAirconWeight(W_0, aircon):
		raise NotImplementedError()

	def CalculateAntiIceWeight(W_0):
		return 0.002 * W_0

	def CalculateHandlingGearWeight(W_0):
		return 0.0003 * W_0
