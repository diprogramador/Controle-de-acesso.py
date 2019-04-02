# Controle-de-acesso.py
#recolhe dados de usuários de certa empresa


def registro_unico():
    import time

    relogio = time.localtime()

    print(relogio.tm_mday,"/", relogio.tm_mon,"/", relogio.tm_year)  
    print(relogio.tm_hour ,":", relogio.tm_min ,":", relogio.tm_sec )

    n = input("Digite seu nome: ")
    i = int(input("Digite sua idade: "))
    e = input("Digite seu endereço: ")
    
    print('\n---------------------+------------------+-------------------+----------------')
    print("\nOlá" ,n,'!' , "\nSua idade é:" , i ,'anos' '.' , "\nSeu endereço é:" ,e ,'.')
    
print('\n---------------------+------------------+-------------------+----------------\n')

controle = ''
while (controle != 's'):
	print('c. Registrar novamente', registro_unico())
	print('s. Sair')
	controle = input('Digite a opção desejada: ')
print('Loop encerrado!')



