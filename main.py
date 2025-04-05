# nome= input(f"digite seu nome:")
# print(f"Seja muito bem vindo ao  mundo, {nome}")

# numero= int(input("Digite um numero:"))
# if numero%2 == 0 :
    # print("seu numero é par")
# else:
    # print("seu numero é impar")

# lista= []

# nome= input(f"digite o primeiro nome:")
# nome1= input(f"digite o segundo  nome:")
# nome2= input(f"digite o terceiro nome:")

# *REPETE QUANTAS VEZES VOCE DEFINIR DENTRO DO RANGE (ESTE ITEM + SEGUINTE)
# for i in range(0,3): 
#     i= input("Digite o nome:")
#     lista.append(i)

# lista.append(nome)
# lista.append(nome1)
# lista.append(nome2)

# *REPETE O NUMERO DE VEZES DE ITENS DENTRO DE LISTAS (ESTE ITEM + ANTERIOR)
# for n in lista: 
#     print(n)


def adiciona_nomes_na_lista(ls):
    # print("adiciona nome à lista")
    # print(nm)
    # ou
    ls.append(input("Digite um nome"))
    print(ls)
def remove_nomes_na_lista(ls):
    # print("remove nome à lista")
    # print(b)
    # ou 
    ls.remove(input("digite o nome"))
    print(ls)
menu= 1
listaNomes = []
while menu==1:
    print("o que voce quer fazer?")

    print("1.Adicionar nomes")
    print("2.Remover nomes")

    escolha= input("digite uma opção: ")

    if escolha == "1":
        adiciona_nomes_na_lista(listaNomes)
        menu+=1
        print(listaNomes)
    elif escolha == "2":
        remove_nomes_na_lista(listaNomes)
        menu+=1
        print(listaNomes)
    else:
        print("erro")