#Classe para converter o arquivo 'vacinas.csv' em arquivo basedados.xml tratado
arquivoVacinas = open('model/arquivos/Vacinas.csv','r')
vacinas = arquivoVacinas.read()
linhasVacinas = vacinas.split('\n')
tabelaVacinas = []

def removerEspaco(frase):
   temp = ''
   for x in frase:
      if x==' ':
         temp+='_'
         continue

      temp+=x
   return temp

def criarBaseDados(texto):
   arquivo = open('model/arquivos/baseDados.xml','w')
   arquivo.write(texto)
   arquivo.close()

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<base>\n'
for x in range(len(linhasVacinas)-1):
   if x == 0:
      continue
   tabelaVacinas.append(linhasVacinas[x].split('\t'))

for x in range(len(linhasVacinas)-2):
   #nomeSemEspaco = (removerEspaco(tabelaVacinas[x][1])).lower()
   xml+='<vacina id=\'{}\' nome=\'{}\' sigla=\'{}\' dose=\'{}\' apresentacao=\'{}\' administracao=\'{}\'>\n<composicao>\n{}\n</composicao>\n<indicacao>\n{}\n</indicacao>\n<contraidicacao>\n{}\n</contraidicacao>\n<fakenews>\n</fakenews>\n</vacina>\n'.format(tabelaVacinas[x][0],tabelaVacinas[x][1],tabelaVacinas[x][2],tabelaVacinas[x][3],tabelaVacinas[x][4],tabelaVacinas[x][6],tabelaVacinas[x][5],tabelaVacinas[x][7],tabelaVacinas[x][8])
xml+='</base>'
arquivoVacinas.close()
criarBaseDados(xml)

