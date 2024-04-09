import pytest
from app import create_app
from werkzeug.datastructures import Headers


@pytest.fixture
def client():
    app = create_app('config_tests.py')

    with app.test_client() as client:
        yield client


def test_getComentarios(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.get('/api/comentario', headers=headers, follow_redirects=True)
    rsp = rv.get_json()

    assert len(rsp) == 16


def test_getComentario(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.get("/api/comentario/1", headers=headers, follow_redirects=True)
    rsp = rv.get_json()

    assert rsp.get("padre") is None
    assert rsp.get("imagen") is None
    assert rsp.get("contenido") == "Se me olvidó mencionar que si quereis más recetas dadle a me gusta!"
    assert 1 == rsp.get("usuario")
    assert 1 == rsp.get("receta")
    assert 1 == rsp.get("id")


def test_postComentario(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    data = {'usuario_id': 1, 'receta_id': 3, 'padre_id': "", 'imagen': '', 'contenido': "prueba"}

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.post("/api/comentario", headers=headers, follow_redirects=True, data=data,
                     content_type='multipart/form-data')
    rsp = rv.get_json()

    assert rsp.get("padre") is None
    assert rsp.get("contenido") == "prueba"
    assert 1 == rsp.get("usuario")
    assert 3 == rsp.get("receta")
    assert 17 == rsp.get("id")


def test_putComentario(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.put("/api/comentario/1", headers=headers, follow_redirects=True,
                    json={'id': 1, 'usuario': 1, 'receta': 1, 'padre': None,
                          'imagen': '/static/imagenes/comentario/anon.jpg',
                          'contenido': "prueba"})
    rsp = rv.get_json()

    assert rsp.get("padre") is None
    assert rsp.get("imagen") == "/static/imagenes/comentario/anon.jpg"
    assert rsp.get("contenido") == "prueba"
    assert 1 == rsp.get("usuario")
    assert 1 == rsp.get("receta")
    assert 1 == rsp.get("id")


def test_delComentario(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.delete("/api/comentario/1", headers=headers, follow_redirects=True)
    respuesta = rv.status
    assert '204 NO CONTENT' == respuesta
