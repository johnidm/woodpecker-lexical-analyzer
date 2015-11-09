import re

# http://blog.ostermiller.org/find-comment

class Woodpecker():

	def __init__(self, filename):
		self.source_code = self.__read_content_file(filename)
		
	def __read_content_file(self, filename):
		with open(filename) as f:
			code = f.read()

		return code

	def code(self):		
		return self.source_code

	def remove_multiple_spaces(self):	
		self.source_code = re.sub(' +', ' ', self.source_code)
		return self

	def remove_empty_lines(self):
		self.source_code = re.sub('\t|\n|\r', ' ', self.source_code)
		return self

	def remove_comment(self):
		self.source_code = re.sub('--.*?--', ' ', self.source_code).strip()
		return self

	def tokens(self):
		tokens = re.split('[ #, #]+', self.source_code) 
		print re.findall(r'#[^#]*#|\S+', 'mark bill #special# #special method# johni')

		for token in tokens:
			print('<{}, {}>'.format(token, 'type'))		


