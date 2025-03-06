import requests

def test_connection(workspace):
    URL = f"http://localhost:8080/geoserver/{workspace}/wms?service=WMS&request=GetCapabilities"

    response = requests.get(URL)

    if response.status_code == 200:
        print("Está sendo conectado com o workspace!")
    else:
        print(f"Erro ao acessar o WMS. Código de erro: {response.status_code}")