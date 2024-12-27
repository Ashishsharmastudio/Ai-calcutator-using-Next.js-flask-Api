from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageDate
from PIL import Image

router = APIRouter()

@router.post("/calculate")
async def run(data: ImageDate):
    image_data = base64.b64decode(data.image.split(",")[1])
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)
    response = analyze_image(image, data.dict_of_vars)
    data = []
    for response in response:
        data.append(response)
    print('response  in route: ', response)
    return {
        "message": "Image Processed",
        "type": "success",
        "data": data
    }
