import calculos
import math

#Coisas básicas
#nome = input('Digite o seu nome:')
#idade = int(input('Digite o sua idade:'))
#if(idade > 20):
#    print('%s é o meu e tenho %d anos e sou velho' % (nome,idade))
#elif(idade <= 20):
#    print('%s é o meu e tenho %d anos e sou novo' % (nome,idade))

# Matriz
#Lista = [1,[3,2,5,4],3,4,5,6,7,8]
#Lista[1][2] = 2
#print(Lista[1][2])

#Ciclo de repetição
#i = 0
#while(len(Lista) > i):
#    print(Lista[i])
#    i+=1;

# Ponteiros e listas
#lista1 = [1,2,3,4,5]
#lista2 = lista1
#lista2[0] = 10
#print(lista1)
#lista3 = [1,2,3,4,5]
#lista4 = lista3[:]
#lista3.append(10)
#lista3.pop(1)
#lista3.remove(10)
#lista4[0] = 10
#print(lista3)

#FOR
#lista = [1,2,3,4]
#for i in lista:
#    if i == lista[3]:
#        print(i)
#        break
#nome = 'python'
#for letra in nome:
#    print(letra, end=' ')

# tuplas - elementos imutáveis
#tupla = (1,2,3,4)
#print(tupla.index(4))

# Conjuntos
#s1 = set()
#s1.add(10)
#s1.add(20)
#s1.add(30)
#print(s1)
#s2 = set()
#s2.add(20)
#s2.add(30)
#s2.add(40)
#s2.add(50)
#s2.add(60)
#s2.add(70)
#print(s2)
#uniao = s1.union(s2)
#print(uniao)
#inter = s1.intersection(s2)
#print(inter)
#diff = s1.difference(s2)
#print(diff)
#Para remover a repetição de uma lista é só adicionar a lista no conjunto

#Dicionários
# Esquema de chave e valor
#Mateus = {'Idade':20, 'Time':'Brasil', 'Jogo':'God of war'}
#print(Mateus)
#print(Mateus['Jogo'])
#Mateus['Refeição'] = 'Feijoada'
#print(Mateus['Refeição'])
#print(Mateus.items())
#print(Mateus.keys())
#print(Mateus.values())
#print('Jogo' in Mateus)
#print('Good of war' in Mateus)

#Função
#def somar(n1,n2):
#    return n1+n2
#def eh_par(x):
#    return x % 2 == 0
#def foo(*args):
#    return sum(*args)
#def fat(n):
#    if n == 0 or n ==1:
#        return 1
#    return n * fat(n - 1)
#def imprimir_nome(nome='desconhecido'):
#    print(nome)
#def somar3(x,y,z,f):
#    return x + f(y,z)
#def f(n1, n2):
#    return n1+n2
#print(somar3(10,20,30,f))
#imprimir = print
#imprimir('hello world')
#imprimir_nome()
#a = lambda x: x*2
#print(a(4))

#Metodos
#print(calculos.area_quad(5))
#print(calculos.peri_quad(5))
#print(calculos.area_ret(2,4))

#Abrir arquivo
#with open('dataset.txt', 'r') as f:
#    lista = f.read().splitlines()
#    print(lista[3])


### Orientação a objetos ###

#help(str)

#class pessoa:

#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade
        
#    def EscreverNome(self):
#        print(self.nome)
    
#    def EscreverIdade(self):
#        print(self.idade)

#p = pessoa('Mateus',20)
#p.EscreverNome()
#p.EscreverIdade()

#class Conta:

#    def __init__(self, cliente, numero):
#        self.cliente = cliente
#        self.numero = numero

#class ContaEspecial(Conta):

#    def __init__(self, cliente, numero, limite=0):
#        Conta.__init__(self,cliente, numero)
#        self.limite = limite

#especial = ContaEspecial('Mateus', '123456', 1200)
#conta = Conta('Mateus','125847532')

#print(especial.limite)
#print(conta.numero)


# Lambda define funções anonimas

#dobro = lambda x: x * 2
#dobro(3)

#soma = lambda x, y: x + y
#soma(10,20)

#lista = [1,2,3,4,5,6,7,8,9,10]
#novalista = list(filter(lambda x: x % 2 == 0, list(map(lambda x: x*2, lista))))
#print(novalista)