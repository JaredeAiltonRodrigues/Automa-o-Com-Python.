from pathlib import Path
import shutil

pasta = Path("documentos")

# Mover todos os PDFs para uma subpasta
for arquivo in pasta.glob("**/*.pdf"):
    destino = pasta / "pdfs" / arquivo.name
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(arquivo, destino)

# Renomear em lote com padrão
for i, arquivo in enumerate(pasta.glob("*.jpg"), start=1):
    arquivo.rename(arquivo.parent / f"foto_{i:03d}.jpg")
