import io

import pytest
from app import create_app
from werkzeug.datastructures import Headers


@pytest.fixture
def client():
    app = create_app('config_tests.py')

    with app.test_client() as client:
        yield client


def test_getUsers(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.get('/api/usuario', headers=headers, follow_redirects=True)
    rsp = rv.get_json()
    assert len(rsp) == 5
    assert "Ezequiel" in [d.get("nombre") for d in rsp]


def test_getUser(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.get("/api/usuario/1", headers=headers, follow_redirects=True)
    rsp = rv.get_json()
    assert "Ezequiel" == rsp.get("nombre")
    assert 1 == rsp.get("id")
    assert "ezequiel@gmail.com" == rsp.get("email")
    assert True is rsp.get("is_admin")
    assert "Zzequi" == rsp.get("nick")


def test_postUser(client):
    data = {'nombre': 'Antonio', 'email': 'antoñete@ejemplo.com', 'hashed_password': 'pestillo', 'nick': 'Antoñete',
            'imagen': (io.BytesIO(b"abcdef"), 'test.jpg')}

    rv = client.post("/api/usuario/", follow_redirects=True,
                     data=data, content_type='multipart/form-data')
    rsp = rv.get_json()

    assert "Antoñete" == rsp.get("nick")
    assert 6 == rsp.get("id")
    assert "antoñete@ejemplo.com" == rsp.get("email")
    assert False is rsp.get("is_admin")
    assert "Antonio" == rsp.get("nombre")


def test_putUser(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    data = {'id': 1, 'email': 'ezequielCambio@ejemplo.com', 'nombre': 'EzequielCambio',
            'nick': 'ZzequiCambio', 'imagen': 'http://localhost:5000/static/usuarios/mistborn.png',
            'hashed_password': ""}

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.put("/api/usuario/1", headers=headers, follow_redirects=True, data=data,
                    content_type='multipart/form-data')
    rsp = rv.get_json()

    assert "EzequielCambio" == rsp.get("nombre")
    assert 1 == rsp.get("id")
    assert "ezequielCambio@ejemplo.com" == rsp.get("email")


def test_delUser(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.delete("/api/usuario/1", headers=headers, follow_redirects=True)
    respuesta = rv.status
    assert '204 NO CONTENT' == respuesta
