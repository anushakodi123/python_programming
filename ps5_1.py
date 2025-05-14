from PIL import Image

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
    
    def pix_to_img(pixel_list, size, mode):
        img = Image.new(mode, size)
        img.putdata(pixel_list)

        return img
    
    def make_matrix(color):
        """Return transformation matrix for a colorblindness type."""
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
        result = []
        for i in range(3):
            row_sum = 0
            for j in range(3):
                row_sum += matrix[i][j] * vector[j]
            result.append(row_sum)
        return result
    
    def filter(pixels_list, color):
        if color == None:
            return pixels_list
        matrix = ImageProcessor.make_matrix(color)
        transformed = []
        for pixel in pixels_list:
            transformed_pixel = ImageProcessor.matrix_multiply(matrix, pixel)
            clamped_pixel = tuple(max(0, min(255, int(round(i)))) for i in transformed_pixel)
            transformed.append(clamped_pixel)

        return transformed




processor = ImageProcessor('hidden2.bmp')
pixels = processor.get_pixels()
print('First 10 pixels: ', pixels[:10])
print('mode of the image: ', processor.get_mode())
print('size of the image: ', processor.get_size())
new_image = ImageProcessor.pix_to_img(pixels, processor.get_size(), processor.get_mode())

new_image.show()

pixels = [(120, 200, 150), (30, 60, 90), (255, 100, 50)]
filtered_pixels = ImageProcessor.filter(pixels, 'red')
print(filtered_pixels)
