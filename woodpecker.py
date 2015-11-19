import re


class TokenUnrecognized(Exception):
    pass


class Woodpecker():

    def __init__(self, filename):
        self.source_code = self.read_content_file(filename)

    def code(self):
        return self.source_code

    def tokens(self):

        tokens = self.__generate_token()

        for token in tokens:
            t, tp = token
            print('<{}, {}>'.format(t, tp), end=' ')

    def read_content_file(self, filename):

        with open(filename) as f:
            content = f.read()

        return content

    def remove_multiple_spaces(self):
        DOUBLE_SPACE = ' +'

        self.source_code = re.sub(DOUBLE_SPACE, ' ', self.source_code)
        return self.source_code.strip()

    def remove_empty_lines(self):
        EMPTY_LINES = '\t|\n|\r'

        self.source_code = re.sub(EMPTY_LINES, ' ', self.source_code)

        return self.source_code

    def remove_comment(self):
        COMMENT = '--.*?--'

        self.source_code = re.sub(COMMENT, ' ', self.source_code).strip()
        return self.source_code

    def get_type_token(self, token):

        IDT_END_LINE = ":"
        IDT_START_BLOCK = "{"
        IDT_END_BLOCK = "}"
        ASSIGNMENT = "="

        def is_integer(s):
            return re.match("^[-+]?\d+$", s) is not None

        def is_float(s):
            return re.match("^[-+]?\d+\.\d+?$", s) is not None

        def is_identifier(s):
            return re.match("^[A-Za-z](\w+)[A-Za-z0-9]$", s) is not None

        KEYWORD = ['woodpecker', 'inicio', 'variavel',
                   'para', 'ate', 'faca', 'igual', 'se', 'fim']

        if token in KEYWORD:
            return 'keyword'
        elif token[0] == "#" and token[-1] == "#":
            return 'string'
        elif is_integer(token):
            return 'integer'
        elif is_float(token):
            return 'float'
        elif token == IDT_END_LINE:
            return 'idt-end-line'
        elif token == IDT_START_BLOCK:
            return 'idt-start-block'
        elif token == IDT_END_BLOCK:
            return 'idt-end-block'
        elif token == ASSIGNMENT:
            return 'assignment'
        elif is_identifier(token):
            return 'idt'
        else:
            raise TokenUnrecognized('Token "{}" unrecognized'.format(token))

    def generate_token(self):

        self.remove_comment()
        self.remove_empty_lines()
        self.remove_multiple_spaces()

        list_tokens = re.findall('#[^#]*#|\S+', self.source_code)

        tokens = []
        for t in list_tokens:
            type_token = self.get_type_token(t)
            tokens.append((t, type_token))

        return tokens
