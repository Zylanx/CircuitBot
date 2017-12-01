__author__ = 'Zylanx'

from functools import wraps

class BaseGate():
	""" TODO: Write description """

	def __init__(self, inputs, outputs):
		""" TODO: Write description"""
		#self._signalMangledNames = []

		# TODO: (BaseGate) Signal lists/dictionaries
		# Differentiate between signals that should trigger an update from ones that should not
		# as well as possibly between different types of signals (Combinatorial from sequential, or synchronous from asynchronous)
		# This could be implemented in the derived classes for finer control
		self._signalInputs = inputs
		self._signalOutputs = outputs
		#self._signalCombInputs = inputs
		#self._signalSeqInputs = []
		#self._signalCombOutputs = outputs
		#self._signalSeqOutputs = []
		self._signalMapping = {}

		self._dirty = False

	def checkInputsChanged(self):
		for inputSignal in self._signalInputs:
			if inputSignal.changed:
				self._dirty = True
				return True

	def updateTick(self):
		""" TODO: Write description """
		if self.checkInputsChanged():
			self.combEval()
		self.seqEval()

	def updateSubTick(self):
		""" TODO: Write description """
		if self.checkInputsChanged():
			self.combEval()

	def combEval(self):
		""" TODO: Write description """
		pass

	def seqEval(self):
		""" TODO: Write description """
		pass

# Base classes for identifying gate type
class CombinatorialGate(BaseGate):
	""" TODO: Write description """
	pass

class SequentialGate(BaseGate):
	""" TODO: Write description """
	pass