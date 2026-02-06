import re


def is_garbage(text):

    # Remove table of contents / index
    bad_patterns = [
        r"contents",
        r"table of contents",
        r"\.{5,}",          # many dots
        r"page\s+\d+",
        r"ARTICLE\s+PAGES",
    ]

    text_low = text.lower()

    for p in bad_patterns:
        if re.search(p, text_low):
            return True

    if len(text.strip()) < 200:
        return True

    return False


def split_text(text, chunk_size=800, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        if not is_garbage(chunk):
            chunks.append(chunk)

        start = end - overlap

    return chunks
