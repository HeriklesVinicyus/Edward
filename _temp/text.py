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