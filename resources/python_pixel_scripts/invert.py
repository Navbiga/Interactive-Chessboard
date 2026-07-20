import os
from PIL import Image

INPUT_DIR = "image_output"
OUTPUT_DIR = "image_output" # Uložíme přímo přebarvené verze

def apply_1px_inline(image):
    img = image.copy()
    width, height = img.size
    pixels = img.load()

    border_pixels = []

    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            
            # Pokud je pixel viditelný
            if a > 0:
                is_border = False
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    
                    if nx < 0 or nx >= width or ny < 0 or ny >= height:
                        is_border = True
                        break
                    elif pixels[nx, ny][3] == 0:
                        is_border = True
                        break

                if is_border:
                    border_pixels.append((x, y))

    # Přebarvíme pouze hraniční pixely na černou
    for x, y in border_pixels:
        pixels[x, y] = (0, 0, 0, 255)

    return img

def process_invert():
    if not os.path.exists(INPUT_DIR):
        print(f"Složka {INPUT_DIR} neexistuje!")
        return

    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".png") or "_selected" in filename:
            continue

        filepath = os.path.join(INPUT_DIR, filename)

        with Image.open(filepath) as img:
            img = img.convert("RGBA")
            inverted_img = apply_1px_inline(img)
            
            output_path = os.path.join(OUTPUT_DIR, filename)
            inverted_img.save(output_path)
            print(f"Invert/Inline aplikován: {filename}")

if __name__ == "__main__":
    process_invert()
    print("\nHotovo! Okraje byly přebarveny na černo.")