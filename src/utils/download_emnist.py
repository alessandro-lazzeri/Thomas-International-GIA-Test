
from pathlib import Path
from PIL import Image
import random
#python -c "import emnist; emnist.ensure_cached_data()" # run in terminal to download dataset
from emnist import extract_training_samples

IMAGEPATH = Path(__file__).parent.parent.parent.joinpath("data\spatialVisualizationImages")

images, labels = extract_training_samples('balanced')

sampledImages = random.sample(list(images),100)

for name, img in enumerate(sampledImages):
    img = Image.fromarray(img)

    img.save(IMAGEPATH.joinpath("%s.png" % name))