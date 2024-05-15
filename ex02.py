votos_geral = 0
idade_geral = 0
votos_CS2 = 0
idade_CS2= 0
media_CS2 = 0
votos_Dota2 = 0
idade_Dota2 = 0
media_Dota2 = 0
votos_LOL = 0
idade_LOL = 0
media_LOL = 0
votos_Valorant = 0
idade_Valorant = 0
media_Valorant = 0
listaCS2 = ["CS2", votos_CS2, media_CS2]
listaDota2 = ["Dota 2", votos_Dota2, media_Dota2]
listaLOL = ["LOL", votos_LOL, media_LOL]
listaValorant = ["Valorant", votos_Valorant, media_Valorant]

def menu():
    return print("\nEm qual você deseja votar?\n1 - CS2\n2 - Dota 2\n3 - LOL\n4 - Valorant\n5 - Sair")

def maior():
    if votos_CS2 > votos_Dota2 and votos_CS2 > votos_LOL and votos_CS2 > votos_Valorant:
        return print(f"Mais votado: CS2 com {votos_CS2} votos")
    elif votos_Dota2 > votos_CS2 and votos_Dota2 > votos_LOL and votos_Dota2 > votos_Valorant:
        return print(f"Mais votado: CS2 com {votos_Dota2} votos")
    elif votos_LOL > votos_CS2 and votos_LOL > votos_Dota2 and votos_LOL > votos_Valorant:
        return print(f"Mais votado: CS2 com {votos_LOL} votos")
    elif votos_Valorant > votos_CS2 and votos_Valorant > votos_Dota2 and votos_Valorant > votos_LOL:
        return print(f"Mais votado: CS2 com {votos_Valorant} votos")
    else:
        return print("Empate!")
    
def menor():
    if votos_CS2 < votos_Dota2 and votos_CS2 < votos_LOL and votos_CS2 < votos_Valorant:
        return print(f"Menos votado: CS2 com {votos_CS2} votos")
    elif votos_Dota2 < votos_CS2 and votos_Dota2 < votos_LOL and votos_Dota2 < votos_Valorant:
        return print(f"Menos votado: Dota 2 com {votos_Dota2} votos")
    elif votos_LOL < votos_CS2 and votos_LOL < votos_Dota2 and votos_LOL < votos_Valorant:
        return print(f"Menos votado: LOL com {votos_LOL} votos")
    elif votos_Valorant < votos_CS2 and votos_Valorant < votos_Dota2 and votos_Valorant < votos_LOL:
        return print(f"Menos votado: Valorant com {votos_Valorant} votos")
    else:
        return print("Empate!")

while True:
    menu()
    listaCS2 = ["CS2", votos_CS2, media_CS2]
    listaDota2 = ["Dota 2", votos_Dota2, media_Dota2]
    listaLOL = ["LOL", votos_LOL, media_LOL]
    listaValorant = ["Valorant", votos_Valorant, media_Valorant]
    escolha = int(input("Escolha uma das opções: "))
    if escolha == 1:
        votos_CS2 += 1
        votos_geral += 1
        idade = int(input("Informe sua idade: "))
        idade_CS2 += idade
        idade_geral += idade
        media_CS2 = idade_CS2/votos_CS2
    elif escolha == 2:
        votos_Dota2 += 1
        votos_geral += 1
        idade = int(input("Informe sua idade: "))
        idade_Dota2 += idade
        idade_geral += idade
        media_Dota2 = idade_Dota2/votos_Dota2
    elif escolha == 3:
        votos_LOL += 1
        votos_geral += 1
        idade = int(input("Informe sua idade: "))
        idade_LOL += idade
        idade_geral += idade
        media_LOL = idade_LOL/votos_LOL
    elif escolha == 4:
        votos_Valorant += 1
        votos_geral += 1
        idade = int(input("Informe sua idade: "))
        idade_Valorant += idade
        idade_geral += idade
        media_Valorant = idade_Valorant/votos_Valorant
    elif escolha == 5:
        media_geral = idade_geral/votos_geral
        print("Saindo...")
        print(70*"-")
        print(listaCS2)
        print(listaDota2)
        print(listaLOL)
        print(listaValorant)
        maior()
        menor()
        print(f"Total de votantes: {votos_geral}, média de idade: {media_geral}")
        break
    else:
        print("Comando inválido!")
        continue