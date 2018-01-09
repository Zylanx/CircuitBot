__author__ = "Zylanx"

# There will be a lot of snake_case and camelCase conflicts.
# This is to do with how the library has been written.
# It uses a lot of metaprogramming and as such, certain things have
# to be done in specific ways

from sly import Lexer

# TODO: Add inferencing of structure

# TODO: Comment everything. Why do I never do this?

class CircuitBotLexer(Lexer):
	
	def __init__(self):
		self._line_start = True
		self._paren_count = 0
		
	def tokenize(self, *args, **kwargs):
		for token in super().tokenize(*args, **kwargs):
			if token.type == "NEWLINE":
				self._line_start = True
			else:
				self._line_start = False
			yield token
		
	def find_column(self, text = None, token = None):
		if not text:
			text = self.text
		if not token:
			token = self
			
		last_cr = text.rfind('\n', 0, token.index)
		if last_cr < 0:
			last_cr = 0
		column = (token.index - last_cr) + 1
		return column
	
	def _in_paren_block(self):
		if self._paren_count > 0:
			return True
	
	literals = {".", ",", ":", "=", "&", "(", ")", "{", "}"}
	
	reserved_words = {"LOAD", "CIRCUIT", "PORT", "IN", "OUT", "COMPONENTS", "WIRING"}
	tokens = {
		"IDENT",
		"NUMBER",
		"NEWLINE",
		"WS",
		#"INDENT",
		#"DEDENT",
		*reserved_words
	}
	
	@_(r"(?:_|\d)*[a-zA-Z]\w*")
	def IDENT(self, t):
		#t.type = self.reserved_words.get(t.value.upper(), "IDENT")
		if t.value.upper() in self.reserved_words:
			t.type = t.value.upper()
		return t
	
	#NUMBER = r"\d+"
	@_(r"\d+")
	def NUMBER(self, t):
		return t
	
	ignore_comment = r"\ *\#[^\n]*"
	
	@_(r"[ ]+")
	def WS(self, t):
		if self._line_start and not self._in_paren_block():
			return t
		
	@_(r"\n+")
	def NEWLINE(self, t):
		self.lineno += len(t.value)
		self._line_start = True
		return t
	
	@_(r"\(")
	def LPAREN(self, t):
		self.type = "("
		self._paren_count += 1
		return t
	
	@_(r"\)")
	def RPAREN(self, t):
		self.type = ")"
		self._paren_count -= 1
		return t
	
	def error(self, value):
		print("Illegal character '%s'" % value[0])
		self.index += 1
		
if __name__ == "__main__":
	testLexer = CircuitBotLexer()
	testData = '''
load builtin.AND.8way
load AND.8way

circuit Test1(conf, or, init, params) {
    Port:
        In:
            thing1(bitlen)
            thing2
        Out:
            out1(len)
            out2(len)

    Signals:
        thing3(bitlen) = thing1(vector:slice) & thing2(vector:slice)

    Components:
        and1 = AND.8way(conf, or, init, params)

    Wiring:
        and1(in1 = thing1, in2 = thing2, out = out1, out = out2)
        #8way(Parameters)
}'''
	
	for token in testLexer.tokenize(testData):
		print(token)