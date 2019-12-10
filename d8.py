import numpy as np
from PIL import Image


def d8_1(data):
    width = 25
    height = 6
    layer_size = width * height
    layers = [[int(n) for n in data[i:i + layer_size]] for i in range(0, len(data), layer_size)]
    counts = {}
    for layer in layers:
        counts[layer.count(0)] = layer.count(1) * layer.count(2)
    return min(counts.items(), key=lambda x: x[0])[1]
 
def d8_2(data):
    width = 25
    height = 6
    layer_size = width * height
    for w in range(0, len(data), width):
        layer = [[]]
    layers = [[int(n) for n in data[i:i + layer_size]] for i in range(0, len(data), layer_size)]
    image = []
    for w in range(width):
        row = []
        for h in range(height):
            for layer in layers:
                pixel = layer[w + (h * width)]
                if pixel == 0:
                    row.append(0)
                    break
                if pixel == 1:
                    row.append(255)
                    break
        image.append(row)
    arr = np.array(image, dtype=np.uint8)
    # Not 100% sure why, but flipping and rotating is required
    arr = np.rot90(arr, 3)
    arr = np.fliplr(arr)
    img = Image.fromarray(arr)
    img.show()
    img.save("d8.png")

# My input
with open("d8.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Part 1
print(f"Part 1 {d8_1(data)}")

# Part 2
print(f"Part 2 {d8_2(data)}")
