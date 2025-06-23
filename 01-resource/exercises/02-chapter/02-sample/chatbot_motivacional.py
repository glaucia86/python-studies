# chatbot_motivacional.py
# Mini projeto: Chatbot Motivacional
# Description: Um chatbot que simula um agente que responde a emoções básicas

# Entrada do usuário
mensagem = input('Com você está se sentindo hoje?')

# Deixando a mensagem sempre em minúsculas para facilitar a análise
mensagem = mensagem.lower()

# Respostas personalizadas
if 'chateado' in mensagem or 'desanimado' in mensagem or 'deprimido' in mensagem:
    resposta = 'Lembre-se: dias difíceis fazem parte, mas você é mais forte do que pensa! 🌟'
elif 'cansado' in mensagem or 'exausto' in mensagem:
    resposta = 'Descanse, se possível. Seu corpo e mente merecem cuidado! Você vai conseguir! 💪'
elif 'feliz' in mensagem or 'animado' in mensagem:
    resposta = 'Que ótimo! Continue espalhando essa energia positiva pelo mundo! 😊'
else:
    resposta = 'Estou aqui para te apoiar. Não desista dos seus sonhos, ok? 💖'

print("Chatbot Motivacional diz: " + resposta)