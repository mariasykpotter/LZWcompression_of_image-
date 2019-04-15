from PIL import Image
from grayscale import GrayscaleImage
from io import StringIO
import numpy as np
import random

N_ROWS = 1000
N_COLS = 1000


def compress(uncompressed):
    """
    Compress a string to a list of output symbols.
    :param uncompressed: str
    :return: list
    """
    # Build the dictionary.
    dict_size = 255
    dictionary = {chr(i): i for i in range(dict_size)}
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary.keys():
            w = wc
        else:
            result.append(dictionary[w])
            dict_size += 1
            dictionary[wc] = dict_size
            w = c
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    """
    Decompress a list of output values to a string.
    :param compressed: list
    :return: str
    """
    # Build the dictionary.
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
    return result.getvalue()


im = Image.open("eye.jpg")
im1 = Image.new('L', im.size, 'black')
# im1.show()
width, height = im.size
img = GrayscaleImage(N_ROWS, N_COLS)
pixels = ""
pixs = im.load()
for i in range(width):
    for j in range(height):
        k = im.getpixel((i, j))
        # print(k)
        img.setitem(i, j, k)
        pixs[i, j] = img.getitem(i, j)
# img1.clear(1)
for i in range(width):
    for j in range(height):
        # print(img1.getitem(i,j))
        if img.getitem(i, j):
            # print(img1.getitem(i, j))
            pixels += str(img.getitem(i, j)) + " "
        else:
            pixels += " "
    pixels += "\n"
compressed = []
overall = []
print(decompress(compress(pixels)))
im.save('new1.jpg', 'JPEG')
