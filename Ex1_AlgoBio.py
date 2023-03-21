''' Ex_1 Contar nucleotídeos A T C G de uma sequência
Brenda Uemura                        AlgoBio - 2023.1'''

sequencia = input("Insira a sequência a ser analisada: \n")

#CONTAGEM INDIVIDUAL DOS NUCLEOTIDOS DA SEQUENCIA
a = sequencia.count('A')       
c = sequencia.count('C')
g = sequencia.count('G')
t = sequencia.count('T')

print("A:", a)
print("C:", c)
print("G:", g)
print("T:", t)

#SOMATORIA DOS NUCLEOTIDEOS 
s = a+c+g+t                  
print("Total de nucleotídeos:", s)
