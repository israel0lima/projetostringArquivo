arquivo = open("words.txt","r")
lista_de_palavras = arquivo.readlines()
s = 0
for i in lista_de_palavras:
    if(len(i)>20):
        s+=1
print(s)

arquivo.close()
