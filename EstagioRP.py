# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def fibonacci():
    a = 0
    b = 1
    lista_fibonacci = [a, b]

    while True:
        proximo_numero = a + b
        lista_fibonacci.append(proximo_numero)
        a = b
        b = proximo_numero
        if proximo_numero > 1000000:  
            break
    
    return lista_fibonacci

x = int(input("Digite um numero: "))

if x in fibonacci():
    print("Esse numero faz parte da sequência de Fibonacci")
else:
    print("Esse numero não faz parte da sequencia de Fibonacci")


# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

string = input("Digite uma palavra: ")
contador = 0

for i in string:
    if i == 'a' or i == 'A':
        contador += 1

if contador > 0:
    print(f"A letra 'a' aparece {contador} vez(es) na string.")
else:
    print("A letra 'a' não está presente na string.")

# 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1 
    soma = soma + k
    print(soma)
    
print(soma)

# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____

a) 9
b) 128
c) 49
d) 100
e) 13
f) 20

# 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes.
# Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.
# Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas,
# qual interruptor controla cada lâmpada? 

Eu ligaria o interruptor1 e deixaria ele ligado por cerca de 15 minutos para que a lâmpada esquentasse bastante. Depois, ligaria o interruptor2 e desligaria o interruptor1.
Em seguida, iria para a sala das lâmpadas. Assim, a lâmpada que estiver ligada é referente ao interruptor2, a lâmpada apagada que estiver quente é referente ao interruptor1
e a lâmpada que estiver apagada e fria é referente ao interruptor3
