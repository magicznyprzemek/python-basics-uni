from fastapi import FastAPI, UploadFile, Form, File
import os
from celery.result import AsyncResult
from tasks import detect_people_from_file, detect_people_from_url
import shutil
app = FastAPI()


@app.post("/detect/file")
async def detect_from_file(file: UploadFile = File(...)):
    save_dir = os.path.abspath("static")
    os.makedirs(save_dir, exist_ok=True)
    image_path = os.path.join(save_dir, f"temp_{file.filename}")

    with open(image_path, 'wb+') as f:
        f.write(file.file.read())
    print(f"File successfully saved at {image_path}")

    task = detect_people_from_file.delay(image_path)
    return {"task_id": task.id}


@app.post("/detect/url")
async def detect_from_url(url: str = Form(...)):
    task = detect_people_from_url.delay(url)
    return {"task_id": task.id}

@app.get("/task/{task_id}")
async def get_task_status(task_id: str):
    task_result = AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result,
    }

