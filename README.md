
    
 # 🚍  Sistema de Gestão de Transporte Escolar
 OBS : **O sistema está em versão inicial, e estou implementando melhorias pouco a pouco.**   

O **Sistema de Gestão de Transporte Escolar** é uma aplicação web desenvolvida com **Django** para facilitar a administração do transporte de alunos do municipio de Guapó. Ele permite que **administradores** gerenciem motoristas, veículos, rotas e alunos, enquanto **os alunos** podem acessar seu portal para visualizar suas rotas e marcar presença.

## 📌 Funcionalidades Principais

### ✅ **Para Administradores**
- 📋 **Gerenciamento de Motoristas** (Nome, CPF, CNH, Telefone, Endereço, etc.)
- 🚐 **Gerenciamento de Veículos** (Placa, Modelo, Capacidade, Motorista vinculado)
- 🗺️ **Gerenciamento de Rotas** (Origem, Destino, Horários, Veículo e Motorista)
- 🎓 **Gerenciamento de Alunos** (Nome, Idade, Escola, Endereço, Responsável, Rota)
- 🔍 **Painel no Django Admin** para visualização rápida de presença dos alunos, motoristas, rotas e etc.

### ✅ **Para Alunos**
- 📌 **Acesso ao Portal simples para Aluno** (Login com usuário e senha)
- 📆 **Registro de Presença no Transporte Escolar**
  - **Vai e volta**
  - **Somente ida**
  - **Somente volta**
  - **Não vai e não volta**
- 🚏 **Visualização da Rota** (Origem, Destino, Horários)
- 🚌 **Informações do Veículo e Motorista**
- 🔑 **Alteração de Senha**
- 🚪 **Logout Seguro**

---

## 🛠️ **Instalação e Configuração**

### ✅ **1️⃣ Clonar o Repositório**
```bash
git clone https://github.com/seu-usuario/meu-projeto.git
```


### ✅ ** Instale e habilite o ambiente Virtual
```bash
  pip install venv
  python -m venv nome_do_ambiente
```
### ✅ ** Rode todas as depedência do projeto
```bash
pip install -r requirements.txt
```


### ✅ ** Rode a aplicação 
 
```bash
 python manage.py runserver
```

### ✅ ** Após rodar acesse o servidor : http://localhost:8080/admin


 

