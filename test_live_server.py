import subprocess
import time
import requests
import os

os.chdir('c:/Users/sha19/Documents/S3B4/DesarrolloWeb-Mascotas-Backend')

# Iniciar servidor
print("Iniciando servidor...")
proc = subprocess.Popen(['./venv/Scripts/python', 'app.py'],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

# Esperar que inicie
time.sleep(4)

# Probar
print("\n=== Probando http://127.0.0.1:5000/ ===")
try:
    response = requests.get('http://127.0.0.1:5000/', timeout=5)
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    print(f"\nPrimeros 500 caracteres del contenido:")
    print(response.text[:500])

    if response.status_code == 200 and 'html' in response.headers.get('Content-Type', ''):
        print("\n✓ SUCCESS - HTML servido correctamente")
    else:
        print("\n✗ ERROR - No es HTML válido")
except Exception as e:
    print(f"✗ ERROR: {e}")

# Terminar servidor
proc.terminate()
proc.wait(timeout=2)
print("\nServidor detenido")
