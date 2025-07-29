# SistemaSimplesBanco

Sistema Bancário Simples em Python
Bem-vindo ao Sistema Bancário Simples! Este é um projeto desenvolvido em Python para simular operações bancárias básicas como depósito, saque e visualização de extrato. O sistema inclui funcionalidades para gerenciar o saldo, registrar todas as transações com data e hora (horário do Brasil), e aplicar limites de saque por operação e diários.

Funcionalidades
Depósito: Adiciona um valor ao saldo da conta.

Saque: Retira um valor do saldo, respeitando um limite de R$ 500,00 por operação e um limite de 3 saques diários.

Extrato: Exibe todas as movimentações (depósitos e saques) realizadas na conta, com a data e hora de cada transação, e o saldo atual.

Como Usar o Sistema
Para executar e interagir com o sistema, siga os passos abaixo:

Pré-requisitos:

Certifique-se de ter o Python 3 instalado em sua máquina. Você pode baixá-lo em python.org.

Este projeto utiliza o módulo pytz para lidar com fusos horários. Se você não o tem, instale-o via pip:

Bash

pip install pytz
Baixe o Projeto:

Você pode clonar este repositório para sua máquina local usando Git:

Bash

git clone https://github.com/Guilhermebackend/SistemaSimplesBanco.git


Execute o Programa:

Abra seu terminal ou prompt de comando.

Navegue até a pasta onde você salvou o arquivo sistema_bancario.py.

Execute o script Python:

Bash

python sistema_bancario.py
Interaja com o Menu:
Após executar o programa, um menu de opções será exibido:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
Digite d e pressione Enter para Depositar.

Digite s e pressione Enter para Sacar.

Digite e e pressione Enter para visualizar o Extrato.

Digite q e pressione Enter para Sair do sistema.

Limitações e Observações
O sistema é simples e não possui persistência de dados. Isso significa que, ao fechar o programa, todo o saldo e extrato serão perdidos.

O limite de saque é de R$ 500,00 por operação.

Você pode realizar um máximo de 3 saques por dia. O contador de saques é zerado à meia-noite (horário de São Paulo).

Valores negativos ou zero não são aceitos para depósito ou saque.

Contribuição
Este projeto foi criado com fins didáticos. Sinta-se à vontade para explorar o código, fazer melhorias ou adicionar novas funcionalidades!

Agradecemos por usar o nosso Sistema Bancário Simples! Esperamos que seja útil para entender os conceitos básicos de programação e operações bancárias.
