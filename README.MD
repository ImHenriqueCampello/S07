# Testes Automatizados de API — JSONPlaceholder

## Descrição

Projeto de testes automatizados para a API REST **JSONPlaceholder**, utilizando Python, Pytest e Requests.

## Tecnologias

* Python
* Pytest
* Requests

## Execução

Instale as dependências:

```bash
pip install pytest requests
```

Execute os testes com:

```bash
pytest
```

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
