# 📂 Organizador Automático de Arquivos

Este projeto é uma automação simples em **Python** que organiza automaticamente os arquivos de uma pasta em categorias, facilitando a organização e limpeza de diretórios com muitos arquivos misturados.

A automação analisa todos os arquivos e pastas no mesmo diretório onde o script (ou executável) está localizado e move cada item para a categoria correspondente dentro de uma pasta chamada **ORGANIZAÇÃO**.

---

## ⚙️ Como funciona

Quando o script é executado, ele:

- Detecta automaticamente o diretório onde está localizado.
- Cria uma pasta chamada **ORGANIZAÇÃO** (caso ela ainda não exista).
- Analisa todos os arquivos e pastas presentes no diretório.
- Move cada item para uma subpasta correspondente baseada no **tipo de arquivo**.

Além disso, o script também:

- Ignora o próprio **script/executável** para evitar mover a automação.
- Ignora a pasta **ORGANIZAÇÃO** caso ela já exista.
- Move todas as **pastas encontradas** para uma subpasta chamada **Pastas**.

---

## 📁 Estrutura criada

Após a execução, a estrutura da pasta ficará semelhante a:

### ORGANIZAÇÃO/

│

├── Videos/

├── Imagens/

├── Texto/

├── Planilhas/

├── Documentos/

├── Compactados/

├── Outros/

└── Pastas/



Cada arquivo será movido automaticamente para sua categoria.

---

## 🧠 Categorias de Arquivos

O script organiza os arquivos com base nas extensões:

| Categoria     | Extensões |
|---------------|-----------|
| Videos        | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv` |
| Imagens       | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| Texto         | `.txt` |
| Planilhas     | `.xls`, `.xlsx`, `.csv` |
| Documentos    | `.pdf`, `.doc`, `.docx` |
| Compactados   | `.zip`, `.rar`, `.7z` |
| Outros        | Qualquer extensão não listada |
