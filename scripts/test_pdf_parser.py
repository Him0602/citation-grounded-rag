from app.ingestion.pdf_parser import extract_pages


pages = extract_pages("tests/sample.pdf")

for page in pages:
    print(f"\n--- Page {page['page_number']} ---")
    print(page["text"][:500])