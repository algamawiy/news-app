from fastapi import FastAPI, UploadFile, File
import os
import shutil


app = FastAPI()



@app.post("/")
def upload_file(file: UploadFile):
    filename = file.filename
    os.makedirs(r'..\assets\uploaded_images', exist_ok=True)
    with open(os.path.join(r'..\assets\uploaded_images', f'{file.filename}'), 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": filename}



