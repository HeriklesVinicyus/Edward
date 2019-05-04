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
        #print(x.split(cFinal),cont)
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

texto = ''.join(lista)
lista = texto.split('@')
texto = ''
#print(lista)
for i in lista:
        if len(i.split(' – '))>0:
                texto += i.split(' – ')[0]+'\n'

lista = []
lista = texto.split('\n')
texto = ''
for i in lista:
        if  not (len(i.split(' ')[0])>1):
                texto+= i.split('.')[0]+'\n'
texto = texto.replace('\n ','\n')
texto = texto.replace(';',',')
lista = texto.split('\n')
texto = ''
cont = 0
for i in lista:
        temp = i.split(', ')
        if temp[0].isupper() and not len(temp[0].split(' '))>1:
                aux = ['\n'+_removerSpace(x).lower()+'|{}'.format(cont) for x in temp]
                texto+=(''.join(aux))
                cont+=1
arquivo.close()

novoArquivo = open('model/arquivos/bases/BaseSinonimos.txt','w')
novoArquivo.write(texto)
novoArquivo.close()