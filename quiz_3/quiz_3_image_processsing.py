# 1) imports
import numpy as np
import matplotlib.pyplot as plt
import skimage.io
import skimage.color

# 2) Load image
image = skimage.io.imread("https://imagej.net/images/leaf.jpeg")

# 3) Display image
plt.imshow(image)
plt.show()

# 4) Convert to grayscale
gray = skimage.color.rgb2gray(image)  #

# 5) Display gray image
plt.imshow(gray, cmap="gray")
plt.show()

# 6) Apply threshold
gray_255 = gray * 255  # stretch 0.0 - 0.1 float values to 0.0 - 255.0 scale
gray_255 = gray_255.astype(np.uint8)  # convert from float to int


binary = gray_255 > 120
binary = binary.astype(np.uint8)  # converts true and false into 1 and 0

# 7) Display binary threshold image
plt.imshow(binary, cmap="gray")
plt.show()

# 8) Count how many bright pixels (value = 1) in image
bright_pixels_sum = np.sum(binary == 1)

# 9) Print pixel count
print(bright_pixels_sum)
