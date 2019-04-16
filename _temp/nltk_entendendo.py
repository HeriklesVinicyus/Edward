import nltk as nt
from nltk.corpus import wordnet as wn# para trabalaho com sinonimos 
from nltk.corpus import sentiwordnet as swn #para analise de sentimentos apenas com o lema das palavras
from wordcloud import WordCloud# importe da ferramneta para gerar a nuvem de palavas
import matplotlib.pyplot as plt# ferramenta para plotar 

t = 'a vacina rotaviros faz mal! eu sei que a vacina faz mal'

#t = 'this is a test'

frases = nt.tokenize.sent_tokenize(t)

tonkens = nt.tokenize.word_tokenize(t)

classes = nt.pos_tag(tonkens)

#classes2 = nt.pos_tag_sents(frases,'eng')

entidades = nt.chunk.ne_chunk(classes)

stemmer = nt.stem.RSLPStemmer()
print(stemmer.stem('frequentemente'))
print(stemmer.stem('copiar'))

#todas as stopword portuguesa
stopword = nt.corpus.stopwords.words('portuguese')

palavras = [i for i in t.split() if not i in stopword]


print(frases)
print(tonkens)
print(classes)
#print(entidades)
#print(stopword, len(stopword))
print(palavras)
print(nt.pos_tag(palavras))
'''
print('\n',wn.synsets('car'))
print(wn.synset('bicycle.n.01').definition())
print(wn.synset('bicycle.n.01').hyponyms())# para ver o hiponinos das palavras 
print(wn.synset('bicycle.n.01').hypernyms())# para ver o hiperoninos das palavras
print(wn.synset('car.n.01').hypernyms())# para ver o hiperoninos das palavras
print(swn.senti_synset('vaccine.n.01'))
'''