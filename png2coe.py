from PIL import Image
new_size = 50

image = Image.open('./figures/plane.png').convert('RGB')
image_size = image.size
image_ratio = image.size[0]/image.size[1]
print(f"Original size, new size : {image.size}, ({int(new_size*image_ratio)}, {new_size})")
image_resized = image.resize((int(new_size*image_ratio), new_size))

with open('./figures/coe/plane.coe','w') as f:
    f.write('memory_initialization_radix=16;\n')
    f.write('memory_initialization_vector=\n')

    for pixel in list(image_resized.getdata()):
        r_4 = pixel[0] >> 4
        g_4 = pixel[1] >> 4
        b_4 = pixel[2] >> 4

        res = r_4 | g_4 << 4 | b_4 << 8
        f.write (f'{res:04x}\n')
    
    f.write(';')
