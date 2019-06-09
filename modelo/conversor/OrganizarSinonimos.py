#Quarta a ser execuldata Essa classe trabalha com a base de sinônimos removendo redundâncias e incongruências 

import spacy
nlp = spacy.load('pt')

def _retornarIndicesSemrepedicoes(sinonimos):
    resp = [sinonimos[0]]
    for i in sinonimos:
        cont = 0
        for j in resp:
            if i == j:
                cont+=1
                break
        if cont == 0:
            resp.append(i)
            
    resp.sort()
    return resp


arquivoSinonimos = open('modelo/arquivos/bases/baseSinonimos.txt')
sinonimos = arquivoSinonimos.read()
sinonimosIndices = [[i.split('|')[0],i.split('|')[1]] for i in sinonimos.split('\n')]
sinonimosIndices = _retornarIndicesSemrepedicoes(sinonimosIndices)
temp = '\n'.join([i[0].lower()+'|'+i[1].lower() for i in sinonimosIndices])

arquivoSinonimos.close()
arquivoSinonimos = open('modelo/arquivos/bases/baseSinonimos.txt','w')
arquivoSinonimos.write(temp)
arquivoSinonimos.close()