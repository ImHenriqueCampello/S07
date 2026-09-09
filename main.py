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
