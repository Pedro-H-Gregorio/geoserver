from dotenv import load_dotenv
import os
from functions.Conection_Test import test_connection
from functions.Get_Map_Paraiba import request_wms_image_paraiba
from functions.Get_City_Map import request_wms_city_image
load_dotenv()

#Loading environment variables
workspace = os.environ["WORKSPACE_NAME"]
layer_title = os.environ["LAYER_TITLE"]
format = os.environ["FORMAT"]
scale = os.environ["BBOX"]
city_code = os.environ["CODIGO_MUNICIPIO"]

if __name__ == "__main__":
  test_connection(workspace)
  request_wms_image_paraiba(workspace, layer_title, format)
  request_wms_city_image(workspace, layer_title, format, scale, city_code)
