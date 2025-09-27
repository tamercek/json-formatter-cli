import json
import sys

# Kullanım: python app.py input.json output.json
infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(outfile, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✔ {outfile} dosyası oluşturuldu")
