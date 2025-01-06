from fastapi import FastAPI, UploadFile, Form, File
import os
from celery.result import AsyncResult
from tasks import detect_people_from_url
import shutil
app = FastAPI()



@app.post("/detect/url")
async def detect_from_url(url: str = Form(...)):
    task = detect_people_from_url.delay(url)
    return {"task_id": task.id}


