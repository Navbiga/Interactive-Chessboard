import os
from PIL import Image

def add_selected_background():
    # Define the target hex color and convert it to an RGB tuple
    hex_color = "93F7FF"
    bg_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) # (147, 247, 255)
    
    # FIX: Get the exact directory where THIS script file is located
    current_directory = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(current_directory)
    
    print(f"Starting image processing in directory: {current_directory}")
    
    for filename in files:
        # Process only PNG files and skip already generated copies to avoid loops
        if filename.lower().endswith('.png') and not filename.endswith('_selected.png'):
            # Skip the main chessboard texture if you don't want to tint it
            if filename == "chessboard.png":
                continue
                
            input_path = os.path.join(current_directory, filename)
            
            try:
                with Image.open(input_path) as img:
                    # Ensure the image has an alpha (transparent) channel
                    img = img.convert("RGBA")
                    
                    # Create a solid background image with the target color
                    background = Image.new("RGBA", img.size, bg_color + (255,))
                    
                    # Composite the original image over the solid background using the alpha channel as a mask
                    combined_img = Image.alpha_composite(background, img)
                    
                    # Generate the new filename with the requested suffix
                    name_part, extension = os.path.splitext(filename)
                    output_filename = f"{name_part}_selected{extension}"
                    output_path = os.path.join(current_directory, output_filename)
                    
                    # Save the result
                    combined_img.save(output_path, "PNG")
                    print(f"Successfully processed: {filename} -> {output_filename}")
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
    print("All done!")

if __name__ == "__main__":
    add_selected_background()