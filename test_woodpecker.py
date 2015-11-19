import unittest

from unittest.mock import patch
from woodpecker import Woodpecker
from woodpecker import TokenUnrecognized


class AssertMixin():

    def assertCountTokenType(self, tokens, token_type, expected):
        """

        """
        filtered = list(filter(lambda t: t[1] == token_type, tokens))
        count = len(filtered)

        self.assertEquals(count, expected)


class TestWoodpecker(unittest.TestCase, AssertMixin):

    def setUp(self):
        pass

    def __f(self):
        """ Factory a object Woodpecker """
        return Woodpecker('**file**')

    def __asrt(self, token, type):
        type_token = self.__f().get_type_token(token)
        self.assertEquals(type_token, type)

    def __should_be(self, actual, expected, func, mock):
        """
        Make a return of the function Woodpecker.read_content_file
        Called a func pass by parameter
        """
        mock.return_value = actual
        code = getattr(self.__f(), func)()
        self.assertEquals(code, expected)

    def __to_be(self, expected, value):
        type_token = self.__f().get_type_token(value)
        self.assertEquals(type_token, expected)

    @patch("woodpecker.Woodpecker.read_content_file")
    def test_remove_multiple_spaces(self, mock):

        self.__should_be("  Your code   is   bad    ",
                         "Your code is bad", "remove_multiple_spaces", mock)
        self.__should_be(
            " A bug in my       code", "A bug in my code", "remove_multiple_spaces", mock)
        self.__should_be(
            "Rewrite    a   bad code", "Rewrite a bad code", "remove_multiple_spaces", mock)

    @patch("woodpecker.Woodpecker.read_content_file")
    def test_remove_empty_lines(self, mock):
        code = "Code review?\t\n\tAin't nobody\n\n\ngot time\rfor that\r\n\n."
        self.__should_be(
            code, "Code review?   Ain't nobody   got time for that   .", "remove_empty_lines", mock)

    @patch("woodpecker.Woodpecker.read_content_file")
    def test_remove_comment(self, mock):
        self.__should_be("--Pushed new code--", "", "remove_comment", mock)
        self.__should_be("-- Wall of code --", "", "remove_comment", mock)

        self.__should_be("-- That source code -- So hot rigth now",
                         "So hot rigth now", "remove_comment", mock)

    @patch("woodpecker.Woodpecker.read_content_file")
    def test_get_type_token(self, mock):
        """ Check token type 'integer' """
        self.__to_be("integer", "0")
        self.__to_be("integer", "101")
        self.__to_be("integer", "-001")
        self.__to_be("integer", "+121")

        """ Check token type 'float' """
        # self.__to_be("float", "+21.")
        self.__to_be("float", "-0.1")
        self.__to_be("float", "+23.1")
        self.__to_be("float", "120.11")

        """ Check token type 'string' """
        self.__to_be("string", "# My code works #")
        self.__to_be("string", "#Copy paste#")

        """ Check token type 'keyword' """
        self.__to_be("keyword", "woodpecker")
        self.__to_be("keyword", "inicio")
        self.__to_be("keyword", "variavel")
        self.__to_be("keyword", "para")
        self.__to_be("keyword", "ate")
        self.__to_be("keyword", "faca")
        self.__to_be("keyword", "igual")
        self.__to_be("keyword", "se")
        self.__to_be("keyword", "fim")

        """ Check token type 'identifiers' """
        self.__to_be("idt", "split")
        self.__to_be("idt", "print")
        self.__to_be("idt", "calc")
        self.__to_be("idt", "sum")

    @patch("woodpecker.Woodpecker.read_content_file")
    def test_generate_token(self, mock):
        source_code = """

        -- Sign in with your ID --
        woodpecker inicio
            variavel senha :
            variavel numero :

            imprimir #Esse é o meu primeiro analisador léxico# :

            para numero ate 100 faca :
            {
                exibir numero :
            }

            --check the password--
            senha = 1234 :

            saldo = -23.32 :

            se senha igual 1234 :
            {
                exibir #Login efetuado com suscesso# :
            }
        fim

        """
        mock.return_value = source_code

        tokens = self.__f().generate_token()

        self.assertCountTokenType(tokens, 'integer', 3)
        self.assertCountTokenType(tokens, 'float', 1)
        self.assertCountTokenType(tokens, 'string', 2)
        self.assertCountTokenType(tokens, 'keyword', 10)
        self.assertCountTokenType(tokens, 'idt', 10)
        self.assertCountTokenType(tokens, 'idt-end-line', 9)
        self.assertCountTokenType(tokens, 'idt-start-block', 2)
        self.assertCountTokenType(tokens, 'idt-end-block', 2)
        self.assertCountTokenType(tokens, 'assignment', 2)

    @patch("woodpecker.Woodpecker.read_content_file")
    def test_regex_type_token_integer(self, mock):

        def asrt(number):
            self.__asrt(number, 'integer')

        asrt('0')
        asrt('-10')
        asrt('+10')
        asrt('10')
        self.assertRaises(TokenUnrecognized, lambda: asrt('13a'))

    @patch("woodpecker.Woodpecker.read_content_file")
    def test_regex_type_token_float(self, mock):

        def asrt(float):
            self.__asrt(float, 'float')

        asrt('0.0')
        asrt('+10.0')
        asrt('-10.0')
        asrt('10.0')
        asrt('10.10')
        asrt('10.10')
        asrt('0.10')
        self.assertRaises(TokenUnrecognized, lambda: asrt('1.22E'))
        self.assertRaises(TokenUnrecognized, lambda: asrt('13a.22'))

    @patch("woodpecker.Woodpecker.read_content_file")
    def test_regex_type_token_idenifier(self, mock):

        def asrt(idt):
            self.__asrt(idt, 'idt')

        asrt('count')
        asrt('c123')
        asrt('c123c')
        asrt('count')
        asrt('Count')
        asrt('cOUNT')

        self.assertRaises(TokenUnrecognized, lambda: asrt('1count'))
        self.assertRaises(TokenUnrecognized, lambda: asrt('_count'))
        self.assertRaises(TokenUnrecognized, lambda: asrt('#count'))
        self.assertRaises(TokenUnrecognized, lambda: asrt(' count'))
        self.assertRaises(TokenUnrecognized, lambda: asrt('!'))
        self.assertRaises(TokenUnrecognized, lambda: asrt('.'))
        self.assertRaises(TokenUnrecognized, lambda: asrt(';'))

if __name__ == "__main__":
    unittest.main()
