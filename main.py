import os
import shutil
import sys


def resource_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))


base_path = resource_path()

org_path = os.path.join(base_path, "ORGANIZAÇÃO")
os.makedirs(org_path, exist_ok=True)


categorias = {
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Texto": [".txt"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Documentos": [".pdf", ".doc", ".docx"],
    "Compactados": [".zip", ".rar", ".7z"]
}


def encontrar_categoria(ext):
    for categoria, extensoes in categorias.items():
        if ext in extensoes:
            return categoria
    return "Outros"


arquivo_atual = os.path.basename(sys.argv[0])


for item in os.listdir(base_path):

    # Ignorar o próprio script/exe
    if item == arquivo_atual:
        continue

    caminho_item = os.path.join(base_path, item)

    # Ignorar a própria pasta de organização
    if item == "ORGANIZAÇÃO":
        continue

    # Se for pasta
    if os.path.isdir(caminho_item):

        pasta_destino = os.path.join(org_path, "Pastas")
        os.makedirs(pasta_destino, exist_ok=True)

        destino = os.path.join(pasta_destino, item)

        print(f"Movendo pasta: {item}")

        shutil.move(caminho_item, destino)

    # Se for arquivo
    elif os.path.isfile(caminho_item):

        ext = os.path.splitext(item)[1].lower()
        categoria = encontrar_categoria(ext)

        pasta_destino = os.path.join(org_path, categoria)
        os.makedirs(pasta_destino, exist_ok=True)

        destino = os.path.join(pasta_destino, item)

        print(f"Movendo arquivo: {item} -> {categoria}")

        shutil.move(caminho_item, destino)


print("\nOrganização finalizada.")
