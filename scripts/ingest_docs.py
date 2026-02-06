import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.ingestion.loader import load_pdf
from app.ingestion.chunker import split_text
from app.ingestion.indexer import index_documents


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw_pdfs")


def main():

    print("Looking for PDFs in:", DATA_DIR)

    if not os.path.exists(DATA_DIR):
        print("❌ Folder not found:", DATA_DIR)
        return

    files = os.listdir(DATA_DIR)

    if not files:
        print("❌ No PDF files found")
        return

    for file in files:

        if file.lower().endswith(".pdf"):

            path = os.path.join(DATA_DIR, file)

            print("Processing:", file)

            text = load_pdf(path)

            print("Extracted chars:", len(text))

            if len(text.strip()) < 100:
                print("⚠️ Warning: Very little text extracted!")

            chunks = split_text(text)

            print("Chunks:", len(chunks))

            index_documents(chunks, file)


if __name__ == "__main__":
    main()
