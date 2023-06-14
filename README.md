# Lembrete Água

Este repositório contém uma aplicação simples desenvolvida em Python para exibir notificações periódicas no sistema operacional Windows, lembrando os usuários de tomar água a cada 5 minutos. A aplicação utiliza a biblioteca win10toast para exibir as mensagens de lembrete.

## Funcionalidades

A aplicação de lembrete para tomar água inclui as seguintes funcionalidades:

- Exibir notificações a cada 5 minutos lembrando os usuários de tomar água
- Encerrar a execução da aplicação

## Requisitos

Para executar a aplicação em sua máquina local, você precisará ter os seguintes requisitos:

- Python 3.6 ou superior
- Windows

## Instalação

Siga as etapas abaixo para configurar e executar a aplicação:

1. Clone este repositório para o seu ambiente local usando o seguinte comando:

   ```
   git clone https://github.com/eduardoranucci/lembrete_agua.git
   ```

2. Navegue até o diretório raiz do projeto:

   ```
   cd lembrete_agua
   ```

3. Opcionalmente, crie e ative um ambiente virtual:

   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

5. Execute a aplicação:

   ```
   python main.py
   ```

6. A partir desse ponto, o programa irá exibir uma notificação a cada 5 minutos lembrando você de tomar água.

## Encerrando a Aplicação

Para encerrar a execução da aplicação, basta pressionar `Ctrl + C` no terminal em que ela está sendo executada.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Agradecimentos

Este projeto utiliza a biblioteca win10toast para exibir as notificações no sistema operacional Windows. Agradecemos aos desenvolvedores por disponibilizarem essa biblioteca de código aberto.
