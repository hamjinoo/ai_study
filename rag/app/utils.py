def make_citations_block(docs):
    parts = []
    for i, d in enumerate(docs, start=1):
        parts.append(f"[{i}] {d.text[:200]}\nSOURCE:{d.meta.get('id','unknown')}")
    return "\n\n".join(parts)
