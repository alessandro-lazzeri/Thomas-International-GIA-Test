"""

GIA reasoning tests


sample some images
split in two groups (randomly)
rotate group 1 and mirror/rotate group 2
solution is # of group 1


"""
import random
import os
from PIL import Image


IMAGEPATH = "../data/spatialVisualizationImages"
NSAMPLES = 2

ROTATE = [90,180,270]
FLIP = ["LEFT_RIGHT","TOP_BOTTOM","TRANSPOSE"]

def make_new_image(image_path, degrees_to_rotate, type_of_flip):
    # rotate and flip
    original_image = Image.open(os.path.join(IMAGEPATH, image_path))

    if degrees_to_rotate == 90:
        rotation = Image.Transpose.ROTATE_90
    elif degrees_to_rotate == 180:
        rotation = Image.Transpose.ROTATE_180
    else:
        rotation = Image.Transpose.ROTATE_270

    if type_of_flip == "LEFT_RIGHT":
        flip = Image.Transpose.FLIP_LEFT_RIGHT
    elif type_of_flip == "TOP_BOTTOM":
        flip = Image.Transpose.FLIP_TOP_BOTTOM
    elif type_of_flip == "TRANSPOSE":
        flip = Image.Transpose.TRANSPOSE
    else:
        flip = None

    edited_image = original_image.transpose(rotation)
    if flip:
        edited_image = edited_image.transpose(flip)
    return original_image, edited_image



def makeSpatialVisualizationItem():

    #get and sample the images
    image_paths = os.listdir(IMAGEPATH)

    images = random.sample(image_paths,NSAMPLES)

    # randomly select if and which to mirror
    mirrors = random.sample([1,0],2)

    newImages = []

    # edit the images
    for image, mirror, in zip(images, mirrors):
        rotate = random.choice(ROTATE)
        if mirror == 1:
            flip = random.choice(FLIP)
        else:
            flip = None
        newImages.append(make_new_image(image, rotate, flip))

    return sum(mirrors), {"images" : newImages}

if __name__ == '__main__':

    for _ in range(3):
        print(makeSpatialVisualizationItem())
