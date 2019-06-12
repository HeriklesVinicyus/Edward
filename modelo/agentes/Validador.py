#class Validador
import xml.etree.ElementTree as et
from Edward import Edward


#Retorna a frase de entrada e o id das frases que são CFN(legenda no arquivo /validar/MontarEntradas.py)
def buscarEntradas():
    _resp = ''
    _idCFN = []
    _arquivoXML = 'validar/Entrada.xml'
    _arvore = et.parse(_arquivoXML)
    _raiz = _arvore.getroot()
    for i in _raiz:
        _resp += i.text+'\n'
        if(i.attrib['tipo']=='cfn' or i.attrib['tipo']=='cfna'):
                _idCFN.append(int(i.attrib['id']))
    return _resp, _idCFN

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
        _arquivoXML = 'validar/Saida.xml'
        _arvore = et.parse(_arquivoXML)
        _raiz = _arvore.getroot()
        cont = len(_raiz)-1
        for i in range(cont,-1,-1):
                _raiz.remove(_raiz.getchildren()[i])
        _arvore.write(_arquivoXML)
                
        for i in lista:
                adcionarSaida(i[0][0],i[0][1])


#Test se conforme as entradas validar as saidas
entradas, idCFN = buscarEntradas()
lista = []
listaId = []
cont = 0
for i in entradas.split('\n'):
        aux =Edward().verificarTexto(i)
        if len(aux) != 0:
                listaId.append(cont)
                lista.append(aux)
        cont+=1

adcionarVariasSaidas(lista)
