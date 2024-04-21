from flask import render_template, request
# from app import app, db, cursor
import pyttsx3
from PIL import Image
import io
import base64
from .model import generate_caption
from .utils import image_to_binary

# 텍스트 음성 변환 엔진 초기화
engine = pyttsx3.init()

