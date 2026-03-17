import pypdf
with open('Excel Ardor Masts PPt.pdf', 'rb') as f:
    reader = pypdf.PdfReader(f)
    for page in reader.pages:
        print(page.extract_text())
