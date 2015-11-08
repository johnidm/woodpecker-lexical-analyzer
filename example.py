from woodpecker import Woodpecker

w = Woodpecker('woodpecker.language') \
	.remove_empty_lines() \
	.remove_comment() \
	.remove_multiple_spaces()

print(w.tokens())
