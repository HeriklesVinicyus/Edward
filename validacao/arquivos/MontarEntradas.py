'''
Script para pegar a o esta pesente em /validar/arquivo/entradaIdFrase.csv
e montar no formato de entrada espedado pelo script Validador.py
'''
import random

'''
Metodo para rotular a frase de acordo com a sua notação no arquivo/validar/arquivos/entradaIdFrase.csv:
0 = (cfn) frase com Fake news sobre vacinas e que estão iguais a base
1 = (cfna) frase com Fake news sobre vacinas e que estão semelhantes a base [alguma alteração sintatica]
2 = (sfn) frases sem Fake news sobre facinas
'''
def _rotulaFrase(notacao):
    if(notacao == '0'):
        return 'cfn'
    if(notacao == '1'):
        return 'cfna'
    if(notacao == '2'):
        return 'sfn'

def _montarEntrada():
    arquivoBase = open('validacao/arquivos/entradaIdFrase.csv','r')
    frasesSeparadas = arquivoBase.read().split('\n')
    arquivoBase.close()

    frasesSeparadasAleatorias = frasesSeparadas
    random.shuffle(frasesSeparadasAleatorias)
    temp = ''
    cont = 0
    for i in frasesSeparadasAleatorias:
        aux = i.split('\t')
        temp += '<afirmacao id="{}" tipo="{}">{}</afirmacao>'.format(cont,_rotulaFrase(aux[0]),aux[1])
        cont += 1
    return temp

def gerarArquivoEntrada():
    arquivoEntrada = open('validacao/Entrada.xml','w')
    arquivoEntrada.write('')
    arquivoEntrada.write('<entrada>{}</entrada>'.format(_montarEntrada()))
    arquivoEntrada.close()

gerarArquivoEntrada()