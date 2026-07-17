from PIL import Image
import os

# ... (tvoje funkce invert_chess_piece zůstává stejná) ...

# Tímto získáme absolutní cestu ke složce, ve které leží tento skript (resources)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Spojíme cestu ke složce s názvem souboru
input_file = os.path.join(script_dir, "black_knight.png")
output_file = os.path.join(script_dir, "white_knight_test.png")


def invert_chess_piece(input_path, output_path):
    # Otevřeme obrázek a převedeme na RGBA (podpora průhlednosti)
    img = Image.open(input_path).convert("RGBA")
    pixels = img.load()
    
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # 1. Pokud je pixel úplně průhledný, přeskočíme ho
            if a == 0:
                continue
                
            # 2. Ponecháme velmi tmavé pixely (obrysové linky) beze změny
            # Hodnota 45 určuje citlivost (pokud jsou některé obrysy moc světlé, můžeš číslo zvýšit)
            brightness = (r + g + b) / 3
            if brightness < 25:
                continue
                
            # 3. Invertujeme barvu vnitřní výplně
            inv_r = 255 - r
            inv_g = 255 - g
            inv_b = 255 - b
            
            # 4. Přidáme nažloutlý / slonovinový nádech (teplý tón)
            # Červenou a zelenou necháme vysokou, modrou trochu stáhneme dolů
            new_r = int(inv_r * 1.0)      # Držíme max jas v červené
            new_g = int(inv_g * 0.95)     # Lehce ztlumíme zelenou pro přirozenější tón
            new_b = int(inv_b * 0.85)     # Výrazněji stáhneme modrou, což vytvoří krásnou žlutavou/krémovou
            
            # Ošetříme, aby hodnoty nepřetekly přes 255
            new_r = min(255, max(0, new_r))
            new_g = min(255, max(0, new_g))
            new_b = min(255, max(0, new_b))
            
            pixels[x, y] = (new_r, new_g, new_b, a)
            
    # Uložíme výsledný obrázek
    img.save(output_path)
    print(f"Figurka byla úspěšně invertována a uložena jako: {output_path}")

# --- PŘÍKLAD POUŽITÍ ---
# Stačí změnit názvy souborů podle potřeby
invert_chess_piece(input_file, output_file)