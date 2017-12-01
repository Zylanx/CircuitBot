__author__ = 'Zylanx'

from functools import reduce
import operator

from ..base_gates import CombinatorialGate

class NotGate(CombinatorialGate):
	def __init__(self, input, outputs):
		super().__init__(input, outputs)
		self._signalMapping["input"] = input
		self._signalMapping["outputs"] = outputs

	def combEval(self):
		inputVal = self._signalMapping["input"].curVal
		result = ~inputVal
		for outputSignal in self._signalMapping["outputs"]:
			outputSignal.nextVal = result