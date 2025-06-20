# Chapter 02 - Variables and Simple Data Types

## **Resumo – Capítulo 2: Variáveis e Tipos de Dados Simples**

Este capítulo mergulha nos fundamentos da manipulação de dados em Python, mostrando como trabalhar com variáveis, strings, números, comentários e boas práticas de código.

A primeira lição é sobre **variáveis**: no Python, elas funcionam como rótulos que apontam para valores. Para criar uma variável, basta escolher um nome (sempre seguindo as convenções de nomes com letras minúsculas e underscores), usar o operador `=`, e atribuir um valor — normalmente começando por strings, como em `message = "Hello Python world!"`. A linguagem não exige declaração prévia do tipo da variável (como ocorre em JavaScript quando se usa `let`, `const` ou `var`). Os nomes de variáveis precisam ser claros, não podem começar com números, não podem conter espaços e não devem colidir com palavras reservadas do Python (por exemplo, nunca use `print` como nome de variável).

O capítulo reforça a importância de **corrigir erros de digitação** e ensina a ler o *traceback* (mensagem de erro que Python mostra ao executar um código com erro), pois o Python sinaliza claramente quando uma variável não foi definida ou escrita corretamente.

Sobre **strings**, o capítulo apresenta as principais formas de manipulação: usar aspas simples ou duplas para delimitar texto, aplicar métodos como `.title()`, `.upper()`, `.lower()` para formatar o texto, e criar mensagens dinâmicas usando f-strings (prefixando a string com `f` e usando chaves `{}` para interpolar variáveis, como em `f"Olá, {nome}!"`). É explicado que o uso correto de aspas evita erros de sintaxe, especialmente quando o texto contém apóstrofes.

O capítulo ensina também a **trabalhar com espaços em branco** em strings — tanto para adicionar (usando `\t` para tabulação e `\n` para quebra de linha) quanto para remover (usando os métodos `.strip()`, `.rstrip()`, `.lstrip()` para limpar espaços em excesso no início, fim ou ambos os lados da string). Além disso, apresenta os métodos `removeprefix()` e `removesuffix()`, que são úteis para tratar strings como URLs ou nomes de arquivos.

Em **números**, o Python lida com inteiros e floats de forma transparente. Operadores matemáticos básicos funcionam como esperado (`+`, `-`, `*`, `/`), com a diferença que divisões sempre retornam float. O operador de potência é `**` (por exemplo, `3 ** 2`). Python aceita underscores para facilitar a leitura de números grandes (`universe_age = 14_000_000_000`), que são ignorados na execução.

O capítulo mostra ainda que é possível **atribuir valores a múltiplas variáveis em uma única linha** (`x, y, z = 0, 0, 0`) e que, por convenção, nomes em letras maiúsculas representam constantes (`MAX_CONNECTIONS = 5000`), ainda que Python não impeça que elas sejam alteradas.

Em relação a **comentários**, usa-se o símbolo `#` para escrever explicações ou anotações no código, facilitando a leitura futura ou o trabalho colaborativo. Comentários devem ser claros, explicar decisões de implementação ou detalhar partes mais complexas do código.

O capítulo encerra apresentando o "Zen of Python", conjunto de princípios que norteia a comunidade Python, incentivando a busca por soluções simples, legíveis e elegantes.

---

## **Notas rápidas para quem vem do JavaScript/TypeScript**

* **Variáveis:** Python não usa `let`, `const` ou `var`. Apenas nome = valor.
* **Strings:** F-strings (`f"Olá, {nome}"`) equivalem a template literals (\`\${nome}\`) no JS.
* **Números:** Não precisa declarar tipo, operações seguem lógica semelhante ao JS.
* **Constantes:** Só existe convenção (nome em CAPS), não existe palavra-chave real.
* **Comentários:** Sempre com `#`, não há comentário em bloco (`/* ... */`).

---

## **Pronto para o próximo passo**

Agora que você já entende os tipos básicos e variáveis, pode criar scripts mais dinâmicos e começar a experimentar lógica e processamento de dados. No próximo capítulo, vai entrar em **listas** (equivalente aos arrays do JS), tornando possível manipular coleções de dados.

Se quiser, posso criar exemplos extras ou desafios baseados nesse capítulo — ou já sugerir mini projetos para praticar conceitos pensando em IA, processamento de strings ou manipulação de dados.
