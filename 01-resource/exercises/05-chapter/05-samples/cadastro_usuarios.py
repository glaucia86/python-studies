# Simulação de Cadastro de Usuários
# Regras
# - Nomes de usuários não podem ser repetidos (case insensitive)
# - "admin" recebe uma mensagem especial ao logar
# - O sistema mostra mensagens diferentes para sucesso ou falha no cadastro

# Lista de usuários já cadastrados no sistema
# Lista de usuários já cadastrados no sistema
current_users = ['admin', 'alice', 'joao', 'Maria', 'lucas']

print("=== Sistema de Cadastro de Usuário ===\n")
new_user = input("Digite o nome de usuário que deseja cadastrar: ")

# Checagem case-insensitive
current_users_lower = [user.lower() for user in current_users]

if new_user.lower() in current_users_lower:
    print(f"Nome de usuário '{new_user}' já está em uso. Escolha outro.")
else:
    current_users.append(new_user)
    print(f"Usuário '{new_user}' cadastrado com sucesso!")
    # Mensagem especial para admin
    if new_user.lower() == 'admin':
        print("Bem-vindo, admin! Você tem acesso privilegiado.")
    else:
        print(f"Olá, {new_user.title()}! Cadastro realizado.")

# Exibe todos os usuários cadastrados
print("\nUsuários cadastrados atualmente:")
for user in current_users:
    print("-", user)
