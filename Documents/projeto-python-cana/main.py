import json

# Função para calcular a perda percentual
def calcular_perda_percentual(toneladas_colhidas, toneladas_estimada):
    perda = ((toneladas_estimada - toneladas_colhidas) / toneladas_estimada) * 100
    return round(perda, 2)

# Função para registrar um talhão
def registrar_colheita(talhao, estimada, colhida):
    perda = calcular_perda_percentual(colhida, estimada)
    return {
        "talhao": talhao,
        "estimada": estimada,
        "colhida": colhida,
        "perda_percentual": perda
    }

# Interação com o usuário
colheitas = []

while True:
    talhao = input("Informe o nome do talhão (ou 'sair' para encerrar): ")
    if talhao.lower() == 'sair':
        break

    estimada = float(input("Informe a produção estimada (toneladas): "))
    colhida = float(input("Informe a produção colhida (toneladas): "))

    colheita = registrar_colheita(talhao, estimada, colhida)
    colheitas.append(colheita)

# Salvar os dados em JSON
with open("dados_colheita.json", "w") as arquivo_json:
    json.dump(colheitas, arquivo_json, indent=4)

# Salvar os dados em TXT
with open("dados_colheita.txt", "w", encoding="utf-8") as arquivo_txt:
    for r in colheitas:
        linha = f"Talhão: {r['talhao']}, Estimada: {r['estimada']}t, Colhida: {r['colhida']}t, Perda: {r['perda_percentual']}%\n"
        arquivo_txt.write(linha)

print("Registros salvos com sucesso!")

