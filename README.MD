# Testes Automatizados de API — JSONPlaceholder

## Descrição

Projeto de testes automatizados para a API REST **JSONPlaceholder**, utilizando Python, Pytest e Requests.

## Tecnologias

* Python
* Pytest
* Pytest HTML
* Requests

## Execução

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute os testes e gere o relatório HTML com:

```bash
pytest
```

Ao final da execução, o relatório autocontido estará disponível em
`reports/report.html`. Ele pode ser aberto diretamente em qualquer navegador e
é atualizado a cada nova execução dos testes.

## Casos de Teste

A suíte contém 10/20 casos de teste:

### Dados válidos

* **TC-001** — Buscar post existente
* **TC-002** — Buscar usuário existente
* **TC-003** — Listar posts
* **TC-004** — Filtrar posts por usuário
* **TC-005** — Buscar comentários de um post

### Dados inválidos / inoportunos

* **TC-006** — Buscar post inexistente
* **TC-007** — Buscar usuário inexistente
* **TC-008** — Buscar post utilizando ID textual
* **TC-009** — Buscar post utilizando ID negativo
* **TC-010** — Acessar endpoint inexistente

## API utilizada

Os testes são executados utilizando a API pública:

`https://jsonplaceholder.typicode.com`

## Uso de IA

Foi utilizada Inteligência Artificial como apoio para gerar README, explicar como a API funciona e auxiliar com idéias de testes.
