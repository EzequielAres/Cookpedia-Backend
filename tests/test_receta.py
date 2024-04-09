import io

import pytest
from app import create_app
from werkzeug.datastructures import Headers


@pytest.fixture
def client():
    app = create_app('config_tests.py')

    with app.test_client() as client:
        yield client


def test_getRecetas(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.get('/api/receta', headers=headers, follow_redirects=True)
    rsp = rv.get_json()

    assert len(rsp) == 15
    assert "Gazpacho" in [d.get("nombre") for d in rsp]


def test_getReceta(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.get("/api/receta/1", headers=headers, follow_redirects=True)
    rsp = rv.get_json()

    assert "Tarta de limón sin queso" == rsp.get("nombre")
    assert 1 == rsp.get("id")
    assert 'La tarta de limón sin queso es una elaboración deliciosa, fresquita y sencilla de preparar. Un pastel de ' \
           'limón ideal para después de una comida, ya que es ligero y con un sabor agradable. Además, esta receta ' \
           'que os presentamos no contiene queso, se elabora con yogur y con nata. Por otro lado, no necesita horno y ' \
           'es ideal para el verano. Sin embargo, aunque no necesite horno, si es necesario 3-4 horas para que esté ' \
           'la tarta fría, incluso, el día siguiente está más buena.' == rsp.get("descripcion")


def test_postReceta(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    data = {'nombre': 'Pollo prueba', 'descripcion': 'sdfds', 'pasos': 'sdfsdfsdf', 'id_usuario': 1,
            'imagen': (io.BytesIO(b"abcdef"), 'test.jpg')}

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.post("/api/receta/", headers=headers, follow_redirects=True, data=data,
                     content_type="multipart/form-data")
    rsp = rv.get_json()

    assert "Pollo prueba" == rsp.get("nombre")
    assert 16 == rsp.get("id")
    assert "sdfds" == rsp.get("descripcion")
    assert 'http://localhost:5000/static/recetas/test.jpg' == rsp.get("imagen")
    assert "sdfsdfsdf" == rsp.get("pasos")


def test_putReceta(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.put("/api/receta/1", headers=headers, follow_redirects=True,
                    json={"id": 1, 'nombre': 'Pollo prueba', 'descripcion': 'sdfds', 'imagen': 'sdfsdfs',
                          'pasos': 'sdfsdfsdf', "video": ""})
    rsp = rv.get_json()

    assert "Pollo prueba" == rsp.get("nombre")
    assert 1 == rsp.get("id")
    assert "sdfds" == rsp.get("descripcion")
    assert "sdfsdfs" == rsp.get("imagen")
    assert "sdfsdfsdf" == rsp.get("pasos")


def test_delReceta(client):
    rv = client.post('/login', json={'nombre': 'Ezequiel', 'password': 'pestillo'})
    rsp = rv.get_json()
    assert 'access_token' in rsp.keys()

    headers = Headers()
    headers.add('Authorization', f"Bearer {rsp['access_token']}")
    rv = client.delete("/api/receta/1", headers=headers, follow_redirects=True)
    respuesta = rv.status
    assert '204 NO CONTENT' == respuesta
