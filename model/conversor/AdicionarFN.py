import xml.etree.ElementTree as et
import spacy
import nltk
import re

nlp = spacy.load('pt')

arquivoXML = 'model/arquivos/baseDados.xml'
arquivoFN = open('model/arquivos/FN.csv','r')
arvore = et.parse(arquivoXML)
raiz = arvore.getroot()
textoFN = arquivoFN.read()
linhasFN = textoFN.split('\n')
tabelasFN = []

#pode ser nome ou sigla
def retornaVacina(nome):
    cont = 0
    for x in raiz:
        if nome.lower() == (x.attrib['nome']).lower() or nome.lower() == (x.attrib['sigla']).lower():
            return cont 
        cont+=1

def tratamentoNltk(frase):
   tempFrase = re.sub(r'[-./?!,":;()\']','',frase)
   temp = []
   for i in tempFrase.split(' '):
      temp.append(nltk.stem.RSLPStemmer().stem(i))

   return ' '.join(temp)
   
for x in range(len(linhasFN)-1):
   if x == 0:
      continue
   tabelasFN.append(linhasFN[x].split('\t'))

for x in tabelasFN:

   print(x)
   novaFakeNew = et.SubElement(raiz[retornaVacina(x[1])][3],'fakenew')
   fn = et.SubElement(novaFakeNew,'acusacao')
   tratada = et.SubElement(novaFakeNew,'acusacaotratadasc')
   tratada2 = et.SubElement(novaFakeNew,'acusacaotratadanlyk')
   resposta = et.SubElement(novaFakeNew,'resposta')
   fonte = et.SubElement(novaFakeNew,'fonte')
   #caso muda a estrutura dos .csv tenho que fazer muitas coisas para voltar a funcionar
   fn.text = x[2]
   tratada.text = (" ".join([i.lemma_ for i in nlp(str(x[2])) if not i.is_punct])).lower()
   tratada2.text = tratamentoNltk(x[2])
   resposta.text = x[3]
   fonte.text = x[4]

print(arquivoXML)
arvore.write(arquivoXML)
arquivoFN.close()
