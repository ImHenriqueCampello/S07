import pytest
import requests


# ============================================================
# FIXTURES
# ============================================================

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


# ============================================================
# TESTES - DADOS VÁLIDOS
# ============================================================

# TC-001 | GET | Buscar post existente
def test_tc_001_buscar_post_existente(base_url):
    response = requests.get(f"{base_url}/posts/1")

    assert response.status_code == 200


# TC-002 | GET | Buscar usuário existente
def test_tc_002_buscar_usuario_existente(base_url):
    response = requests.get(f"{base_url}/users/1")

    assert response.status_code == 200


# TC-003 | GET | Listar posts
def test_tc_003_listar_posts(base_url):
    response = requests.get(f"{base_url}/posts")

    assert response.status_code == 200


# TC-004 | GET | Filtrar posts por usuário
def test_tc_004_filtrar_posts_por_usuario(base_url):
    response = requests.get(
        f"{base_url}/posts",
        params={"userId": 1}
    )

    assert response.status_code == 200


# TC-005 | GET | Buscar comentários de um post
def test_tc_005_buscar_comentarios(base_url):
    response = requests.get(f"{base_url}/posts/1/comments")

    assert response.status_code == 200

# TC-011 | POST | Criar novo post
def test_tc_011_criar_novo_post(base_url):
    payload = {
        "title": "Teste automatizado",
        "body": "Conteudo criado pelo pytest",
        "userId": 1
    }

    response = requests.post(
        f"{base_url}/posts",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


# TC-012 | PUT | Atualizar completamente um post existente
def test_tc_012_atualizar_post_put(base_url):
    payload = {
        "id": 1,
        "title": "Titulo atualizado",
        "body": "Conteudo atualizado",
        "userId": 1
    }

    response = requests.put(
        f"{base_url}/posts/1",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


# TC-013 | PATCH | Atualizar parcialmente um post
def test_tc_013_atualizar_parcialmente_post(base_url):
    payload = {
        "title": "Titulo alterado via PATCH"
    }

    response = requests.patch(
        f"{base_url}/posts/1",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]


# TC-014 | GET | Buscar fotos de um álbum
def test_tc_014_buscar_fotos_album(base_url):
    response = requests.get(
        f"{base_url}/albums/1/photos"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for foto in data:
        assert foto["albumId"] == 1


# TC-015 | GET | Buscar tarefas de um usuário
def test_tc_015_buscar_tarefas_usuario(base_url):
    response = requests.get(
        f"{base_url}/users/1/todos"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for tarefa in data:
        assert tarefa["userId"] == 1


# ============================================================
# TESTES - DADOS INVÁLIDOS / INOPORTUNOS
# ============================================================

# TC-006 | GET | Buscar post inexistente
def test_tc_006_post_inexistente(base_url):
    response = requests.get(f"{base_url}/posts/99999999")

    assert response.status_code == 404


# TC-007 | GET | Buscar usuário inexistente
def test_tc_007_usuario_inexistente(base_url):
    response = requests.get(f"{base_url}/users/99999999")

    assert response.status_code == 404


# TC-008 | GET | ID textual
def test_tc_008_id_textual(base_url):
    response = requests.get(f"{base_url}/posts/abc")

    assert response.status_code == 404


# TC-009 | GET | ID negativo
def test_tc_009_id_negativo(base_url):
    response = requests.get(f"{base_url}/posts/-1")

    assert response.status_code == 404


# TC-010 | GET | Endpoint inexistente
def test_tc_010_endpoint_inexistente(base_url):
    response = requests.get(f"{base_url}/endpoint-inexistente")

    assert response.status_code == 404

# TC-016 | POST | Tentar criar recurso diretamente em ID existente
def test_tc_016_post_em_recurso_especifico(base_url):
    payload = {
        "title": "Post invalido",
        "body": "Operacao realizada em endpoint incorreto",
        "userId": 1
    }

    response = requests.post(
        f"{base_url}/posts/3",
        json=payload
    )

    assert response.status_code == 404


# TC-017 | PUT | Atualização sem informar ID do recurso
def test_tc_017_put_sem_id(base_url):
    payload = {
        "title": "Titulo atualizado",
        "body": "Conteudo atualizado",
        "userId": 1
    }

    response = requests.put(
        f"{base_url}/posts",
        json=payload
    )

    assert response.status_code == 404


# TC-018 | PATCH | Atualização parcial sem informar ID
def test_tc_018_patch_sem_id(base_url):
    payload = {
        "title": "Titulo alterado"
    }

    response = requests.patch(
        f"{base_url}/posts",
        json=payload
    )

    assert response.status_code == 404


# TC-019 | DELETE | Exclusão sem informar ID
def test_tc_019_delete_sem_id(base_url):
    response = requests.delete(
        f"{base_url}/posts"
    )

    assert response.status_code == 404


# TC-020 | POST | Enviar JSON malformado
def test_tc_020_json_malformado(base_url):
    headers = {
        "Content-Type": "application/json"
    }

    # JSON propositalmente inválido:
    # possui vírgula antes do fechamento da chave
    payload_invalido = """
    {
        "title": "Teste JSON invalido",
        "body": "Conteudo de teste",
        "userId": 1,
    }
    """

    response = requests.post(
        f"{base_url}/posts",
        data=payload_invalido,
        headers=headers
    )

    assert response.status_code == 500