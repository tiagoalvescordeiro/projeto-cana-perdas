import json
import os
from db import conectar_oracle

# Função para calcular a perda percentual
def calcular_perda_percentual(toneladas_colhidas, toneladas_estimadas):
    perda = ((toneladas_estimadas - toneladas_colhidas) / toneladas_estimadas) * 100
    return round(perda, 2)

# Função para registrar um talhão
def registrar_colheita(cultura_escolhida, talhao, estimada, colhida):
    perda = calcular_perda_percentual(colhida, estimada)
    return {
        "cultura":cultura_escolhida,
        "talhao": talhao,
        "estimada": estimada,
        "colhida": colhida,
        "perda_percentual": perda
    }

# Função para entrada de dados com validação
def entrada_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("❌ Entrada inválida! Digite um número.")

# Função para salvar em JSON
def salvar_json(colheitas, caminho):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(colheitas, f, indent=4, ensure_ascii=False)
    print("Registros salvos com sucesso em JSON.")

# Função para salvar em TXT
def salvar_txt(colheitas, caminho):
    with open(caminho, "w", encoding="utf-8") as f:
        for r in colheitas:
            linha = f"Cultura: {r['cultura']}, Talhão: {r['talhao']}, Estimada: {r['estimada']}t, Colhida: {r['colhida']}t, Perda: {r['perda_percentual']}%\n"
            f.write(linha)
    print(" Registros salvos com sucesso em TXT.")


def exibir_menu_culturas():
    culturas = ["Milho", "Soja", "Cana-de-açúcar", "Café"]
    
    print("Selecione a cultura agrícola:")
    for i, cultura in enumerate(culturas, start=1):
        print(f"{i}. {cultura}")
    
    while True:
        try:
            escolha = int(input("Digite o número da cultura: "))
            if 1 <= escolha <= len(culturas):
                print(f"Você selecionou: {culturas[escolha - 1]}")
                return culturas[escolha - 1]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")




# Menu interativo
def menu():
    colheitas = []
    print(" Cadastro de Talhões - Controle de Perdas na Colheita da Cana")

    while True:
        cultura_escolhida = exibir_menu_culturas()

        talhao = input("Digite o nome do talhão (ex: Talhão 1): ")
        estimada = entrada_float("Informe a produção estimada (em toneladas): ")
        colhida = entrada_float("Informe a produção colhida (em toneladas): ")

        colheitas.append(registrar_colheita(cultura_escolhida,talhao, estimada, colhida))

        continuar = input("Deseja adicionar outro talhão? (s/n): ").lower()
        if continuar != 's':
            break

    # Caminhos de arquivos
    pasta = os.path.join("data")
    os.makedirs(pasta, exist_ok=True)

    caminho_json = os.path.join(pasta, "dados_colheita.json")
    caminho_txt = os.path.join(pasta, "dados_colheita.txt")

    salvar_json(colheitas, caminho_json)
    salvar_txt(colheitas, caminho_txt)

if __name__ == "__main__":
    menu()
