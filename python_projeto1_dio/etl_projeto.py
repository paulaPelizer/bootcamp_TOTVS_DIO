import pandas as pd

# EXTRAÇÃO

print("Iniciando a etapa de Extração...")

df = pd.read_csv('clientes.csv')
print("Dados extraídos com sucesso:\n", df)



# TRANSFORMAÇÃO

print("\nIniciando a etapa de Transformação...")

def gerar_mensagem_personalizada(linha):
    """
    Simula a transformação. Você pode usar uma lógica de negócio 
    ou integrar com a API da OpenAI/Google Gemini aqui.
    """
    nome = linha['Nome']
    saldo = float(linha['Saldo'])
    
    if saldo > 10000:
        return f"Olá, {nome}! Notamos seu excelente saldo. Que tal conhecer nossas opções de investimentos em Renda Variável?"
    elif saldo > 1000:
        return f"Olá, {nome}! Seu dinheiro pode render mais. Conheça nossos fundos de Renda Fixa de baixo risco."
    else:
        return f"Olá, {nome}! Monte sua reserva de emergência conosco. Abra uma caixinha de rendimento automático."


df['Mensagem_Marketing'] = df.apply(gerar_mensagem_personalizada, axis=1)
print("Transformação concluída!")

# CARREGAMENTO (Load)

print("\nIniciando a etapa de Carregamento...")

df.to_csv('clientes_com_mensagem.csv', index=False, sep=';', encoding='utf-8-sig')
print("Dados carregados com sucesso no arquivo 'clientes_com_mensagem.csv'!")