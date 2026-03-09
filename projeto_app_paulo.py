'''

CRUD

barbearia

Uma barbearia funciona oferecendo serviços de corte de cabelo,barba e cuidados masculinos, organizando atendimentos por agendamento ou ordem de chegada e recebendo pagamento pelos serviços realizados. 



'''

print('Hello World!')

input('Pressione Enter para sair...')

nome_funcionario = input ('Qual é o nome do funcionario')


print(f'Olá,{nome_funcionario}! Seja bem-vindo(a) a barbearia do Paulo!')


print('nossos serviços são: corte de cabelo, barba e cuidados masculinos')

serviço = input('digite o serviço desejado')

if serviço == 'corte de cabelo':
     print('o valor do corte de cabelo é 30,00')
elif serviço == 'barba':
     print('o valor da barba é 20,00')
elif serviço == 'cuidados masculinos':
     print('o valor dos cuidados masculinos é 50,00')
else:   
    print('serviço não encontrado, por favor escolha um serviço valido')
        