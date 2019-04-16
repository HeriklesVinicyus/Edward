
import spacy

nlp = spacy.load('pt')
doc = nlp(u'Você encontrou o livro que eu te falei, Carla?')#Obs: você deve declarar a string como unicode para que ele funcione corretamente.
tokens = [token for token in doc]

#Primeiro, vamos analisar a frase da maneira mais simples: dividindo-a com o método split de qualquer string.
print(doc.text.split())
print([token for token in doc])

#Se não quisermos os objetos Tokens, mas sim as strings que cada Token contém podemos usar o método .orth_:
print([token.orth_ for token in doc])

#Como o spaCy entende que existe uma diferença entre uma palavra e uma pontuação, também podemos fazer filtragens. E se eu quisesse apenas as palavras da frase?
print([token.orth_ for token in doc if not token.is_punct])

#Podemos também entender as classes gramaticais de cada palavra dentro do nosso contexto:
print([(token.orth_, token.pos_) for token in doc])

# para encontrar a raiz da palavra
print('aqui',[token.lemma_ for token in doc])

#Do mesmo jeito que podemos encontrar as raízes de uma palavra, podemos checar se uma palavra é raíz de outra:
doc = nlp(u'encontrar encontrei')
tokens = [token for token in doc]
tokens[0].is_ancestor(tokens[1])

#Por fim, podemos avaliar as entidades presentes em uma frase. Por exemplo, peguemos a frase:
doc = nlp(u'Machado de Assis um dos melhores escritores do Brasil, foi o primeiro presidente da Academia Brasileira de Letras')
print(doc.ents)

