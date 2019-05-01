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
      resp = []
      resp.append(self._tratamentoSpacy(frase))
      resp.append(self. _tratamentoNltk(frase))
      return resp

classe = Pasquale()
test = 'A Vacina contra o HPV incentiva o sexo sem preservativo'
tratada = classe.tratadas(test)
print(tratada)