'''
import nltk
import re

frase = re.sub('[-|0-9]',' ','Isso é possível ao remover seus! afixos e vogais temáticas das palavras.')
frase = re.sub(r'[-./?!,":;()\']','',frase)
temp = []
for i in frase.split(' '):
    print (i)
    print(frase.split(' '))
    temp.append(nltk.stem.RSLPStemmer().stem(i))
print (' '.join(temp))
   #return ' '.join(temp)


import urllib.request as url

text = 'https://www.sinonimos.com.br/vacina/'

#text2 =url.urlretrieve (text , 'index.html')
#text2 =url.urlretrieve (text , 'index.html')
#text2 =url.urlretrieve (text , 'index.html')
text2 = url.urlretrieve(text,'index.html')

print(text2)
'''

'''
import requests

#função para buscar dentro de um site do sinonimos.com.br
def BuscaSinonimosDentroHTML(paginaHTML):
   ''''''
    for linha in paginaHTML.split('<p>'):
       for l in linha.split('</p>'):
          if l.find('div class="sentido"') != -1:
            for linha2 in l.split('<p'):
               for l2 in linha2.split('</p>'):
                  if l2.find('class="sinonimos"') != -1:
                     print('\n\n',buscaSinonimosLink(l2))
                        '''''''
   #print('\n\n'.join(paginaHTML.split('class="sinonimo">')))
   print('\n\n',buscaSinonimosLink(paginaHTML))

def buscaSinonimosLink(texto):
   for linha in texto.split('class="sinonimo">'):
      return linha.split('</a>')


 
r = requests.get('https://www.sinonimos.com.br/vacina/')
print('\n\n'.join(r.encoding))
print (BuscaSinonimosDentroHTML(r.text))'''
'''
import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.sinonimos.com.br/vacina/')
soup = BeautifulSoup(r.content, 'html.parser')
html = list(soup.children)[2]
body = list(html.children)[0]
print(body)
'''

'''
import requests
import xml.etree.ElementTree as et
from unicodedata import normalize




#função para buscar dentro de um site do sinonimos.com.br e joga no arquivo temp.xml
def _buscaSinonimosDentroHTML(palavra):
   temp = open('model/arquivos/temp.xml','w')
   r = requests.get('https://www.sinonimos.com.br'+palavra+'')
   if not r.ok:
      temp.write('')
      temp.close()
      return None
   esq = r.text.replace('<!DOCTYPE html>','')
   esq = esq.replace('\n','')
   esq = esq.replace('»','')
   esq = esq.replace('« ','')
   esq = esq.replace('> ','>')
   esq = esq.replace('<p','\n§<p')
   esq = esq.split('/head>')[1]
   esq = esq.split('</html>')[0]
   esq = ''.join([xml for xml in esq.split('§') if xml.find('class="sentido"')!=-1 or xml.find('class="sinonimos"')!=-1])
   esq = esq.replace('</a>, ','</a>')
   esq = esq.replace('</a>.','</a>')
   esq = esq.replace('</span>, ','</span>')
   esq = esq.replace('</span>.','</span>')
   #esq = esq.replace('</div>\n','\n')

   esq = '<sinonimos>'+esq+'</sinonimos>'
   temp.write(esq)
   temp.close()

def _retornaPalavrasComLink(raiz):
   for xml in raiz:
      if len(xml.getchildren()) > 0:
         return [i.text for i in xml.getchildren() if i.tag == 'a'], '\n'.join([i.attrib['href'] for i in xml.getchildren() if i.tag == 'a'])

def _retornaPalavrasSemlink(raiz):
   for xml in raiz:
      if len(xml.getchildren()) > 0:
         return [i.text for i in xml.getchildren() if i.tag == 'span' and i.text != 'Exemplo: ']

def _removeAcentos(palavra):
   target = normalize('NFKD', palavra).encode('ASCII','ignore').decode('ASCII')
   target = target.replace('.','')
   target = target.replace(',','')
   target = target.replace('!','')
   target = target.replace('?','')
   target = target.replace('\"','')
   return target.lower()

def _extrairPalavras():
   arquivoFN = open('model/arquivos/FN.csv','r').read()
  
   lista = [i.split('\t')[2] for i in arquivoFN.split('\n') if len(i.split('\t'))>1]
   arquivoFN = ''
   for i in lista:
      arquivoFN+= '\n'.join(i.split())
      arquivoFN+='\n'
      
   lista = [i for i in arquivoFN.split('\n')]

   return sorted(lista)

_buscaSinonimosDentroHTML('/vacina/')
arvore = et.parse('model/arquivos/temp.xml')
raiz = arvore.getroot()


print(_retornaPalavrasComLink(raiz))
'''
import requests

def _buscaSinonimosDentroHTML(palavra):
   temp = open('model/arquivos/temp.xml','w')
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
   print(esq)

_buscaSinonimosDentroHTML('/vacina/')