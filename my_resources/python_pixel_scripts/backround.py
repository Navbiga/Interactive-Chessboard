import os
from PIL import Image

# -----------------------------------------------------------------------------
# NASTAVENÍ BARVY POZADÍ
# -----------------------------------------------------------------------------
SELECTION_HEX_COLOR = "#5C7CFA"       # Výchozí modrá
KING_SELECTION_HEX_COLOR = "#FF6B6B"  # Červená pro krále

TARGET_TILE_SIZE = (100, 100)

INPUT_DIR = "resources"
OUTPUT_DIR = "image_output"

def hex_to_rgba(hex_str, alpha=255):
    hex_str = hex_str.lstrip('#')
    r, g, b = tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
    return (r, g, b, alpha)

def process_background():
    if not os.path.exists(INPUT_DIR):
        print(f"Složka {INPUT_DIR} neexistuje!")
        return

    for filename in os.listdir(INPUT_DIR):
        # Bereme pouze čisté verze
        if not filename.endswith(".png") or "_selected" in filename:
            continue

        input_path = os.path.join(INPUT_DIR, filename)

        with Image.open(input_path) as img:
            img = img.convert("RGBA")

            # Určení barvy pozadí podle toho, zda jde o krále
            bg_color = KING_SELECTION_HEX_COLOR if "king" in filename else SELECTION_HEX_COLOR
            
            # Vytvoření plného pozadí 100x100
            background = Image.new("RGBA", TARGET_TILE_SIZE, hex_to_rgba(bg_color))
            
            # Vložení figurky na pozadí
            background.paste(img, (0, 0), img)

            # Uložení jako _selected.png
            sel_filename = filename.replace(".png", "_selected.png")
            sel_path = os.path.join(OUTPUT_DIR, sel_filename)
            background.save(sel_path)

            print(f"Vygenerováno pozadí pro: {sel_filename}")

if __name__ == "__main__":
    process_background()
    print("\nHotovo! Všechny _selected textury s pozadím jsou vytvořeny.")