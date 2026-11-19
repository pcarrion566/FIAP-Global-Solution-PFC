# Neighborhood Action Dashboard - Global Solution

## Identificação da Equipe
* **RM 576700**
* **Integrante:** Pedro Fattorelli Carrion

## Descrição do Projeto
O **Neighborhood Action Dashboard** é um protótipo funcional desenvolvido em linguagem Python, operando via interface textual no terminal. O sistema simula um painel comunitário voltado para o registro, organização, consulta e acompanhamento de ocorrências e demandas urbanas em bairros e comunidades (como iluminação pública, acessibilidade, limpeza urbana e conservação de espaços coletivos).

## Estruturas de Dados Utilizadas e Justificativa
* **Lista (`list`):** Empregada para armazenar o conjunto completo de ocorrências cadastradas, permitindo percorrer sequencialmente os registros para listagens gerais.
* **Dicionário (`dict`):** Utilizado para mapear o identificador único (ID) de cada ocorrência aos seus respectivos dados, garantindo buscas diretas e eficientes sem varredura linear.
* **Fila (FIFO - *First In, First Out*):** Organiza as demandas recém-abertas que ainda não foram examinadas pela equipe de atendimento, respeitando a ordem cronológica de chegada.
* **Pilha (LIFO - *Last In, First Out*):** Utilizada para registrar e rastrear o histórico de atualizações e eventos recentes do sistema, permitindo consultar a última modificação realizada.
* **Matriz / Lista de Listas:** Sintetiza e cruza quantitativamente as ocorrências por categoria e situação atual, exibindo uma tabela consolidada no painel de indicadores.

## Regras Lógicas e Validações
O sistema emprega estruturas condicionais (`if`, `elif`, `else`) associadas a operadores lógicos (`and`, `or`, `not`) para validar entradas e restringir dados inconsistentes.
* **Expressão Booleana de Validação:**
`if not cat or not stat or (cat not in CATEGORIAS_VALIDAS) or (stat not in SITUACOES_VALIDAS):`
Esta regra impede o cadastro ou alteração de ocorrências com campos obrigatórios vazios ou categorias/status desconhecidos.

## Indicadores Implementados
O painel de indicadores calcula automaticamente:
1. **Totais e Proporções:** Quantidade absoluta e percentual de ocorrências por cada situação (*aberta*, *em análise*, *concluída*).
2. **Matriz Cruzada:** Distribuição quantitativa das demandas por categoria em função do seu status atual.
3. **Métrica Operacional:** Contagem de pendências na fila de triagem e o topo da pilha de histórico.

## Instruções de Execução
Para executar a aplicação em seu terminal, certifique-se de ter o Python instalado e utilize o comando na raiz do projeto:
```bash
python src/sistema.py
