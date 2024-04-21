from flask import Blueprint, request, render_template
from Team5_web import db
import pyttsx3
from PIL import Image
bp = Blueprint('main', __name__, url_prefix='/')
engine = pyttsx3.init()
from Team5_web.utils import image_to_binary
from Team5_web.model import Image

def generate_caption(image):
    # 모델 코드 구현
    caption = "예시 캡션: 이미지에 대한 설명"
    return caption

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 요청에서 이미지 가져오기
        image_file = request.files['image']
        image = Image.open(image_file.stream)

        # 캡션 생성
        caption = generate_caption(image)

        # 이미지를 바이너리 데이터로 변환
        image_binary = image_to_binary(image)

        # 이미지와 캡션을 데이터베이스에 저장
        new_image = Image(image=image_binary, caption=caption)
        db.session.add(new_image)
        db.session.commit()

        # 캡션을 음성으로 변환
        engine.say(caption)
        engine.runAndWait()

    #     flash('Image uploaded and caption generated successfully.', 'success')
    #     return redirect(url_for('main.index'))
    #
    # return render_template('index.html')

        return render_template('index.html', caption=caption)
    return render_template('index.html')

@bp.route('/gallery')
def gallery():
    images = db.session.query(Image).all()
    return render_template('gallery.html', images=images)