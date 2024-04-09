import pytest
from app import create_app
from werkzeug.datastructures import Headers


@pytest.fixture
def client():
    app = create_app('config_tests.py')

    with app.test_client() as client:
        yield client


def test_getLikes(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.get('/api/like', headers=headers, follow_redirects=True)
    rsp = rv.get_json()

    assert 36 == len(rsp)


def test_getLike(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.get("/api/like/1", headers=headers, follow_redirects=True)
    rsp = rv.get_json()

    assert 1 == rsp.get("usuario")
    assert 1 == rsp.get("receta")
    assert 1 == rsp.get("id")


def test_postLike(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.post("/api/like", headers=headers, follow_redirects=True, json={'usuario': 1, 'receta': 3})
    rsp = rv.get_json()

    assert 1 == rsp.get("usuario")
    assert 3 == rsp.get("receta")
    assert 37 == rsp.get("id")


def test_putLike(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.put("/api/like/1", headers=headers, follow_redirects=True, json={'id': 1, 'usuario': 1, 'receta': 1})
    rsp = rv.get_json()

    assert 1 == rsp.get("usuario")
    assert 1 == rsp.get("receta")
    assert 1 == rsp.get("id")


def test_delLike(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.delete("/api/like/1", headers=headers, follow_redirects=True)
    respuesta = rv.status
    assert '204 NO CONTENT' == respuesta
