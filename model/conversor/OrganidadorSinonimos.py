arquivo = open('model/arquivos/sinonimos.txt','r')
texto = arquivo.read()
textoModificado = ''
lista = []

def _removerEntre(txt):
    return ' '.join(txt.split('\n'))
def _removerSpace(txt):
    return ''.join(txt.split(' '))

def _removerTextoEspecifico(txt, remover):
    return ' '.join(txt.split(remover))

def _subistituirNumeros(txt, cont, caracter):
    temp = txt
    for i in range(cont,-1,-1):
        temp = temp.replace(str(i),caracter)
    return temp

def _retornaApenasSinonimosTXT(txt,cInicial,cFinal):
    palavra = ''
    palavraSiginificado = txt.split(cInicial)
    cont = 0
    for x in palavraSiginificado:
        cont +=1
        print(x.split(cFinal),cont)
        palavra += (x.split(cFinal))[0]+'\n\n'
    
    return palavra

def _retornaApenasSinonimosList(txt):
    temp = ''
    #id = 0
    for i in txt.split(' '):
        #print(i)
        if i.isupper() and len(i)>1 and (i[0]!='\"'and i[0]!='“' and i[1]!='.'):
           temp+=str(i)
    return temp

textoModificado = _removerEntre(texto)
textoModificado = _removerTextoEspecifico(textoModificado,'@')
textoModificado = _subistituirNumeros(textoModificado,10,'')
textoModificado = _retornaApenasSinonimosList(textoModificado)

texto = _removerEntre(texto)
texto = _subistituirNumeros(texto,1000,'\n\n@')

for i in texto.split('\n\n'):
    if len(i.split(' '))>1 and i.split(' ')[1].isupper():
        lista.append(i)

for i in texto.split('\n\n'):
    if len(i.split(' '))>1 and i.split(' ')[1].isupper():
        lista.append(i)

texto
print ('\n\n'.join(lista))
arquivo.close()