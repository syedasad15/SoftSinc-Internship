from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import uuid
import json

app = FastAPI(title="Student Manager + CSV EDA API")

# CORS settings (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
PLOT_DIR = "plots"
EDA_DIR = "eda"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(PLOT_DIR, exist_ok=True)
os.makedirs(EDA_DIR, exist_ok=True)

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    file_id = str(uuid.uuid4())
    save_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")

    with open(save_path, "wb") as buffer:
        buffer.write(await file.read())

    # Load CSV into DataFrame
    try:
        df = pd.read_csv(save_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV: {e}")

    # Generate summary
    summary = df.describe(include="all")

    # Convert to JSON-safe format
    summary_json = json.loads(summary.to_json())

    # Save summary to file
    summary_file = os.path.join(EDA_DIR, f"{file_id}_summary.json")
    with open(summary_file, "w") as f:
        json.dump(summary_json, f, indent=4)

    # Create and save plots
    plot_files = []
    numeric_cols = df.select_dtypes(include="number").columns

    eda_folder = os.path.join("eda_results", file_id)
    os.makedirs(eda_folder, exist_ok=True)

    # Save summary JSON
    summary_file = os.path.join(eda_folder, "summary.json")
    with open(summary_file, "w") as f:
        json.dump(summary_json, f, indent=4)

    # Save plots
    plot_files = []
    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f"Distribution of {col}")
        plt.tight_layout()
        plot_path = os.path.join(eda_folder, f"plot_{col}.png")
        plt.savefig(plot_path)
        plt.close()
        plot_files.append(plot_path)


    return JSONResponse(content={
        "filename": file.filename,
        "eda_summary": summary_json,
        "summary_file": summary_file,
        "plot_files": plot_files
    })
