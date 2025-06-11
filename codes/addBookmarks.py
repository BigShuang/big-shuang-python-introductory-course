import fitz  # PyMuPDF

UpperSize = 17.5

RANK1 = 16.8
RANK2 = 16
RANK3 = 15

def detect_titles(pdf_path, font_size_threshold=14):
    """
    Detect titles in a PDF file based on font size.

    Args:
        pdf_path (str): Path to the PDF file.
        font_size_threshold (float): Font size threshold to detect titles.

    Returns:
        list of tuples: (title text, page number, font size)
    """
    doc = fitz.open(pdf_path)
    titles = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    font_size = span["size"]
                    text = span["text"].strip()

                    if font_size >= font_size_threshold \
                        and font_size < UpperSize and text:
                        print(text, font_size)
                        titles.append((text, page_num + 1, font_size))  # page number starts from 1

    doc.close()
    return titles

def build_toc(titles):
    """
    Build a Table of Contents (ToC) list for set_toc().

    Args:
        titles (list): (title text, page number, font size)

    Returns:
        list of lists: Each item is [level, title, page_number]
    """
    toc = []
    for title, page, size in titles:
        # Use font size to infer level (larger -> higher level)
        level = 1 if size >= RANK1 else 2 if size >= RANK2 else 3
        toc.append([level, title, page])
    return toc

def add_bookmarks(pdf_path, output_path, titles):
    """
    Add bookmarks to PDF using detected titles.

    Args:
        pdf_path (str): Input PDF path.
        output_path (str): Output PDF path with bookmarks.
        titles (list): List of (title text, page number, font size)
    """
    doc = fitz.open(pdf_path)

    toc = build_toc(titles)
    doc.set_toc(toc)

    doc.save(output_path)
    print(f"✅ Bookmarks created and saved to: {output_path}")


# Example usage
pdf_path = "./output/1.pdf"
output_path = "./output/c1.pdf"

titles = detect_titles(pdf_path)
add_bookmarks(pdf_path, output_path, titles)
