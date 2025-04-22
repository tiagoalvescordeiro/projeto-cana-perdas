import json
from db import conectar_oracle



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

# Entrada interativa dos dados
colheitas = []
print("🔄 Cadastro de talhões - Controle de Perdas na Colheita da Cana-de-Açúcar")
while True:
    talhao = input("Digite o nome do talhão (ex: Talhão 1): ")
    estimada = float(input("Informe a produção estimada (em toneladas): "))
    colhida = float(input("Informe a produção colhida (em toneladas): "))

    colheitas.append(registrar_colheita(talhao, estimada, colhida))

    continuar = input("Deseja adicionar outro talhão? (s/n): ").lower()
    if continuar != 's':
        break

# Salvando no arquivo JSON
with open("projeto-cana-perdas-main\projeto-python-cana\data\10dados_colheita.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(colheitas, arquivo_json, indent=4, ensure_ascii=False)

print("✅ Registros salvos com sucesso em dados_colheita.json")

# Salvando no arquivo TXT
with open("projeto-cana-perdas-main\projeto-python-cana\data\dados_colheita.txt", "w", encoding="utf-8") as arquivo_txt:
    for r in colheitas:
        linha = f"Talhão: {r['talhao']}, Estimada: {r['estimada']}t, Colhida: {r['colhida']}t, Perda: {r['perda_percentual']}%\n"
        arquivo_txt.write(linha)

print("✅ Registros também salvos com sucesso em dados_colheita.txt")
