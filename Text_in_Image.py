from PIL import Image
import numpy as np
def Encrypt(message,image):
    img=Image.open(image,'r')
    width , height = img.size
    total_pixels=width*height
    array = np.array(list(img.getdata()))
    message=message+'###'
    b_message =''.join(format(ord(i), '08b') for i in  message)
    required_pixels=len(b_message)
    if required_pixels > total_pixels :
        print('Your message is too lengthy....Need larger image size to encode your message')
    else:
        index = 0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < required_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index],2)
                    index += 1
    if img.mode =="RGB":
        array = array.reshape(height, width,3)
    else:
        array=array.reshape(height,width,4)
    enc_img = Image.fromarray(array.astype('uint8'), img.mode)
    return enc_img
def Decrypt(image):
    img=Image.open(image,'r')
    width,height=img.size
    array=np.array(list(img.getdata()))
    total_pixels=width*height
    hidden_bits=""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])
    hidden_bits = [hidden_bits[i:i + 8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-3:] == "###":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "###" in message:
        return "Hidden message:"+ message[:-3]
    else:
        return "No Hidden Message Found"
def Main():
    print("1: Encode")
    print("2: Decode")

    func = input()

    if func == '1':
        print('If your file is not in Png type <filename>.png')
        name=input()
        print("Enter Original file name along with Extension")
        image = input()
        Image.open(image).save(name)
        print("Enter Message to Hide")
        message = input()
        print("Enter Destination Image Path")
        dest = input()
        print("Encoding...")
        Encrypt(message,name)

    elif func == '2':
        print("Enter Source Image Path")
        image = input()
        print("Decoding...")
        Decrypt(image)

    else:
        print("ERROR: Invalid option chosen")

if __name__ == '__main__':
    Main()
