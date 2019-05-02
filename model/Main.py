from agentes.Pasquale import Pasquale
from agentes.Ramalho import Ramalho
from agentes.CapitaoAmerica import CapitaoAmerica

class Edward:
    def __init__(self):
        self._ag1 = Pasquale()
        self._ag2 = Ramalho()
        self._ag3 = CapitaoAmerica()
        self.resposta = []

    def _agir(self, frase):
        frases = self._ag1.tratadas(frase)
        cont = len(frases)-1
        while(cont>=0):
            aux = self._ag2.retornaFaseComPalavrasConhecidas(frases[cont])
            frases.append(aux)
            cont-=1

        for i in frases:
            aux = self._ag3.agenteCapitaoAmerica(i)
            if aux != '' and [aux[0],aux[1]] not in self.resposta:
                self.resposta.append([aux[0],aux[1]])
        return self.resposta


test = Edward()
nosso = test._agir('Vacina contra o HPV da a incentiva o sexo sem preservativo. Vacina do HPV UM encorajamento PRECOCE À VIDA SEXUAL')

for i in nosso:
    print(i)