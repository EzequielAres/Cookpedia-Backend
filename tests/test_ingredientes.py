import pytest
from app import create_app
from werkzeug.datastructures import Headers


@pytest.fixture
def client():
    app = create_app('config_tests.py')

    with app.test_client() as client:
        yield client


def test_getIngredients(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.get('/api/ingrediente', headers=headers, follow_redirects=True)
    rsp = rv.get_json()

    assert "Sal" in [d.get("nombre") for d in rsp]


def test_getIngredient(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.get("/api/ingrediente/1", headers=headers, follow_redirects=True)
    rsp = rv.get_json()

    assert "Galletas" == rsp.get("nombre")
    assert 1 == rsp.get("id")


def test_postIngrediente(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.post("/api/ingrediente/", headers=headers, follow_redirects=True, json={'nombre': 'Test'})
    rsp = rv.get_json()

    assert "Test" == rsp.get("nombre")


def test_putIngrediente(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.put("/api/ingrediente/1", headers=headers, follow_redirects=True,
                    json={'id': 1, 'nombre': 'testCambio'})
    rsp = rv.get_json()

    assert "testCambio" == rsp.get("nombre")
    assert 1 == rsp.get("id")


def test_delIngrediente(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.delete("/api/ingrediente/1", headers=headers, follow_redirects=True)
    respuesta = rv.status
    assert '204 NO CONTENT' == respuesta
