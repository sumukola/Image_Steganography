# Image_Steganography 
This project is all about hiding personal/confidential information in an image.


# Image Structure : 
An image has thousands of pixels which gives out the colors . 
                  These pixels has 3 color values (RGB) Red,Green and Blue and RGBA as well , where A is the opacity of that pixel.
                  Each pixel contains values (8-bit value) depending on its type and depth.


# What is this application doing? : 
This Web App is generally taking some user text or user image to hide into another image. 



# How is it doing? : 
Basically there are two mediums users have thier data to hide in an image:

1:Text 

2:Image

1>Text : The user typed text is converted to a binary string , the string "image steaganograpy" in binary string is 
"110100111011011100001110011111001011000001110011111010011001011100111110000111011101101111110011111100101100001111000011010001111001"

Each character in the binary string is replaced with the LSB of RGB values.

The first three bits 110 is replace in the image pixels as :


First bit: 
    Suppose value of R before replacing : 11110000 , then R after replacing becomes : 11110001 
    
    
Second bit: 
    Suppose value of G before replacing : 10101010 , then G after replacing becomes : 10101011


Third bit:
    Suppose value of B before replacing : 11010100 , then B after replacing becomes : 11010101
    
    
This process is repeated for each bit in the binary string , after all the bit replacements the image is packed back. 

At the time of extracting the same image is unpacked and LSB values of each pixels are collected , convert them to binary string and back to its original string. 

The same process goes with the image to hide in another image.
