from agentes.Pasquale import Pasquale
from agentes.Ramalho import Ramalho
from agentes.CapitaoAmerica import CapitaoAmerica

class Edward:
    def __init__(self):
        self._ag1 = Pasquale()
        self._ag2 = Ramalho()
        self._ag3 = CapitaoAmerica()
        self.resposta = ''
        self.referencia = ''
    #frase = 'Vacina do HPV UM INCENTIVO À VIDA SEXUAL PRECOCE?'

    def _agir(self, frase):
        frases = self._ag1.tratadas(frase)
        frases.append(frase)
        cont = len(frases)-1
        while(cont>=0):
            aux = self._ag2.retornaFaseComPalavrasConecidas(frases[cont])
            frases.append(aux)
            cont-=1

        for i in frases:
            aux = self._ag3.agenteCapitaoAmerica(i)
            if aux != '':
                self.resposta = aux[0]
                self.referencia = aux[1]
                break
        return self.resposta,self.referencia

