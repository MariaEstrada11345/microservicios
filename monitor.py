import requests
import time

SERVICIOS = {
    "usuarios": "http://localhost:5000/health",
    "pedidos": "http://localhost:5001/health",
    "inventario": "http://localhost:5002/health"
}

def chequear_servicios():
    for nombre, url in SERVICIOS.items():
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200 and r.json().get("status") == "ok":
                print(f"[OK] {nombre}: vivo")
            else:
                print(f"[FAIL] {nombre}: error en respuesta")
        except Exception as e:
            print(f"[FAIL] {nombre}: caído ({e})")

if __name__ == "__main__":
    while True:
        print("\n--- Health Check ---")
        chequear_servicios()
        time.sleep(5)
