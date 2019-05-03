import re
import nltk
import spacy
class Pasquale:
   def __init__(self):
      self._nlp = spacy.load('pt')

   def _tratamentoNltk(self,frase):
      tempFrase = re.sub(r'[-./?!,":;()\']','',frase)
      temp = []
      for i in tempFrase.split(' '):
         temp.append(nltk.stem.RSLPStemmer().stem(i))
      return ' '.join(temp)

   def _tratamentoSpacy(self,frase):
      return (' '.join([i.lemma_ for i in self._nlp(str(frase)) if not i.is_punct])).lower()
   
   def tratadas(self, frase):
      resp = [[0,frase]]
      cont = 1
      for i in nltk.tokenize.sent_tokenize(frase):
         resp.append([cont,i])
         resp.append([cont, self._tratamentoSpacy(i)])
         resp.append([cont,self. _tratamentoNltk(i)])
         cont+=1
      return resp
