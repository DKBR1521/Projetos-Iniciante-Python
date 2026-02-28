# Calculadora de Juros (Simples e Compostos) 💰

Este script em Python foi desenvolvido para facilitar o cálculo de rendimentos financeiros, permitindo ao usuário alternar entre juros simples e compostos em uma única interface de terminal.

## 🚀 Funcionalidades
- **Cálculo Duplo:** Suporte para Juros Simples ($J = C \cdot i \cdot t$) e Juros Compostos ($M = C \cdot (1 + i)^t$).
- **Conversão Automática:** O programa ajusta o tempo (Dias, Meses, Anos) automaticamente para bater com a unidade da taxa informada.
- **Navegação Amigável:** Comandos `exit` para encerrar e `back` para reiniciar o fluxo a qualquer momento.
- **Tratamento de Erros:** Validação de entradas numéricas com `try/except` para evitar fechamentos inesperados.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Conceitos:** Loops (`while`), Condicionais (`if/elif`), Tratamento de Exceções e Formatação de Strings.

## 📈 Exemplo de Uso
O usuário define o Capital, a Taxa (ex: 2% ao mês) e o Tempo (ex: 1 ano). O script converte o tempo para 12 meses e entrega o Juro e o Montante final formatados com duas casas decimais.

(Projeto Inicial)
