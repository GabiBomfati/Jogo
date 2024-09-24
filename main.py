'''
Jogo do Adivinhe o Número
2024.07.30
Gabriela Bomfati Garcia
'''
#Objetivo: Desenvolver um jogo, onde o usúario deverá tentar adivinhar um número secreto sortedo pelo PC

# Módulos e Bibliotecas
from random import randint # Importa números aleátorios, dentro de um determinado intervalo 
 
# Variáveis
msg = '' # Variável para msg (mudar de acordo com a situação)
numeroSecreto = 0 # Variável para numeroSecreto (muda de acordo com a situação)

# CONSTANTES
CAR = "+" # Define o carácter que aparcerá para demarcar o tamanho da tela e da margem 
TDT = 40 # Define o tamanho da tela 
MAR = 2 # Define o tamanho da margem 
INI = 1 # Define a partir de que número começa o sorteio do número secreto
FIM = 100 # Define onde termina o sorteio do número secreto
TVS = 3 # Define quantas tentativas o usuário terá no jogo

# Listas
listaMsgs = [] # variável para listaMsgs

# Funções

# Função para mostrar uma linha de caracteres
def mostraLinha(): # Essa função mostra uma linha de caracteres
  print(CAR*TDT) # Delimita com "+" e mostra o tamanho da dela

# Função para mostrar um texto centralizado entre um número de caracteres
def msgCentro(msg): # Essa função indica que uma mensagem será mostrada no centro da tela
  print(f"{CAR} {msg:^{TDT-MAR-MAR}} {CAR}") # Delimita o tamanho da tela e da margem com "+" e mostra uma mensagem ao centro da tela delimitada

# Função para mostrar um cabeçalho com texto entre as linhas
def cabecalho(listaMsgs): # Essa função cria o cabeçalho
  mostraLinha() # Mostra uma linha de carácter
  for msg in listaMsgs: # Coloca uma mensagem dentro da variável listaMsgs
    msgCentro(msg) # Mostra uma mensagem no centro da tela
  mostraLinha() # Mostra uma linha de carácter

# Função para sortear um número secreto
def sorteiaNum(): # Essa função sorteia um número
  numeroSecreto = randint(INI,FIM) # Determina o intervalo em que será sorteado o número secreto, de acordo com o que foi importado e determinado nas constantes anteriormente
  return numeroSecreto # Retorna com o número secreto

#Função para pegar a resposta e testar se é um número
def pegaResposta(): # Essa função pega a resposta dada pelo usuário
  resposta = input(f"{CAR} Sua resposta: ") # Mostrará "+ Sua resposta: " e indicará que você deve digitar um número
  while not resposta.isdigit(): # Testará se o que você digitou é um número inteiro ou não
    listaMsgs = ["Resposta Inválida!", "Tente outro Número"] # Caso sua resposta não seja um número inteiro, mostrará essa mensagem na tela, quando listaMsgs for chamada
    cabecalho(listaMsgs) # Mostrará a mensagem a cima no cabeçalho, na tela
    resposta = input(f"{CAR} Sua resposta: ") # Mostrará "+ Sua resposta: " e indicará que você deve digitar um número
  resposta = int(resposta) # Indica que a resposta deve ser um número inteiro
  return resposta # Retorna com a resposta

# Função para dar dica
def dica(numeroSecreto, resposta): # Essa função mostrará uma dica de acordo com o número secreto e a resposta dada
  if numeroSecreto < resposta: # Verifica se o número secreto é menor que a resposta
    cabecalho("Tente um número MENOR!") # Se o número secreto for menor que a resposta dada, essa mensagem aparecerá na tela
  else: # Se o número secreto não for menor que a resposta, o else será executado para verifcar se o número secreto é maior que a resposta dada
    cabecalho("Tente um número MAIOR!") # Se o número secreto for maior que a resposta dada, essa mensagem aparecerá na tela

# Função para o jogo Startar
def startGame(): # Essa função começa o jogo
  TVS = 3 # Define que o usuário terá 3 tentativas
  numeroSecreto = sorteiaNum() # Define que o número secreto será sorteado
  listaMsgs = ["JOGO DO ADIVINHE O NUMERO","Powred by Gabriela Bomfati"] # Mostrará essa mensagem na tela, quando listaMsgs for chamada
  cabecalho(listaMsgs) # Mostra a mensagem escrita a cima no cabeçalho, na tela
  playGame(TVS, numeroSecreto) # O número secreto é escolhido e as tentaivas do usuário começam

def playGame(TVS, numeroSecreto): # Essa função define qual é o número secreto e começa a contar as tentativas
  for tentativas in range(TVS): # Afirma que a quantidade de tentativas será igual a TVS
    resposta = pegaResposta() # A resposta receberá a resposta dada pelo usuário
    testeAcerto = resposta == numeroSecreto # Verifca se a resposta é igual ao número secreto
    if testeAcerto: # Testa se a resposta é igual ao número secreto
      listaMsgs = ['OLOCO BIXO!!!', 'ACERTOU MEMO!!!'] # Mostrará essa mensagem na tela, quando listaMsgs for chamada
      cabecalho(listaMsgs) # Mostra a mensagem escrita a cima no cabeçalho, na tela
      break # Interrompe o laço for
    elif tentativas != 2: # Só é executado se o if for falso e o elif for verdadeiro, e verifica se o número de tentativas é diferente de 2
      listaMsgs = ['SE É RUIM D+', 'NÃO É ASSIM CRIATURA'] # Se o usuário não certar o número secreto, essa mensagem aparecerá na tela, quando listaMsgs for chamada
      cabecalho(listaMsgs) # Mostra a mensagem escrita a cima no cabeçalho, na tela
      dica(numeroSecreto, resposta) # Mostrará uma dica, indicando se o número secreto é maior ou menor que a resposta dada
    else: # Só é executado se o if for falso, e verifica se a resposta é igual ao número secreto ou não
      cabecalho("MelDels que feio!!!") # Se a resposta não for igual ao número secreto essa mensagem aparecerá no cabeçalho na tela e essa mensagem será mostrada uma letra por linha
  else: # Verifca se você tem mais tentativas de jogo
    listaMsgs = ["FIM DE JOGO!", "O NUMERO SECRETO ERA", numeroSecreto, "PARABÉNS YOU LOSE!"] # Se suas tentativas tiverem acabado essa mensagem aparecerá na tela e revelará o número secreto, quando listaMsgs for chamada
    cabecalho(listaMsgs) # Mostrará a mensagem cima no cabeçalho, na tela 
    listaMsgs = ["Deseja Jogar Novamente?", "[0 - NÃO]", "[1 - SIM]"] # Após o fim do jogo essa mensagem aparecrá na tela, quando listaMsgs for chamada
    cabecalho(listaMsgs) # Mostrará a mensagem a cima no cabeçalho, na tela
    resposta = pegaResposta() # Verifca a resposta do usuário, se ele deseja ou não jogar novamente
    if resposta == 1: # Verifica se a resposta dada pelo usuário foi 1
      startGame() # Se a resposta for 1 o jogo se inica novamente
    else: # Só é executado se a resposta do if for falsa, e verifica se a resposta dade pelo usuário foi diferente de 1
      listaMsgs = ["FOI BOM JOGAR COM VOCÊ!", "ATÉ A PROXIMA"] # Se o usuário responder que não deseja jogar novamente, essa mensagem aparecerá na tela, quando listaMsgs for chamada
      cabecalho(listaMsgs) # Mostrará a mesangem acima no cabeçalho, na tela

#Programa Principal
startGame() # Inicia o jogo novamente