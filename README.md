# 📝 Ponteiro &middot; ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Logo](documentos/logo.png)
- Gerenciamento remoto de presença
- Monitoramento remoto de atividade e produtividade
- Local para interação com grupos de trabalho
<hr/>

## 📖 Uma breve história
A proposta do projeto Ponteiro foi de criar um sistema simples para gerenciar o horário de entrada e saída de um usuário em determinado grupo, e registrar os períodos de atividade durante estes intervalos. Ele surgiu como ideia para um trabalho de segundo semestre da faculdade de Análise e Desenvolvimento de Sistemas, no Instituto Federal de São Paulo, pela matéria de Estrutura de Dados. 

## 🖥️ Como usar
1. Instale as [ferramentas utilizadas](#-ferramentas-utilizadas) através do pip (recomendável o uso de um ambiente virtual)
2. Abra a pasta Ponteiro em projeto_Django
3. Execute o sistema no terminal por meio do comando ``` python manage.py runserver ```
4. Acesse a porta ``` localhost:8000/ponteiro ``` em um navegador de sua preferência
5. Agora o sistema está pronto para ser utilizado, em nossa interface, você encontrará funções para:
   
     - Realizar cadastro
     - Realizar login
     - Buscar, editar ou apagar contas
     - Criar, editar, apagar ou entrar em grupos
     - Alterar o idioma da interface
     - Alterar o tema da interface
     - Registrar a presença no grupo
     - Solicitar relatórios de presença
    #### 🚧 (Em construção)
    - Enviar e receber mensagens
    - Enviar e receber pedidos de amizade
    - Enviar e receber solicitações de entrada em grupo
    - Receber notificações
    - Implementação de uma ferramenta para gerenciamento de atividade/produtividade
    - Geração de relatórios mais detalhados

### 🔧 Ferramentas utilizadas
- Python 3.11.15
- Django 5.0.4
- Pillow 10.3.0
- Openpyxl 3.1.2
