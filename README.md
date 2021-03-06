#### Woodpecker Lexical Analyzer

Woodpecker is a simple lexical analyzer written in Python used to explain a lexical convention on the study of compilers.

<center>![woodpecker image](woodpecker.png)</center>

#### Lexical Specification

Source code

![source code](woodpecker.language.png)

Conventions table

| Color   | Description                                                        |
|---------|--------------------------------------------------------------------|
| Blue    | Names of languages – keyword                                       |
| Purple  | Keyword                                                            |
| Orange  | Identifier - procedure starts with a lowercase or uppercase letter |
| Cyan    | Identifier - variable starts with a lowercase or uppercase letter  |
| Green   | String                                                             |
| Brown   | Integer                                                            |
| Lime    | Float                                                              |
| ------- | Between -- -- is a comment                                         |
| ------- | Left curly bracket - { - start block code                          |
| ------- | Right curly bracket - } - end block code                           |
| ------- | Colon - : - end <keyword> Statement                                |
| ------- | Equal - = - variable assignment statements                         |

#### How to use

Run example

`python example.py`

Run tests

`python test_woodpecker.py`

#### Files

`woodpecker.language`: Source code of programming language.

`woodpecker.py`: Implementation of the lexical analysis(scanning).

`test_woodpecker.py`: Unit test of the lexical specification.
