__author__ = 'Zylanx'

from functools import reduce
import operator

from ..base_gates import CombinatorialGate

class XorGate(CombinatorialGate):
	def __init__(self, inputs, outputs):
		super().__init__(inputs, outputs)
		self._signalMapping["inputs"] = inputs
		self._signalMapping["outputs"] = outputs

	def combEval(self):
		inputVals = [x.curVal for x in self._signalMapping["inputs"]]
		result = (sum(inputVals) % 2) == 0
		for outputSignal in self._signalMapping["outputs"]:
			outputSignal.nextVal = result