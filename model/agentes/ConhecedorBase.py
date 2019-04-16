import xml.etree.ElementTree as et

arquivoXML = 'model/arquivos/baseDados.xml'
arvore = et.parse(arquivoXML)
raiz = arvore.getroot()

def _retornarResposta(nome, acusacao):
    if len(_retornarFN(_retornarVacina(nome), acusacao))>0:
        return _retornarFN(_retornarVacina(nome), acusacao)[3].text, _retornarFN(_retornarVacina(nome), acusacao)[4].text
    return ''

def _retornarDescricao(vacina,filho):
    aux = [i for i in _retornarVacina(vacina) if i.tag == filho]
    if len(_retornarVacina(vacina))>0 and len(aux) > 0:
        return aux[0].text
    return ''

def _retornarVacina(nome):
    for x in raiz:
        if nome.lower() == (x.attrib['nome']).lower() or nome.lower() == (x.attrib['sigla']).lower():
            return x
    return '' 

def _retornarFN(id,acusacao):
    if id != '':
        nunFN = [i for i in id if i.tag =='fakenews'][0]
        for x in nunFN:
            if acusacao.lower() == (x[0].text).lower() or acusacao.lower() == (x[1].text).lower() or acusacao.lower() == (x[2].text).lower():
                return x
    return ''

def agenteCapitaoAmerica(vacina, frase):
    tempFN = _retornarResposta(vacina,frase)
    tempDescri = _retornarDescricao(vacina,frase)

    if(tempFN!=''):
        return tempFN
    if(tempDescri!=''):
        return tempDescri
    return ''
