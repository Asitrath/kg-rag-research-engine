import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# 1. Setup paths
BASE_DIR = Path(__file__).resolve().parent
WIKI_DIR = BASE_DIR / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
CONCEPTS_DIR = WIKI_DIR / "concepts"

# 2. Load environment and initialize
load_dotenv(BASE_DIR / ".env")
client = genai.Client()

def get_wiki_content():
    """Reads all markdown files in the wiki directory to provide context."""
    combined_content = ""
    
    # Read Sources
    if SOURCES_DIR.exists():
        combined_content += "--- SOURCE SUMMARIES ---\n"
        for file in SOURCES_DIR.glob("*.md"):
            # Added errors="ignore" to handle special characters
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                combined_content += f"\nFile: {file.name}\n{f.read()}\n"
                
    # Read Concepts
    if CONCEPTS_DIR.exists():
        combined_content += "\n--- CONCEPT DEFINITIONS ---\n"
        for file in CONCEPTS_DIR.glob("*.md"):
            # Added errors="ignore" here as well
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                combined_content += f"\nConcept: {file.name}\n{f.read()}\n"
                
    return combined_content

def run_linter():
    print("Reading wiki content for analysis...")
    wiki_context = get_wiki_content()
    
    if not wiki_context:
        print("Wiki is empty. Please run ingestion.py first.")
        return

    lint_prompt = f"""
    You are a Research Linter specializing in Knowledge Graph RAG (KG-RAG). 
    I will provide the current contents of my research wiki. Your task is to:
    
    1. **Identify Logical Gaps**: Does any baseline (like ToG or GNN-RAG) fail to address the 'Structural Boundary' problem defined in UniKG-RAG?
    2. **Terminology Consistency**: Are we using 'qualifiers', 'attributes', and 'modifiers' consistently across all notes?
    3. **Link Suggestions**: Suggest 5 specific [[wikilinks]] that should be added to connect existing pages.
    4. **Contradiction Detection**: Highlight if any baseline claims to handle a structure that UniKG-RAG proves it cannot handle.

    CURRENT WIKI CONTENT:
    {wiki_context}
    """

    print("Gemini is analyzing your research graph...")
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=lint_prompt
    )

    # Save the report
    report_path = WIKI_DIR / "LINT_REPORT.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# Wiki Lint Report - {os.path.getmtime(report_path) if report_path.exists() else 'New'}\n\n")
        f.write(response.text)
    
    print(f"\nAnalysis Complete! Report saved to {report_path}")
    print("\n--- Summary of Findings ---")
    print(response.text[:500] + "...")

if __name__ == "__main__":
    run_linter()