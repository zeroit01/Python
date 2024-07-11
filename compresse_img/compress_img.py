from PIL import Image

def compress_image(input_path, output_path, quality=20, max_width=None, max_height=None):
    # Open an image file
    with Image.open(input_path) as img:
        # Convert image to RGB mode if it's in P mode
        if img.mode == 'P':
            img = img.convert('RGB')
        
        # Resize image if max_width or max_height is provided
        if max_width or max_height:
            # Calculate aspect ratio
            aspect_ratio = img.width / img.height
            
            if max_width and max_height:
                # Determine the new size keeping the aspect ratio
                if img.width / max_width > img.height / max_height:
                    new_width = max_width
                    new_height = int(max_width / aspect_ratio)
                else:
                    new_height = max_height
                    new_width = int(max_height * aspect_ratio)
            elif max_width:
                new_width = max_width
                new_height = int(max_width / aspect_ratio)
            elif max_height:
                new_height = max_height
                new_width = int(max_height * aspect_ratio)
            
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Save it with a new name and quality
        img.save(output_path, "JPEG", quality=quality)

# Example usage
input_image_path = "back.png"  # This can be a PNG, GIF, etc.
output_image_path = "compressed_image.jpg"
compress_image(input_image_path, output_image_path, quality=30, max_width=3467)
