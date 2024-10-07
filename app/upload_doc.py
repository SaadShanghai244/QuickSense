from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
import io


app = FastAPI()
# Directory where uploaded files will be saved
UPLOAD_DIRECTORY = "./uploaded_files"

# Ensure upload directory exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Check the file extension to ensure it's either PDF or text file
    if file.content_type not in ["application/pdf", "text/plain"]:
        raise HTTPException(status_code=400, detail="Only PDF and text files are allowed.")
    

    # Save the file to the upload directory
    file_location = f"{UPLOAD_DIRECTORY}/{file.filename}"
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())  # Save as binary

    # Process the text content
    print("File content (text):")  # Print first 100 characters of the text
    
    return JSONResponse(content={"filename": file.filename, "message": "File uploaded and read successfully"})

   