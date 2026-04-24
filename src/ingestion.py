import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# 1. Setup paths relative to where this script is saved
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "raw"
WIKI_DIR = BASE_DIR / "wiki"
# Updated this line to look inside the wiki folder
SCHEMA_FILE = WIKI_DIR / "CLAUDE.md" 

# 2. Load the .env file and initialize Gemini
load_dotenv(BASE_DIR / ".env")
client = genai.Client()

# 3. Load your Wiki Schema
if not SCHEMA_FILE.exists():
    print(f"ERROR: Could not find schema at {SCHEMA_FILE}")
    exit()

with open(SCHEMA_FILE, "r") as f:
    schema_content = f.read()

# 4. Ingest Papers
# Add the names of your baseline PDFs here
papers_to_ingest = ["UniKG_RAG__Universal_Retrieval_Augmented_Generation_over_Knowledge_Graphs_of_Varying_Structural_Forms.pdf"]


for paper_name in papers_to_ingest:
    file_path = RAW_DIR / paper_name
    
    if not file_path.exists():
        print(f"Skipping {paper_name}: File not found in {RAW_DIR}")
        continue

    # Upload to File API using the correct 'file' parameter
    print(f"Uploading {paper_name}...")
    file_ref = client.files.upload(file=str(file_path)) # Fixed parameter name

    # Generate the Wiki Content
    print(f"Processing {paper_name} with Gemini...")
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            file_ref, 
            f"Apply the following schema to this paper and output the markdown content:\n\n{schema_content}"
        ]
    )

    # Save output to a new file in wiki/sources/
    output_folder = WIKI_DIR / "sources"
    output_folder.mkdir(exist_ok=True)
    
    output_file = output_folder / f"{Path(paper_name).stem}.md"
    with open(output_file, "w") as f:
        f.write(response.text)
        
    print(f"Success! Saved to {output_file}\n")