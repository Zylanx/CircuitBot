__author__ = 'Zylanx'

class Signal():
	def __init__(self, val):
		self.signalName = None
		self._val = val

	@property
	def curVal(self):
		return self._val

	@property
	def nextVal(self):
		return self._val

	@nextVal.setter
	def nextVal(self, newVal):
		self._val = newVal