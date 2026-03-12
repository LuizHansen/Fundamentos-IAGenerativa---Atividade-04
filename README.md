# Assistente com Memória

Projeto desenvolvido como parte do **Desafio da Aula 04**, com o objetivo de evoluir um chatbot simples adicionando controle de memória, persona, integração com funções Python e persistência de dados.

---

# Funcionalidades Implementadas

## 1. Controle de Memória

Foi implementado o comando:

```
/limpar
```

Quando utilizado, o histórico da conversa é apagado e o assistente retorna a mensagem:

```
Memória da conversa apagada.
```

Isso permite iniciar uma nova conversa sem manter o contexto anterior.

---

## 2. Persona do Assistente

Foi adicionada uma **mensagem de sistema** que define o comportamento do assistente.

O assistente foi configurado para responder de forma:

* educada
* clara
* objetiva
* amigável

Essa configuração garante que o padrão de resposta seja consistente durante toda a interação.

---

## 3. Limite de Memória

Para evitar que o histórico cresça indefinidamente, foi implementado um limite máximo de **10 mensagens** armazenadas.

Quando o limite é ultrapassado:

* as mensagens mais antigas são removidas automaticamente
* apenas as **10 mensagens mais recentes** permanecem no histórico

Isso melhora o desempenho e evita excesso de contexto enviado ao modelo.

---

## 4. Integração de Funções Python

Foram implementadas duas funções externas para realizar tarefas específicas.

### Calcular Idade

O usuário informa o ano de nascimento e o sistema calcula a idade aproximada com base no ano atual.

Exemplo de uso:

```
Digite seu ano de nascimento
```

O sistema retorna a idade calculada.

---

### Conversão de Temperatura

Permite converter temperaturas entre **Celsius** e **Fahrenheit**.

Exemplo:

```
Converter temperatura de C para F
```

O sistema realiza o cálculo e retorna o valor convertido.

---

## 5. Persistência de Dados

O histórico da conversa é salvo em um arquivo:

```
history.json
```

Esse arquivo armazena todas as mensagens da conversa.

Quando o programa é iniciado novamente:

* o histórico é carregado automaticamente
* a conversa pode continuar do ponto em que parou

---

# Estrutura do Projeto

```
assistente-memoria/

main.py
memory_manager.py
functions.py
history.json
requirements.txt
README.md
```

Descrição dos arquivos:

**main.py**

Arquivo principal responsável pela execução do assistente e interação com o usuário.

**memory_manager.py**

Responsável por gerenciar o histórico da conversa, incluindo:

* armazenamento
* limite de mensagens
* limpeza da memória
* persistência em JSON

**functions.py**

Contém as funções Python utilizadas para executar tarefas específicas.

**history.json**

Arquivo onde o histórico da conversa é armazenado.

**requirements.txt**

Arquivo com as dependências necessárias para executar o projeto.

---

# Como Executar o Projeto

## 1 Instalar as dependências

Execute no terminal:

```
pip install -r requirements.txt
```

---

## 2 Configurar a chave da API

Defina sua chave da API da OpenAI.

Linux ou Mac:

```
export OPENAI_API_KEY="sua-chave"
```

Windows:

```
set OPENAI_API_KEY=sua-chave
```

---

## 3 Executar o projeto

Execute o arquivo principal:

```
python main.py
```

Após iniciar, o assistente estará pronto para receber mensagens.

---

# Reflexão

## Se o histórico crescer muito, quais problemas podem ocorrer no uso de LLMs?

Se o histórico crescer excessivamente, podem ocorrer alguns problemas como:

* aumento no custo de uso da API
* maior tempo de resposta
* possibilidade de atingir o limite de contexto do modelo
* redução da relevância das mensagens antigas na geração da resposta

Por esse motivo, é importante limitar o tamanho do histórico de conversas.

---

## Por que algumas tarefas são melhores resolvidas por funções Python do que pelo próprio LLM?

Algumas tarefas são mais adequadas para serem executadas diretamente por código, como:

* cálculos matemáticos
* manipulação de datas
* conversões de unidades
* geração de valores determinísticos

Isso acontece porque funções Python são mais rápidas, precisas e não apresentam risco de gerar respostas incorretas por interpretação do modelo.

---

## Quais riscos existem ao deixar que o LLM tome decisões sobre quando usar uma função?

Quando o modelo decide sozinho quando utilizar uma função, alguns riscos podem surgir, como:

* interpretar incorretamente a intenção do usuário
* utilizar uma função quando não é necessário
* enviar parâmetros incorretos para a função
* gerar resultados inconsistentes

Por esse motivo, muitos sistemas utilizam validações adicionais ou mecanismos específicos para controlar o uso de funções pelo modelo.

---

# Considerações Finais

Durante o desenvolvimento deste projeto foi possível compreender melhor:

* como gerenciar memória em aplicações com LLMs
* como integrar funções externas ao fluxo de conversa
* a importância de limitar o histórico de mensagens
* como persistir dados para manter continuidade entre execuções

Esses conceitos são fundamentais para o desenvolvimento de **assistentes mais robustos e úteis em aplicações reais**.
