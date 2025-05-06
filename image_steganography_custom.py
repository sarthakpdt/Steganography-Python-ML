#imports the Image module from the Pillow library to handle image loading and saving
from PIL import Image
#Converts a text message into a binary string.
#ord(c) gives ASCII of character c.
#format(..., '08b') converts it to 8-bit binary.
#Example: "H" → 01001000
def to_binary(message):
    return ''.join(format(ord(c), '08b') for c in message)

#Convert binary to message
#Splits the binary string into 8-bit chunks.
#Converts each chunk back to a character using chr() and int(..., 2).
def binary_to_text(binary_data):
    chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return ''.join(chars)

#Loads the input image.
#Extracts all pixels as a list of RGB tuples.
def encode_image(input_path, output_path, message):
    image = Image.open(input_path)
    pixels = list(image.getdata())
    #Converts message to binary.
    #Calculates total bits needed and how many pixels are required.
    binary_message = to_binary(message)
    total_bits = len(binary_message)
    required_pixels = (total_bits // 8) * 3 + 3
    #Throws an error if image is too small to hide the message.
    if required_pixels > len(pixels):
        raise ValueError("Image is too small to hold this message.")
    #Initialize indices and a new list for modified pixels
    pixel_index = 0
    bit_index = 0
    new_pixels = []
    #Processes 3 pixels (9 RGB values) at a time.
    while bit_index < total_bits:
        #Take 3 pixels (9 RGB values)
        current_pixels = []
        for _ in range(3):
            current_pixels.append(list(pixels[pixel_index]))
            pixel_index += 1
        #Loop through the first 8 RGB values and match them with message bits.
        for i in range(8):  # Modify first 8 values
            row = i // 3
            col = i % 3
            value = current_pixels[row][col]
            bit = int(binary_message[bit_index])
            # 0 -> even, 1 -> odd
            if bit == 0 and value % 2 != 0:
                value -= 1
            elif bit == 1 and value % 2 == 0:
                value += 1
            #Saves the modified value and moves to the next bit.
            current_pixels[row][col] = value
            bit_index += 1
        # Last value (9th) – flag: 0 (even) = continue, 1 (odd) = end
        if bit_index >= total_bits:
            if current_pixels[2][2] % 2 == 0:
                current_pixels[2][2] += 1  # Make odd to stop
        else:
            if current_pixels[2][2] % 2 != 0:
                current_pixels[2][2] -= 1  # Make even to continue

        # Add modified pixels
        for p in current_pixels:
            new_pixels.append(tuple(p))

    # Add remaining original pixels
    new_pixels.extend(pixels[pixel_index:])

    # Save new image
    encoded_image = Image.new(image.mode, image.size)
    encoded_image.putdata(new_pixels)
    encoded_image.save(output_path)
    print(f"Message encoded successfully into '{output_path}'.")

# Decode message from image
def decode_image(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    
    binary_data = ''
    pixel_index = 0
    #Reads 3 pixels (9 values) at a time.
    while pixel_index + 2 < len(pixels):
        current_pixels = []
        for _ in range(3):
            current_pixels.append(list(pixels[pixel_index]))
            pixel_index += 1
        #Rebuilds binary data using LSB (least significant bit) of each color channel.
        for i in range(8):
            row = i // 3
            col = i % 3
            value = current_pixels[row][col]
            binary_data += '1' if value % 2 != 0 else '0'

        #If 9th RGB value is odd, stop reading (end of message).
        if current_pixels[2][2] % 2 != 0:
            break
    #Converts binary data back to text and prints it.
    message = binary_to_text(binary_data)
    print("Decoded message:")
    print(message)


def main():
    #Simple user menu to choose between encoding and decoding.
    print("Image-Based Steganography (RGB Pixel Method)")
    print("1. Encode a message")
    print("2. Decode a message")
    choice = input("Choose an option (1/2): ")

    if choice == '1':
        input_img = input("Enter input image path (PNG recommended) or name of the image: ").strip()
        output_img = input("Enter output image path or name of the output image path: ").strip()
        secret = input("Enter the message to hide: ").strip()
        encode_image(input_img, output_img, secret)

    elif choice == '2':
        stego_img = input("Enter stego image path: ").strip()
        decode_image(stego_img)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
