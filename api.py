from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles # <--- NEW IMPORT
import shutil
import os
from src.processor import process_stocktake_file

app = FastAPI(title="Stocktake Reporter API")

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
STATIC_DIR = os.path.join(BASE_DIR, 'static') # <--- NEW PATH

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Mount the static folder so the HTML can be served
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse) # <--- Serve HTML on Homepage
def home():
    # Read the index.html file and return it
    with open(os.path.join(STATIC_DIR, "index.html")) as f:
        return f.read()

@app.post("/upload/")
async def upload_report(file: UploadFile = File(...)):
    # 1. Sanitize Inputs
    base_name = os.path.splitext(file.filename)[0]
    safe_input_name = f"{base_name}.xlsx"
    file_path = os.path.join(INPUT_DIR, safe_input_name)
    
    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # 2. Process
    output_filename = f"Report_{base_name}.xlsx"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    print(f"Processing {safe_input_name}...")
    try:
        process_stocktake_file(file_path, output_path)
        
        if os.path.exists(output_path):
            return FileResponse(
                path=output_path, 
                filename=output_filename, 
                media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
        else:
            return {"error": "Processing Failed. Check server logs."}
            
    except Exception as e:
        return {"error": f"Server Error: {str(e)}"}
    
# To run: uvicorn api:app --reload