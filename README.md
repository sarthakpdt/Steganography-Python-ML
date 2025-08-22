# 🖼️ Image Steganography (RGB Pixel Method)  

## 📌 Project Overview  
This project implements an **Image-Based Steganography system** using the **Least Significant Bit (LSB) method** on RGB pixel values.  

The system allows you to:  
- **Encode** (hide) a secret text message inside an image.  
- **Decode** (retrieve) the hidden message back from the image.  

It is a simple yet effective approach for secure communication using images.  

---

## 🎯 Objectives  
- Develop a program to **hide text inside images**.  
- Use **RGB pixel modification (LSB method)** for embedding data.  
- Provide a way to **decode hidden messages** from stego images.  
- Ensure the output image looks visually identical to the original.  

---

## ⚙️ Methodology  

### 🔹 Encoding Process  
1. Convert the secret message into **binary**.  
2. Traverse the image pixels in groups of 3.  
3. Modify the **Least Significant Bit (LSB)** of the RGB channels to store message bits.  
4. Use the **9th pixel value as a flag** to mark whether more data follows or not.  
5. Save the modified image as the **stego image**.  

### 🔹 Decoding Process  
1. Read the pixels of the stego image in the same order.  
2. Extract the **LSBs of RGB values** to reconstruct binary data.  
3. Stop reading when the flag bit indicates the end of the message.  
4. Convert the binary data back into text.  

---

## 📂 Example Workflow  

### ✅ Encoding  
- Input: `original.png`  
- Message: `"This is a secret message!"`  
- Output: `stego.png`  

### ✅ Decoding  
- Input: `stego.png`  
- Output: `"This is a secret message!"`  

---

## 📦 Requirements  

Make sure you have the following installed:  
- Python 3.x  
- Pillow (for image handling)  

Install dependencies with:  
```bash
pip install pillow
```

## How to Run
Clone the repository:

git clone https://github.com/your-username/Image-Steganography.git
cd Image-Steganography

Run the program:

python stegano.py

Select an option:

Enter 1 → To encode a message into an image.

Enter 2 → To decode a hidden message from a stego image.

## 📊 Sample Output

Encoding Example:

Image-Based Steganography (RGB Pixel Method)
1. Encode a message
2. Decode a message
Choose an option (1/2): 1
Enter input image path (PNG recommended) or name of the image: original.png
Enter output image path or name of the output image path: stego.png
Enter the message to hide: Hello World!
Message encoded successfully into 'stego.png'.


Decoding Example:

Image-Based Steganography (RGB Pixel Method)
1. Encode a message
2. Decode a message
Choose an option (1/2): 2
Enter stego image path: stego.png
Decoded message:
Hello World!

## 🙌 Acknowledgment

This project was developed as part of my exploration in Cryptography and Steganography.
Thanks to the open-source community for resources on LSB image steganography.

## 📝 License

This project is for educational purposes only. Do not use it for illegal or malicious activities.
```bash
pip install pillow
