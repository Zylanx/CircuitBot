__author__ = 'Zylanx'

from functools import reduce
import operator

from ....base_gates import SequentialGate

class JKFlipFlop(SequentialGate):
	def __init__(self, inputs, outputs):
		super().__init__(inputs, outputs)
		self._signalMapping["inputs"] = inputs
		self._signalMapping["outputs"] = outputs
		
		self._outputBuffer = 0

	def seqEval(self):
		# TODO: Possibly make it only do it if the data line was changed
		#    Hopefully in a better way than just checking if d == out
		jVal = self._signalMapping["j"].curVal
		kVal = self._signalMapping["k"].curVal
		
		if jVal & kVal:
			self._outputBuffer = ~self._outputBuffer
		elif jVal:
			self._outputBuffer = True
		elif kVal:
			self._outputBuffer = False
			
		for outputSignal in self._signalMapping["outputs"]:
			outputSignal.nextVal = self._outputBuffer