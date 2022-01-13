from PIL import Image
from steganograpy import Steganography
def unmerge(img):
    unmerged_image=Steganography.unmerge(Image.open(img))
    return unmerged_image.save('unmerged.png')
unmerge('output.jng')