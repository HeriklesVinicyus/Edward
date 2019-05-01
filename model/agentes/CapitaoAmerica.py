import xml.etree.ElementTree as et
class CapitaoAmerica:
    def __init__(self):
        self._arquivoXML = 'model/arquivos/bases/baseDados.xml'
        self._arvore = et.parse(self._arquivoXML)
        self.raiz = self._arvore.getroot()

    def _retornarResposta(self, nome, acusacao):
        if len(self._retornarFN(self._retornarVacina(nome), acusacao))>0:
            return self._retornarFN(self._retornarVacina(nome), acusacao)[3].text, self._retornarFN(self._retornarVacina(nome), acusacao)[4].text
        return ''

    def _retornarDescricao(self,vacina,filho):
        aux = [i for i in self._retornarVacina(vacina) if i.tag == filho]
        if len(self._retornarVacina(vacina))>0 and len(aux) > 0:
            return aux[0].text
        return ''

    def _retornarVacina(self,nome):
        for x in self.raiz:
            if nome.lower() == (x.attrib['nome']).lower() or nome.lower() == (x.attrib['sigla']).lower():
                return x
        return '' 

    def _retornarFN(self,id,acusacao):
        if id != '':
            nunFN = [i for i in id if i.tag =='fakenews'][0]
            for x in nunFN:
                if acusacao.lower() == (x[0].text).lower() or acusacao.lower() == (x[1].text).lower() or acusacao.lower() == (x[2].text).lower():
                    return x
        return ''

    def _descobreVacina(self, frase):
        for nome in frase.split(' '):
            palavras = self._retornarVacina(nome)
            if palavras != '':
                return nome
        return 'TODAS'

    def agenteCapitaoAmerica(self, frase):
        vacina = self._descobreVacina(frase)
        tempFN = self._retornarResposta(vacina,frase)
        tempDescri = self._retornarDescricao(vacina,frase)

        if(tempFN!=''):
            return tempFN
        if(tempDescri!=''):
            return tempDescri
        return ''