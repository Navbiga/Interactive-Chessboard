import os
from PIL import Image

# -----------------------------------------------------------------------------
# NASTAVENÍ A KONFIGURACE
# -----------------------------------------------------------------------------
TARGET_TILE_SIZE = (100, 100)

INPUT_DIR = "resources_unscaled"
OUTPUT_DIR = "resources"

# Koeficienty zmenšení pro jednotlivé figurky
SCALING_FACTORS = {
    "pawn": 0.8,
    "king": 0.9,
    "queen": 0.85,
    "rook": 0.7,
    "bishop": 0.8,
    "knight": 0.8,
}

def process_scale():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Vytvořena složka: {OUTPUT_DIR}")

    for filename in os.listdir(INPUT_DIR):
        # Bereme pouze PNG soubory a přeskakujeme jakékoliv _selected verze
        if not filename.endswith(".png") or "_selected" in filename:
            continue

        input_path = os.path.join(INPUT_DIR, filename)

        # Určení typu figurky ze jména souboru
        piece_type = None
        for p_type in SCALING_FACTORS.keys():
            if p_type in filename:
                piece_type = p_type
                break

        if not piece_type:
            continue

        scale_factor = SCALING_FACTORS[piece_type]

        with Image.open(input_path) as img:
            img = img.convert("RGBA")

            # Výpočet nových rozměrů
            effective_scale = min(scale_factor, 1.0)
            new_w = int(img.width * effective_scale)
            new_h = int(img.height * effective_scale)

            # Zmenšení s zachováním ostrých pixelů (NEAREST)
            resized_img = img.resize((new_w, new_h), Image.Resampling.NEAREST)

            # Vycentrování na plátno 100x100 px s průhledným pozadím
            background = Image.new("RGBA", TARGET_TILE_SIZE, (0, 0, 0, 0))
            paste_x = (TARGET_TILE_SIZE[0] - new_w) // 2
            paste_y = (TARGET_TILE_SIZE[1] - new_h) // 2

            background.paste(resized_img, (paste_x, paste_y), resized_img)

            output_path = os.path.join(OUTPUT_DIR, filename)
            background.save(output_path)
            print(f"Zpracováno & vycentrováno: {filename} -> {OUTPUT_DIR}/")

if __name__ == "__main__":
    process_scale()
    print("\nHotovo! Všechny obrázky byly zmenšeny a vycentrovány do 100x100px.")
