import pygame

class Filter:
    def __init__(self, img):
        self.image = img

    def LoadImage(self):
        # load the image and convert to numpy array
        img_load = pygame.image.load(self.image).convert_alpha()
        self.arr = pygame.surfarray.array3d(img_load)

    def SaveImage(self, destination):
        surface = pygame.surfarray.make_surface(self.arr) # convert array back to pygame surface
        pygame.image.save(surface, destination) # save the surface as png

class GrayScaleTransformer(Filter):
    def __init__(self, img):
        super().__init__(img)

    def transform(self):
        # convert to grayscale using for loops
        for i in range(0, len(self.arr)): # column number from 0 to 15
            for j in range(0, len(self.arr[i])): # row number from 0 to 15
                r, g, b = self.arr[i][j] # get rgb values for the pixel
                avg = r/3  + g/3  + b/3 # calculate average
                self.arr[i][j] = [avg, avg, avg] # set rgb values to average

    def SaveImage(self, destination):
        return super().SaveImage(destination)
    
    def LoadImage(self):
        return super().LoadImage()

class MyUltraTransformer(Filter):
    def __init__(self, img):
        super().__init__(img)

    def transform(self):
        # convert to grayscale using for loops
        for i in range(0, len(self.arr)): # column number from 0 to 15
            for j in range(0, len(self.arr[i])): # row number from 0 to 15
                r, g, b = self.arr[i][j] # get rgb values for the pixel
                self.arr[i][j] = [g, b, r] # mix rgb values
        
        #mix pixels
        n = len(self.arr)
        m = len(self.arr[0])
        for i in range(0, n):
            for j in range(0, m): 
                self.arr[i][j], self.arr[n-i-1][m-j-1] = self.arr[n-i-1][m-j-1], self.arr[i][j]

    def SaveImage(self, destination):
        return super().SaveImage(destination)
    
    def LoadImage(self):
        return super().LoadImage()


def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 400))

    # little pic
    image_file = "data/test_cut.png"

    # to gray

    transformer = GrayScaleTransformer(image_file)

    transformer.LoadImage()
    transformer.transform()
    transformer.SaveImage("data/test_gray_little.png")

    # shuffle channels

    transformer2 = MyUltraTransformer(image_file)

    transformer2.LoadImage()
    transformer2.transform()
    transformer2.SaveImage("data/test_ultra_little.png")


    # # big pic
    image_file = "data/test_cut_big.png"

    # # to gray

    transformer = GrayScaleTransformer(image_file)

    transformer.LoadImage()
    transformer.transform()
    transformer.SaveImage("data/test_gray_big.png")

    # # shuffle channels

    transformer2 = MyUltraTransformer(image_file)

    transformer2.LoadImage()
    transformer2.transform()
    transformer2.SaveImage("data/test_ultra_big.png")

if __name__ == '__main__':
    main()