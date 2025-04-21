# 📊 Projeto: Controle de Perdas na Colheita da Cana-de-Açúcar

## 🌱 Contexto
A colheita da cana-de-açúcar, especialmente a mecanizada, pode gerar perdas significativas — chegando a até 15% da produção. Este sistema foi desenvolvido para auxiliar produtores e gestores do agronegócio a registrar, calcular e acompanhar as perdas durante a colheita, permitindo uma análise mais precisa e ações corretivas.

## 🎯 Objetivo
Criar uma aplicação em Python para:
- Calcular a perda percentual entre a produção estimada e a efetivamente colhida.
- Registrar os dados por talhão.
- Armazenar os registros em arquivos `.json` e `.txt`.
- Possibilitar entrada interativa dos dados via terminal.

## 🛠️ Tecnologias e conceitos aplicados
- Python 3.13
- Funções com passagem de parâmetros
- Estruturas de dados: listas, dicionários
- Manipulação de arquivos `.txt` e `.json`
- Interface interativa via terminal (input do usuário)

## ▶️ Como executar o projeto

1. Certifique-se de ter o Python instalado (versão 3.10 ou superior).
2. Faça o download ou clonagem do repositório.
3. Execute o script `main.py` com o comando:

   ```bash
   python main.py
   ```

4. **Siga o menu interativo** para registrar os dados dos talhões:
   - Informe o nome do talhão
   - Informe a produção estimada (em toneladas)
   - Informe a produção colhida (em toneladas)
   - O sistema calculará automaticamente a perda percentual
   - Você pode adicionar quantos talhões quiser

5. Ao final, dois arquivos serão gerados na pasta:
   - `dados_colheita.json` → formato estruturado em JSON
   - `dados_colheita.txt` → relatório simples em texto

## 🧪 Exemplo de saída em JSON

```json
[
  {
    "talhao": "Talhão 1",
    "estimada": 100,
    "colhida": 85,
    "perda_percentual": 15.0
  }
]
```

## 👨‍💻 Autores
- Tiago Alves Cordeiro - RM561791  
- Edson Henrique Felix Batista - RM566321  
- Matheus Parra - RM561907

---

📚 Projeto desenvolvido para a disciplina de **Gestão do Agronegócio em Python** (Cap. 3 ao 6) | FIAP 2025
