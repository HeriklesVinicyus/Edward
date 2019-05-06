#Vai ate o site sinonimos e busca os sinonimos das bases de FN
import requests
import xml.etree.ElementTree as et
from unicodedata import normalize
import spacy

nlp = spacy.load('pt')

#função para buscar dentro de um site do sinonimos.com.br e joga no arquivo temp.xml
def _buscaSinonimosDentroHTML(palavra):
   temp = open('modelo/arquivos/temp.xml','w')
   r = requests.get('https://www.sinonimos.com.br'+palavra+'')
   if not r.ok:
      temp.write('')
      temp.close()
      return None
   esq = r.text.replace('<!DOCTYPE html>','')
   esq = esq.replace('\n','')
   esq = esq.replace('<p ','\n§<p ')
   esq = esq.replace('</p>','</p>\n')
   esq = ''.join([i for i in esq.split('\n') if i.find('§')!= -1])
   esq = '\n'.join([i for i in esq.split('§') if i.find('class="sinonimos"')!= -1])
   esq = esq.replace('</a>, ','</a>')
   esq = esq.replace('</a>.','</a>')
   esq = esq.replace('</span>, ','</span>')
   esq = esq.replace('</span>.','</span>')
   esq = '<sinonimos>'+esq+'</sinonimos>'
   temp.write(esq)
   temp.close()

def _retornaPalavrasComLink(raiz, id):
   for xml in raiz:
      if len(xml.getchildren()) > 0:
         return [i.text+'|'+str(id) for i in xml.getchildren() if i.tag == 'a'], '\n'.join([i.attrib['href'] for i in xml.getchildren() if i.tag == 'a'])

def _retornaPalavrasSemlink(raiz, id):
   for xml in raiz:
      if len(xml.getchildren()) > 0:
         return [i.text+'|'+str(id) for i in xml.getchildren() if i.tag == 'span' and i.text != 'Exemplo: ']

def _removeAcentos(palavra):
   target = normalize('NFKD', palavra).encode('ASCII','ignore').decode('ASCII')
   target = target.replace('.','')
   target = target.replace(',','')
   target = target.replace('!','')
   target = target.replace('?','')
   target = target.replace('\"','')
   return target.lower()

def _extrairPalavrasBaseFN():
    arquivoFN = open('modelo/arquivos/info/FN.csv','r')
    FN = arquivoFN.read()
    
  
    lista = [i.split('\t')[2] for i in FN.split('\n') if len(i.split('\t'))>1]
    FN = ''
    for i in lista:
        FN+= '\n'.join(i.split())
        FN+='\n'
        
    lista = [i for i in FN.split('\n') if len(i)>0]
    temp = []
    for i in lista:
        if '1234567890'.find(i)==-1:
            temp+=[i.lemma_ for i in nlp(str(i)) if not i.is_punct]

    lista = temp
    arquivoFN.close()           
    return sorted(set(lista))

def _criarDicionarioSinonimos():
    lista = _extrairPalavrasBaseFN()
    lista = ['/'+_removeAcentos(i)+'/' for i in lista]
    temp = []
    #text = ''
    palavrasSemSinonimos = ''
    id = 0
    for i in lista:
        _buscaSinonimosDentroHTML(i)
        raiz = ''
        try:
            arvore = et.parse('modelo/arquivos/temp.xml')
            raiz = arvore.getroot()
        except et.ParseError:
            palavrasSemSinonimos+=i
            continue
        aux = _retornaPalavrasComLink(raiz,i.replace('/',''))
        temp+= aux[0]
        #usado para buscar sinonimos dos sinonimos(não em uso)
        #text += aux[1]
        temp+=_retornaPalavrasSemlink(raiz,i.replace('/',''))
        id+=1
    #print(palavrasSemSinonimos)
    return '\n'.join(temp)

def _atualizarBaseSinonimos():
   todosSinonimos = _criarDicionarioSinonimos()
   base = open('modelo/arquivos/bases/baseSinonimos.txt','w')
   base.write(todosSinonimos)

_atualizarBaseSinonimos()