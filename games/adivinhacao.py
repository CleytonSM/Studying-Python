import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101) # trabalha com num. inteiros com um range, nesse caso, de 1 à 100  , ou, uma de forma porca, -> random.random() -> 0.0 - 1.0 * 100 #
    total_de_tentativas = 0
    pontos = 1000

    print("QUal nível de dificuldade?", numero_secreto)
    print("(1) Fácil  (2) Médio  (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
        print("Você escolheu o nível facil!")
    elif(nivel == 2):
        total_de_tentativas = 10
        print("Você escolheu o nível médio!")
    else:
        total_de_tentativas = 5
        print("Você escolheu o nível difícil!")



    for  contador_de_rodadas in range(1, total_de_tentativas + 1):
        print(f"Tentativa {contador_de_rodadas} de {total_de_tentativas}")
        chute = input("Digite o seu número entre 1 e 100: ")
        numero_chute = int(chute)
        print("Você digitou ", chute)
        
        if (numero_chute < 1 or numero_chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_chute == numero_secreto
        maior = numero_chute > numero_secreto
        menor = numero_chute < numero_secreto
        
        if(acertou):
            print("Você Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número")
            pontos_perdidos = abs(numero_secreto - numero_chute)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()