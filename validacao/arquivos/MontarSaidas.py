#class MotarSaidas

'''
imports necessário para acessar a pasta controle
'''
import sys
import os
caminho = os.getcwd()
sys.path.append(caminho)

import xml.etree.ElementTree as et
#importação do controle
from controle.Edward import Edward

#Armazena o parâmetro no arquivo de saídas
def _adcionarSaida(acusacao, respostaFonte):
    _arquivoXML = 'validacao/Saida.xml'
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

#Retorna as frases do arquivo de entradas
def _buscarEntradas():
    _resp = ''
    _arquivoXML = 'validacao/Entrada.xml'
    _arvore = et.parse(_arquivoXML)
    _raiz = _arvore.getroot()
    for i in _raiz:
        _resp += i.text+'\n'
    return _resp

#Armazena no arquivo de saídas lista com varias saídas
def _adcionarVariasSaidas(lista):
        _arquivoXML = 'validacao/Saida.xml'
        _arvore = et.parse(_arquivoXML)
        _raiz = _arvore.getroot()
        cont = len(_raiz)-1
        for i in range(cont,-1,-1):
                _raiz.remove(_raiz.getchildren()[i])
        _arvore.write(_arquivoXML)
                
        for i in lista:
                _adcionarSaida(i[0][0],i[0][1])

#Função para recompilar o arquivo de saída
#Única função acessível fora dessa classe
def executar():
        entradas = _buscarEntradas()
        lista = []
        cont = 0
        for i in entradas.split('\n'):
                aux =Edward().verificarTextoEspscifico(i)
                if len(aux) != 0:
                        lista.append(aux)
                cont+=1

        _adcionarVariasSaidas(lista)