#Como ponto de partida para resolução desse problema peguei um problema clássico
#que eu já tinha visto na faculdade que é o problema do menor número de troco
#Estudei esse problema e esse algoritmo na disciplina de Estrutura de Dados II, na matéria
#de programação dinâmica, tentei modificá-lo para atender a necessidade do problema de listar
#todas as possíveis moedas, mas não consegui terminar a tempo

#Consegui ter um bom caminho indo no StackOverFlow: https://stackoverflow.com/questions/1106929/how-to-find-all-combinations-of-coins-when-given-some-dollar-value?page=2&tab=scoredesc#tab-top
def InfiniteCoins(coinValueList,change):
   #Criando o set para armazenar as moedas 
   moedas = {}
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]: 
         #Aqui em cada chamada recursiva tentei colocar em um array para depois tentar transformar em set
         #Mas não consegui calcular a quantidade de cada tipo de moeda
         numCoins = 1 + InfiniteCoins(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins



print(InfiniteCoins([1,5,10,25], 12))