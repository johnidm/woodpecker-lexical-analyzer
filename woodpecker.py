import re

class Woodpecker():

    def __init__(self, filename):
        self.source_code = self.__read_content_file(filename)
        
    def code(self):     
        return self.source_code

    def tokens(self):

        tokens = self.__generate_token()

        for token in tokens:
            t, tp = token
            print('<{}, {}>'.format(t, tp), end=' ')

    def __read_content_file(self, filename):
        with open(filename) as f:
            content = f.read()

        return content

    def __remove_multiple_spaces(self): 
        DOUBLE_SPACE = ' +'

        self.source_code = re.sub(DOUBLE_SPACE, ' ', self.source_code)
        return self.source_code

    def __remove_empty_lines(self):
        EMPTY_LINES = '\t|\n|\r'

        self.source_code = re.sub(EMPTY_LINES, ' ', self.source_code)
        return self.source_code

    def __remove_comment(self):
        COMMENT = '--.*?--'
        
        self.source_code = re.sub(COMMENT, ' ', self.source_code).strip()
        return self.source_code

    def __get_type_token(self, token):

        def is_integer(s):
            return re.match("[-+]?\d+$", s) is not None

        def is_float(s):
            return re.match("[-+]?\d+\.\d+?$", s) is not None
        
        KEYWORD = ['woodpecker', 'inicio', 'variavel', 'para', 'ate', 'faca', 'igual', 'se', 'fim']
        
        if token in KEYWORD:
            return 'keyword'
        elif token[0] == "#" and token[-1] == "#":
            return 'string'
        elif is_integer(token):
            return 'integer'
        elif is_float(token):
            return 'float'
        else:
            return 'idt'

    def __generate_token(self):

        self.__remove_comment()
        self.__remove_empty_lines()
        self.__remove_multiple_spaces()

        list_tokens = re.findall('#[^#]*#|\S+', self.source_code)

        tokens = []
        for t in list_tokens:
            type_token = self.__get_type_token(t)
            tokens.append( (t, type_token) ) 

        return tokens




