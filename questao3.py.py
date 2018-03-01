def Tem(palavra,conj):
    cont = 0
    for i in range(len(conj)):
        for c in range(len(palavra)):
            if(conj[i]==palavra[c]):
                cont+=1
                break

    if(cont==len(conj)):
        return True
    else:
        return False
i = input()
s = input()

if(Tem(i,s)):
    print("TODAS AS LETRAS ENCONTRADAS")
else:
    print("TODAS NÃO FORAM ENCONTRADAS")
                
