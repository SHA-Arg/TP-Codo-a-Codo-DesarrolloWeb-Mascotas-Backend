import requests

BASE_URL = "http://localhost:5000"  # Cambia por tu dominio en PythonAnywhere si lo corrés allá

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_crud_mascota():
    # Crear
    mascota = {
        "name": "Test",
        "pet_type": 1,
        "race": "mestizo",
        "color": "negro",
        "size": "mediano",
        "sex": "M",
        "age": 2,
        "vaccine": True,
        "sterilization": True,
        "health_status": "sano",
        "description": "test api",
        "organization": 1,
        "image": "",
        "ubication": "CABA"
    }
    r = requests.post(f"{BASE_URL}/mascotas", json=mascota)
    assert r.status_code in (201, 409)  # 409 si ya existe
    # Listar
    r = requests.get(f"{BASE_URL}/mascotas")
    assert r.status_code == 200
    data = r.json()
    assert "pets" in data

if __name__ == "__main__":
    test_health()
    test_crud_mascota()
    print("Smoke tests OK")
