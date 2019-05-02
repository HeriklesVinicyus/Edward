
def _buscarPalavrasBaseLista():
    arq = open('model/arquivos/bases/baseSinonimos.txt')
    temp = arq.read()
    arq.close()
    resp = []
    for i in temp.split('\n'):
        aux = i.split('|')
        resp.append([aux[0],aux[1]])
    return resp

def _buscarPalavrasDesconhecidas():
    arq = open('model/arquivos/bases/basePalavrasDesconhecidas.txt')
    temp = arq.read()
    arq.close()
    resp = []
    for i in temp.split('\n'):
        resp.append(i)
    return resp

def _adicionarPalavras(palavra):
    temp = _buscarPalavrasDesconhecidas()
    if not (palavra in temp):
        arq = open('model/arquivos/bases/basePalavrasDesconhecidas.txt','w')
        arq.write(('\n'.join(temp))+'\n'+palavra)
        arq.close()

def _palavrasConhecidas(lista):
    return [i[1] for i in lista]

def _retornaPalavrasConhecida(palavra, baseSinonimos):
    aux = [i[1] for i in baseSinonimos if i[0] == palavra]
    if len(aux) == 0:
        _adicionarPalavras(palavra)
        return palavra
    if len(aux) > 0:
        return aux[0]

class Ramalho:
    def __init__(self):
        self._listaSinonimos = _buscarPalavrasBaseLista()
        self._palavrasConhecidas = _palavrasConhecidas(self._listaSinonimos)
        self._palavrasDesconhecidas = _buscarPalavrasDesconhecidas()
    
    def _recaregarPalavrasDesconhecidas(self):
        self._palavrasDesconhecidas = _buscarPalavrasDesconhecidas()

    def retornaFaseComPalavrasConecidas(self,frase):
        temp = frase.split()
        #resp = ' '.join([ _retornaPalavrasConhecida(i,self._listaSinonimos) for i in temp])
        resp = ''
        for i in temp:
            aux = _retornaPalavrasConhecida(i,self._listaSinonimos)
            resp+= ' '+aux
        return ' '.join(resp.split())
