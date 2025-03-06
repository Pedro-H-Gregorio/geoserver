import requests
from io import BytesIO
from PIL import Image

def request_wms_image_paraiba(workspace, layer, format):
    GEO_URL = f"http://localhost:8080/geoserver/{workspace}/wms"
    
    params = {
        "service": "WMS",
        "version": "1.1.1",
        "request": "GetMap",
        "layers": f"{workspace}:{layer}",
        "styles": "",
        "bbox": "-38.765603399999975,-8.302955099999963,-34.79308649999996,-6.025911899999926",
        "width": "1920",
        "height": "1080",
        "srs": "EPSG:4674",
        "format": f"image/{format}"
    }
    
    try:
        print("Requisitando imagem do mapa da Paraíba")
        response = requests.get(GEO_URL, params=params)
        
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image.save(f"images/PB_Municipios.{format}", F"{str.upper(format)}")
            print(f"Imagem salva em: images/PB_Municipios.{format}")
        else:
            print(f"Erro na requisição: {response.status_code} - {response.reason}")
    except Exception as e:
        print("Erro ao requisitar a imagem do WMS:", e)