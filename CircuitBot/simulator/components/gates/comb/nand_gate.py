__author__ = 'Zylanx'

from functools import reduce
import operator

from ..base_gates import CombinatorialGate

class NandGate(CombinatorialGate):
	def __init__(self, inputs, outputs):
		super().__init__(inputs, outputs)
		self._signalMapping["inputs"] = inputs
		self._signalMapping["outputs"] = outputs

	def combEval(self):
		inputVals = [x.curVal for x in self._signalMapping["inputs"]]
		result = ~reduce(operator.and_, inputVals)
		for outputSignal in self._signalMapping["outputs"]:
			outputSignal.nextVal = result