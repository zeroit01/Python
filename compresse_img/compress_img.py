from PIL import Image

def compress_image(input_path, output_path, quality=20, max_width=None, max_height=None):
    with Image.open(input_path) as img:
        if img.mode == 'P':
            img = img.convert('RGB')
        
        if max_width or max_height:
            aspect_ratio = img.width / img.height
            
            if max_width and max_height:
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
        
        img.save(output_path, "JPEG", quality=quality)

input_image_path = "1.png"
output_image_path = "2.jpg"
compress_image(input_image_path, output_image_path, quality=30, max_width=3467)
