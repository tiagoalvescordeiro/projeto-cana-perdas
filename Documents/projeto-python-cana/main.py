import json

# Função para calcular a perda percentual
def calcular_perda_percentual(toneladas_colhidas, toneladas_estimadas):
    perda = ((toneladas_estimadas - toneladas_colhidas) / toneladas_estimadas) * 100
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

# Simulação de dados
colheitas = [
    registrar_colheita("Talhão 1", 100, 85),
    registrar_colheita("Talhão 2", 120, 100),
    registrar_colheita("Talhão 3", 90, 70)
]

# Salvando no arquivo JSON
with open("dados_colheita.json", "w") as arquivo_json:
    json.dump(colheitas, arquivo_json, indent=4)

print("Registros salvos com sucesso em dados_colheita.json")
# Salvando em arquivo TXT
with open("dados_colheita.txt", "w", encoding="utf-8") as arquivo_txt:
    for r in colheitas:
        linha = f"Talhão: {r['talhao']}, Estimada: {r['estimada']}t, Colhida: {r['colhida']}t, Perda: {r['perda_percentual']}%\n"
        arquivo_txt.write(linha)

print("Registros também salvos com sucesso em dados_colheita.txt")

