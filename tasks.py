from celery import Celery
import cv2
import os
import numpy as np
import requests
from io import BytesIO

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",

)


def detect_people(image_path): ##todo
    return 1, 1


@celery.task
def detect_people_from_url(url):
    response = requests.get(url)
    image_path = f"static/temp_{url.split('/')[-1]}"
    with open(image_path, 'wb') as f:
        f.write(response.content)
    count, output = detect_people(image_path)
    return {"count": count, "output_path": output}
