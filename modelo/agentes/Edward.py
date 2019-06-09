from Pasquale import Pasquale
from Ramalho import Ramalho
from CapitaoAmerica import CapitaoAmerica

class Edward:
    def __init__(self):
        self._ag1 = Pasquale()
        self._ag2 = Ramalho()
        self._ag3 = CapitaoAmerica()
        self.acusacao = []
        self.resposta = []

    def _verificarFrases(self, frases):
        for i in frases:
            aux = self._ag3.agenteCapitaoAmerica(i[1])
            if aux != '' and [aux[0],aux[1]] not in self.resposta:
                for j in frases:
                    if j[0] == i[0]:
                        self.acusacao.append(j[1])
                        break
                self.resposta.append([aux[0],aux[1]])

    def _agir(self, frase):
        frasesTradadascomIDs = self._ag1.tratadas(frase)
        cont = len(frasesTradadascomIDs)-1
        while(cont>=0):
            aux = self._ag2.retornaFaseComPalavrasConhecidas(frasesTradadascomIDs[cont][1])
            frasesTradadascomIDs.append([frasesTradadascomIDs[cont][0],aux])
            cont-=1
        self._verificarFrases(frasesTradadascomIDs)   
        return self.acusacao,self.resposta
    
    def verificarTexto(self,frase):
        resp = []
        aux = self._agir(frase)
        for i in range(len(aux[0])):
            resp.append([aux[0][i],aux[1][i]])
        return resp
    
    def responder(self, arrayDeAcusacoesRespostas):
        resp = ''
        for i in arrayDeAcusacoesRespostas:
            resp+= 'Sobre a frase: {}\nDeclaro: {}\n<Fonte para mais pesquisas: {}>\n\n'.format(i[0],i[1][0],i[1][1])
        return resp
    