__author__ = 'Zylanx'

from functools import reduce
import operator

from ....base_gates import SequentialGate

class DFlipFlop(SequentialGate):
	def __init__(self, inputs, outputs):
		super().__init__(inputs, outputs)
		self._signalMapping["inputs"] = inputs
		self._signalMapping["outputs"] = outputs
		self._signalMapping["d"] = inputs[0]

	def seqEval(self):
		# TODO: Possibly make it only do it if the data line was changed
		#    Hopefully in a better way than just checking if d == out
		result = self._signalMapping["d"].curVal
		for outputSignal in self._signalMapping["outputs"]:
			outputSignal.nextVal = result