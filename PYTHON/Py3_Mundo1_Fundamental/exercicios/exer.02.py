# 2 Crie um programa que leia:
# A data de nascimeto de uma pessoa e mostre uma mensagem com a data formatada.
#-----------------------------------------------------------------------------#
print()
print('=-='*20)
n = input ('digite seu nome: ')
d = input ('Digite o dia em que nasceu: ')
m = input ('Digite o mês em que nasceu: ')
a = input ('Digite o ano em que nasceu: ')
print ('Ola',n,'Você naceu no dia',d,'Mês', m,'ano',a,'Está correto?')
print ('Ola {}, você nasceu no dia {}, do mês {}, do ano de {}, está correto?'.format(n,d,m,a))
print('=-='*20)
print()