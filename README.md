#### Woodpecker Lexical Analyzer

Woodpecker is a simple lexical analyzer written in Python used to explain a lexical conventions on study of compilers.

![woodpecker image](woodpecker.png)

#### Lexical Specification

Source code


<h1 style="color:blue">This is a heading</h1>
woodpecker inicio
	variavel senha :
	variavel login :
	variavel numero :
	
	exibir_msg "Esse_ao_meu_primeiro_analisador_léxico" :
	
	para numero ate 100 faca
	{
		exibir numero :
	}

	--verificação da senha--
	senha = 1234 :			
	login = senha igual 1234 :

	se login
	{
		exibir_msg "Login_efetuado_com_suscesso" :
	}	
fim


Tabela de convenções

| Color       | Description                                          |
|-------------|------------------------------------------------------|
| Azul        | Nome da linguagem de programação – palavra reservada |
| Roxo        | Palavras reservadas                                  |
| Laranja     | Identificadores (variável ou procedimento)           |
| Verde       | Constante literal                                    |
| Azul-claro  | Constante inteira                                    |
| Vermelho    | Marcador de final de linha                           |
| Entre -- -- | Entre Comentários                                    |

#### Files

`woodpecker.language`: Source code of programming language

`woodpecker.py`: Implementation of the lexical analyzer

`test_woodpecker.py`: Unit test of the lexical analyzer
