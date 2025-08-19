# Exemplo: if / elif / else

entrada = input('você quer "entrar" ou "sair?"')

if entrada == 'entrar':
    print('Você escolheu entrar.')
elif entrada == 'sair':
    print('Você escolheu sair.')
else:
    print('Opção inválida.')

print('Você escolheu {}'.format(entrada))
print('Você saiu do sistema.')