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


def gerarGrafico(tituloGrafico, nomesEixos, dados):
    mp.rcParams.update({'font.size':20})
    mp.title('\n'+tituloGrafico+'\n',fontdict={'fontsize': 30})

    mp.pie(dados, labels=nomesEixos, autopct='%1.2f%%', startangle=90)
    mp.axis('equal')

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
    tituloGrafico = 'Quantidade de Frases sem FN respondidas'
    porcentagem = (porcentagem*100)/total
    titulos = ['Entradas Sem Fake News não respondidas','Entradas Sem Fake News respondidas']
    dados = [100-porcentagem,porcentagem]
    gerarGrafico(tituloGrafico, titulos, dados)

# Testa para verificar se frases que com FN foram respondidas(o resultado deve ser o mais proximo de 100%)
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

    tituloGrafico = 'Quantidade de frases com FN respondidas'
    porcentagem = (porcentagem*100)/total
    titulos = ['Entradas com Fake News respondidas',
               'Entradas com Fake News não respondidas']
    dados = [porcentagem, 100-porcentagem]
    gerarGrafico(tituloGrafico, titulos, dados)

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
    tituloGrafico = 'Quantidade de frases com FN alteradas respondidas'
    porcentagem = (porcentagem*100)/total
    titulos = ['Entradas com alterações\nnas Fake News\nrespondidas',
               'Entradas com alterações\nnas Fake News\nnão respondidas']
    dados = [porcentagem, 100-porcentagem]
    gerarGrafico(tituloGrafico, titulos, dados)



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
    tituloGrafico = 'Quantidade de frases respondidas de forma correta'
    porcentagem = ((porcentagemCFN +(totalSFN - porcentagemSFN))*100)/total
    titulos = ['Entradas respondida corretamente',
               'Entradas respondida de forma errada']
    dados = [porcentagem, 100-porcentagem]
    gerarGrafico(tituloGrafico,titulos, dados)

if(str(input('Gostaria de recompilar a base de saida?(s): ')).lower()=='s'):
    print('Processo iniciado')
    ms.executar()
    print('Fim do processo')


testRespondeuCorretamenteComSemFN()
testRespondeuSFN()
testRespondeuCFN()
testRespondeuCFNA()