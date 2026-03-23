from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False)

result = md.convert("2025_community.pdf")

with open("2025_community.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)

print("변환 완료")