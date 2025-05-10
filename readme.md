# 🖨️ Impressão Automática de Imagens com Python

### Este projeto monitora uma pasta específica no seu sistema. Sempre que uma nova imagem (`.jpg`) for adicionada, ela será automaticamente enviada para a impressora padrão **sem confirmação do usuário**.
---

## ✅ Requisitos

- Python 3.13 ou superior
- Sistema operacional Windows
- Driver da impressora Fujifilm ASK-300 instalado
- Definir a impressorar Fujifilm ASK-300 como a padrão
- Visualizador padrão de imagens com suporte a impressão silenciosa (ex: Visualizador de Fotos do Windows)

---

## 🚀 Como Executar o Projeto

2. Crie um ambiente virtual
```python -m venv venv```

3.  Ative o ambiente virtual
```venv\Scripts\activate```

4. Instale as dependências
```pip install -r requirements.txt```

5. Rodar aplicativo
```python main.py```

## Customizar pasta
```FOLDER_TO_WATCH = r"C:\Users\User\Documents\REI\pasta"```
