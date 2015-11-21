from woodpecker import Woodpecker

w = Woodpecker('woodpecker.language')
tokens = w.generate_tokens()

for token in tokens:
	tk, tp = token
	import pdb; pdb.set_trace()
	print('<{}, {}>'.format(tk, tp))




