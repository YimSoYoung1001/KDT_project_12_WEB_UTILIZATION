import io
from PIL import Image

def image_to_binary(image):
    image_bytes = io.BytesIO()
    image_format = image.format if image.format else 'PNG'  # 원본 이미지의 포맷을 확인하고, 없다면 기본값으로 'PNG'를 사용
    image.save(image_bytes, format=image_format)  # 원본 이미지의 포맷으로 이미지를 저장
    image_bytes = image_bytes.getvalue()
    return image_bytes