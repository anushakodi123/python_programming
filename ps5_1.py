from PIL import Image, ImageFont, ImageDraw

def make_matrix(color):
    matrices = {
        'red': [
            [0.56667, 0.43333, 0.00000],
            [0.55833, 0.44167, 0.00000],
            [0.00000, 0.24167, 0.75833]
        ],
        'green': [
            [0.62500, 0.37500, 0.00000],
            [0.70000, 0.30000, 0.00000],
            [0.00000, 0.30000, 0.70000]
        ],
        'blue': [
            [0.95000, 0.05000, 0.00000],
            [0.00000, 0.43333, 0.56667],
            [0.00000, 0.47500, 0.52500]
        ]
    }
    return matrices[color]

def matrix_multiply(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3)]

def extract_end_bits(num_end_bits, pixel):
    if isinstance(pixel, tuple):
        return tuple(i & ((1 << num_end_bits) - 1) for i in pixel)
    else:
        return pixel & ((1 << num_end_bits) - 1)

def pix_to_img(pixel_list, size, mode):
    img = Image.new(mode, size)
    img.putdata(pixel_list)
    return img

class ImageProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(filename)
        self.pixels = list(self.image.getdata())

    def get_pixels(self):
        return self.pixels
    
    def get_mode(self):
        return self.image.mode
    
    def get_size(self):
        return self.image.size
    
    def filter(self, color):
        if color is None:
            return self.pixels

        matrix = make_matrix(color)
        transformed = []
        for pixel in self.pixels:
            transformed_pixel = matrix_multiply(matrix, pixel)
            clamped_pixel = tuple(max(0, min(255, int(round(i)))) for i in transformed_pixel)
            transformed.append(clamped_pixel)

        return transformed

    def reveal_bw_image(self):
        return [pix & 1 for pix in self.pixels]

    def reveal_color_image(self):
        return [extract_end_bits(3, pix) for pix in self.pixels]

    def reveal_image(self):
        if self.get_mode() in ['1', 'L']:
            return self.reveal_bw_image()
        elif self.get_mode() == 'RGB':
            return self.reveal_color_image()
        else:
            raise ValueError(f"Unsupported image mode: {self.get_mode()}")

    def draw_kerb(self, kerb):
        im = self.image.copy()
        font = ImageFont.truetype("noto-sans-mono.ttf", 40)
        draw = ImageDraw.Draw(im)
        draw.text((0, 0), kerb, "white", font=font)
        idx = self.filename.rfind(".")
        new_filename = self.filename[:idx] + "_kerb" + self.filename[idx:]
        im.save(new_filename)
        return new_filename

def main():
    processor = ImageProcessor('hidden2.bmp')
    
    print('First 10 pixels:', processor.get_pixels()[:10])
    print('Mode:', processor.get_mode())
    print('Size:', processor.get_size())

    # Re-create and show image from pixels
    new_image = pix_to_img(processor.get_pixels(), processor.get_size(), processor.get_mode())
    new_image.show()

    # Filter example
    pixels = [(120, 200, 150), (30, 60, 90), (255, 100, 50)]
    processor.pixels = pixels
    print('Red filtered:', processor.filter('red'))

    # Bit extraction examples
    print('Extract 5 bits from 214:', extract_end_bits(5, 214))
    print('Extract 3 bits from (214, 17, 8):', extract_end_bits(3, (214, 17, 8)))

    # Reveal BW
    bw_processor = ImageProcessor('hidden1.bmp')
    print('BW reveal (first 10):', bw_processor.reveal_image()[:10])
    pixel_list = bw_processor.reveal_image()[:100]
    print(pix_to_img(pixel_list, (300, 300), 'L'))

if __name__ == '__main__':
    main()
