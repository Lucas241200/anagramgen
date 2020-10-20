from random import shuffle

def fat (numero): #FAZENDO MINHA PROPRIA FUNÇÃO DE FATORIAL
    contador = 0
    lista_do_fatorial = [numero]
    formula = 0
    def multiply_list(mylist):
        resultado=1
        for numero in mylist:
            resultado=resultado*numero
        return resultado


    while contador != numero-1:
        contador+=1
        formula=numero-contador
        lista_do_fatorial.append(formula)
    return multiply_list(lista_do_fatorial)
""""THE FUNCTION ABOVE WAS JUST FOR FUN, BUT IT'S POSSIBLE TO USE THE LIBRARY MATH INSTEAD"""
print("Anagrama")
palavra=str(input("Digite uma palavra: "))
lista_de_letras=[palavra[i:i+1] for i in range (0, len(palavra),1)] #DIVIDINDO OS CARACTERES E BOTANDO NUMA LISTA
lista_final = [palavra]
nova_palavra=""
espaço_vazio=""
count=0
caracteres_repetidos=[]
caracteres_iguais=[]
for l in palavra:
    continha = palavra.count(l)
    if continha > 1:
        caracteres_repetidos.append(l)
        caracteres_iguais.append(l)
        if caracteres_iguais.count(l) > 1:
            caracteres_iguais.remove(l)

conta=1
contagem=0
for c in caracteres_iguais:
    contagem=caracteres_repetidos.count(c)
    conta=conta*fat(contagem)

fatorial=fat(len(lista_de_letras))/conta
while nova_palavra not in lista_final and len(lista_final) < fatorial:
    count+=1
    shuffle(lista_de_letras)
    for letra in lista_de_letras:
        nova_palavra+=str(letra)
    lista_final.append(nova_palavra)
    if lista_final.count(nova_palavra) > 1:
        lista_final.remove(nova_palavra)
    nova_palavra=espaço_vazio
    len(lista_final)
lista_final.sort()
print(lista_final)
print(len(lista_final),"Maneiras de escrever {} em ordem alfabética." .format(palavra))