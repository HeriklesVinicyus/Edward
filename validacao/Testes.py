# Testes
import xml.etree.ElementTree as et
import matplotlib.pyplot as mp
import arquivos.MontarSaidas as ms

# Função para retornar as Raizes do arquivos XML de entrada e saida
def retornaRaizes():
    _arquivoXMLEntrada = 'validacao/Entrada.xml'
    _arquivoXMLSaida = 'validacao/Saida.xml'
    _arvoreE = et.parse(_arquivoXMLEntrada)
    _arvoreS = et.parse(_arquivoXMLSaida)
    _raizE = _arvoreE.getroot()
    _raizS = _arvoreS.getroot()
    return _raizE, _raizS


def gerarGrafico(titulos, dados):
    graf, ax1 = mp.subplots()
    
    ax1.pie(dados, labels=titulos, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    mp.show()

# Testa para verificar se frases que não sem FN foram respondidas(o resultado deve ser o mais proximo de 0)
def testRespondeuSFN():
    raizE, raizS = retornaRaizes()
    porcentagem = 0
    total = 0

    for x in raizE:
        for y in raizS:
            if (x.attrib['tipo'] == 'sfn' and x.text == y[0].text):
                porcentagem += 1
        if(x.attrib['tipo'] == 'sfn'):
            total = + 1
    porcentagem = (porcentagem*100)/total
    titulos = ['Entradas Sem Fake News respondidas',
               'Entradas Sem Fake News não respondidas']
    dados = [100-porcentagem, porcentagem]
    gerarGrafico(titulos, dados)

# Testa para verificar se frases que não com FN foram respondidas(o resultado deve ser o mais proximo de 0)
def testRespondeuCFN():
    raizE, raizS = retornaRaizes()
    porcentagem = 0
    total = 0
    for x in raizE:
        for y in raizS:
            if ((x.attrib['tipo'] == 'cfn' or x.attrib['tipo'] == 'cfna') and x.text == y[0].text):
                porcentagem += 1
        if(x.attrib['tipo'] == 'cfn' or x.attrib['tipo'] == 'cfna'):
            total += 1

    porcentagem = (porcentagem*100)/total
    titulos = ['Entradas com Fake News respondidas',
               'Entradas com Fake News não respondidas']
    dados = [porcentagem, 100-porcentagem]
    gerarGrafico(titulos, dados)

#
def testRespondeuCFNA():
    raizE, raizS = retornaRaizes()
    porcentagem = 0
    total = 0
    for x in raizE:
        for y in raizS:
            if ((x.attrib['tipo'] == 'cfna') and x.text == y[0].text):
                porcentagem += 1
        if(x.attrib['tipo'] == 'cfna'):
            total += 1

    porcentagem = (porcentagem*100)/total
    titulos = ['Entradas com alterações nas Fake News respondidas',
               'Entradas com alterações nas Fake News não respondidas']
    dados = [porcentagem, 100-porcentagem]
    gerarGrafico(titulos, dados)



# Teste total de frases de entrada X Saidas
# Esse teste busca saber quantos % da entradas foram respondidas de forma correta(as com e sem Fake News)
def testRespondeuCorretamenteComSemFN():
    raizE, raizS = retornaRaizes()
    porcentagemCFN = 0
    porcentagemSFN = 0
    total = 0
    totalSFN = 0
    for x in raizE:
        for y in raizS:
            if ((x.attrib['tipo'] == 'cfn' or x.attrib['tipo'] == 'cfna') and x.text == y[0].text):
                porcentagemCFN += 1
            if ((x.attrib['tipo'] == 'sfn') and x.text == y[0].text):
                porcentagemSFN += 1
        if(x.attrib['tipo'] == 'sfn'):
            totalSFN += 1
        total += 1

    porcentagem = ((porcentagemCFN +(totalSFN - porcentagemSFN))*100)/total
    titulos = ['Entradas respondida corretamente',
               'Entradas respondida de forma errada']
    dados = [porcentagem, 100-porcentagem]
    gerarGrafico(titulos, dados)

if(str(input('Gostaria de recompilar a base de saida?(s): ')).lower()=='s'):
    print('Processo iniciado')
    ms.executar()
    print('Fim do processo')


testRespondeuCorretamenteComSemFN()
testRespondeuSFN()
testRespondeuCFN()
testRespondeuCFNA()