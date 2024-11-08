import base64
from django.conf import settings
from django.shortcuts import render
import os
import glob

def index(request):
    anya_path = getattr(settings, 'ANYA_DIR', '/anya')
    image_file = request.GET.get('img', 'anya.png').replace("../", "")
    image_path = os.path.join(anya_path, image_file)
    anyas = []

    try:
        with open(image_path, "rb") as file:
            img = base64.b64encode(file.read()).decode("utf-8")

        for filename in glob.glob(os.path.join(anya_path, '*.txt')):
            with open(filename, 'r') as file:
                anyas.append(file.read())

    except Exception as _e:
        default_image_path = os.path.join(anya_path, 'anya.png')
        with open(default_image_path, "rb") as file:
            img = base64.b64encode(file.read()).decode("utf-8")

    return render(request, 'index.html', {'img': img, 'anyas': anyas})
