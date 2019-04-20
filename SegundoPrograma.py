import requests 

#r = requests.get("https://braziliex.com/api/v1/public/ticker/eth_btc")    
#print(r.text)

Nome = "Dilmo"
Idade = 33

# Teste de Impressao utilizando a Variavel
Frase = '1 - Meu nome é ' + Nome + ' e tenho ' + str(Idade) + ' anos de idade!'
print(Frase)

# Teste de Impressao direto
print("2 - Meu nome é",Nome,"e tenho",Idade,"anos de idade!")

# Assim não funciona!
#print "3 - Meu nome é"

#==========================================================================

a=1
b='ball'

#Method 1:
print('I have %d %s' %(a,b))

#Method 2:
print('I have',a,b)

#Method 3:
print('I have {} {}'.format(a,b))

#Method 4:
print('I have ' + str(a) +' ' +b)

##
# Agora estou testando!!!

#Vou mudar de novo!
#

#Agora esta direto para o GitHub Remoto
