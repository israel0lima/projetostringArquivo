def contar(frase):
    letras = 0
    nums = 0
    for i in frase:
        if((i>='a' and i<='z') or (i>='A' and i<='Z')):
            letras+=1
        elif(i>='0' and i<='9'):
            nums+=1
    print(letras)
    print(nums)


frase = input()
contar(frase)
