from PIL import Image
from steganography import Steganography
from  Text_in_Image import *
class imagemerge():
    def merge(img1,img2):
        merged_image = Steganography.merge(Image.open(img1), Image.open(img2))
        return merged_image
    def unmerge(img):
        unmerged_image=Steganography.unmerge(Image.open(img))
        return unmerged_image
class textmerge():
    def Encrypt(message,image):
        encrypted=Encrypt(message,image)
        return encrypted
    def Decrypt(image):
        decrypted=Decrypt(image)
        return decrypted
        