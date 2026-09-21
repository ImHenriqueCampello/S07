# Testes Automatizados de API — JSONPlaceholder

## Descrição

Projeto de testes automatizados para a API REST **JSONPlaceholder**, utilizando Python, Pytest e Requests.

## Tecnologias

- Python
- Pytest
- Pytest HTML
- Requests

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

A suíte contém 25 casos de teste:

### Dados válidos

- **TC-001** — Buscar post existente
- **TC-002** — Buscar usuário existente
- **TC-003** — Listar posts
- **TC-004** — Filtrar posts por usuário
- **TC-005** — Buscar comentários de um post
- **TC-011** — Criar novo post
- **TC-012** — Atualizar completamente um post existente
- **TC-013** — Atualizar parcialmente um post
- **TC-014** — Buscar fotos de um álbum
- **TC-015** — Buscar tarefas de um usuário
- **TC-021** — Excluir post existente
- **TC-022** — Buscar álbum existente
- **TC-023** — Filtrar tarefas concluídas
- **TC-024** — Filtrar comentários por post
- **TC-025** — Buscar álbuns de um usuário

### Dados inválidos / inoportunos

- **TC-006** — Buscar post inexistente
- **TC-007** — Buscar usuário inexistente
- **TC-008** — Buscar post utilizando ID textual
- **TC-009** — Buscar post utilizando ID negativo
- **TC-010** — Acessar endpoint inexistente
- **TC-016** — Tentar criar recurso diretamente em ID existente
- **TC-017** — Atualizar post sem informar o ID do recurso
- **TC-018** — Atualizar parcialmente um post sem informar o ID
- **TC-019** — Excluir post sem informar o ID
- **TC-020** — Enviar JSON malformado

## API utilizada

Os testes são executados utilizando a API pública:

`https://jsonplaceholder.typicode.com`

## Uso de IA

Foi utilizada Inteligência Artificial como apoio para:

- Gerar README.md e plano de testes;
- Auxiliar no entendimento da estrutura e funcionamento da API utilizada;
- Ideias de testes
