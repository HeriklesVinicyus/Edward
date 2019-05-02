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
            TodasFNdaVacina = [i for i in id if i.tag =='fakenews'][0]
            for x in TodasFNdaVacina:
                if acusacao.lower() == (x[0].text).lower() or acusacao.lower() == (x[1].text).lower() or acusacao.lower() == (x[2].text).lower():
                    return x
        return ''

    def _descobreVacina(self, frase):
        for nome in frase.split(' '):
            palavras = self._retornarVacina(nome)
            if palavras != '':
                return nome
        return 'TODAS'

    def _verificaSeExisteTodasPalavrasDaFrase(self,fraseBase,acusacao):
        flagTemaPalavra = False
        #print (fraseBase,acusacao)
        for y in fraseBase.split(' '):
            flagTemaPalavra = False
            for z in acusacao.split(' '):
                if(y.lower()==z.lower()):
                    flagTemaPalavra = True
                    break
            if not (flagTemaPalavra):
                return flagTemaPalavra
        return flagTemaPalavra
    
    def _buscarFNPorPalavrasNaFrase(self,nome,acusacao):
        vacina = self._retornarVacina(nome)
        if len(vacina)>0:
            TodasFNdaVacina = [i for i in vacina if i.tag =='fakenews'][0]
            for x in TodasFNdaVacina:

                for i in range(3):
                    resp = self._verificaSeExisteTodasPalavrasDaFrase(x[i].text,acusacao)
                    if resp:
                        return x
        return ''

    def agenteCapitaoAmerica(self, frase):
        vacina = self._descobreVacina(frase)
        tempFN = self._retornarResposta(vacina,frase)
        if(tempFN!=''):
            return tempFN

        #para Buscar FN caso ordem das palavras não encontre-se diferente da Base
        tempFN = self._buscarFNPorPalavrasNaFrase(vacina,frase)
        if(tempFN!=''):
            return (tempFN[3].text, tempFN[4].text)

        tempDescri = self._retornarDescricao(vacina,frase)
        if(tempDescri!=''):
            return tempDescri
        return ''