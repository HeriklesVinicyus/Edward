import xml.etree.ElementTree as et
from Edward import Edward

#class Validador
def buscarEntradas():
    _resp = ''
    _arquivoXML = 'validar/Entrada.xml'
    _arvore = et.parse(_arquivoXML)
    _raiz = _arvore.getroot()
    for i in _raiz:
        _resp += i.text+'\n'
    return _resp

def adcionarSaida(acusacao, respostaFonte):
    _arquivoXML = 'validar/Saida.xml'
    _arvore = et.parse(_arquivoXML)
    _raiz = _arvore.getroot()
    _novaSaida = et.SubElement(_raiz,'saida')
    _novaAcusacao = et.SubElement(_novaSaida,'acusacao')
    _resposta = et.SubElement(_novaSaida,'resposta')
    _fonte = et.SubElement(_novaSaida,'fonte')
    _novaAcusacao.text = acusacao
    _resposta.text = respostaFonte[0]
    _fonte.text = respostaFonte[1]
    _arvore.write(_arquivoXML)

def adcionarVariasSaidas(lista):
    for i in lista:
        adcionarSaida(i[0][0],i[0][1])


#Teste se conforme as entradas validar as saidas
entradas = buscarEntradas()
lista = []
for i in entradas.split('\n'):
        aux =Edward().verificarTexto(i)
        if len(aux) != 0:
                lista.append(aux)

adcionarVariasSaidas(lista)
