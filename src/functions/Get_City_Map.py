import requests
from io import BytesIO
from PIL import Image

def request_wms_city_image(workspace, layer, format, bbox, code):
    GEO_URL = f"http://localhost:8080/geoserver/{workspace}/wms"
    
    params = {
        "service": "WMS",
        "version": "1.3.0",
        "request": "GetMap",
        "layers": f"{workspace}:{layer}",
        "styles": "",
        "bbox": "-7.108623068630974,-36.02129230769231,-6.903376931369026,-35.73870769230769",
        "width": "820",
        "height": "600",
        "srs": "EPSG:4674",
        "format": f"image/{format}",
        "CQL_FILTER": f"CD_MUN={code}"
    }

    try:
      response = requests.get(GEO_URL, params=params)
      
      if response.status_code == 200:
          image = Image.open(BytesIO(response.content))
          image.save(f"images/city_wms.{format}", F"{str.upper(format)}")
          print(f"Imagem salva em: city_wms.{format}")
      else:
          print(f"Erro na requisição: {response.status_code} - {response.reason}")
    except Exception as e:
      print("Erro ao requisitar a imagem do WMS:", e)

