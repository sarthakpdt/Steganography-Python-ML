# 🖼️ Image Steganography using RGB Pixel Manipulation (LSB Method)

## 📌 Overview
This project implements an **Image Steganography System** that allows you to hide a secret text message inside an image using the **Least Significant Bit (LSB) modification technique** on **RGB pixels**. The main goal is to securely embed text inside images while keeping the image visually unchanged.

The project supports both:
- **Encoding** (Hide text inside an image)
- **Decoding** (Extract hidden text from the modified image)

---

## 🎯 Objectives
- Hide text securely inside an image without visibly altering the image.
- Use **RGB pixel LSB modification** to embed the message.
- Decode the message with pixel-by-pixel extraction.
- Maintain image quality as close as possible to the original.

---

## ⚙️ Method Used

### 🔹 Encoding
1. Convert the text message into **binary**.
2. Traverse image pixels (R, G, B channels).
3. Replace the **Least Significant Bit** of each RGB channel with message bits.
4. Use a special flag to indicate the **end of the message**.
5. Save the modified image as the **stego image**.

### 🔹 Decoding
1. Read pixel RGB values from the stego image.
2. Extract the **LSB** of each color channel in sequence.
3. Convert the binary sequence back into characters.
4. Stop when the **end flag** bit is reached.
5. Display the recovered secret message.

---

## 🧱 Requirements
Make sure the following packages are installed:
```bash
pip install pillow
```
## ▶️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Image-Steganography.git
cd Image-Steganography
```
```
2. Run the Program
python stegano.py

🎮 Usage

When you run the program, you will see a menu:

Option	Description
1	Encode a secret message inside an image
2	Decode the hidden message from a stego image
✅ Encoding Example
Choose an option (1/2): 1
Enter input image path: original.png
Enter output image name: stego.png
Enter the message to hide: This is a secret!
Message encoded successfully into 'stego.png'

✅ Decoding Example
Choose an option (1/2): 2
Enter stego image path: stego.png
Decoded message:
This is a secret!

📝 Notes

Use PNG format to avoid image compression artifacts.

Ensure the image has enough pixels to store the full message.

The output image may look slightly different due to RGB LSB modification, but the change is usually visually unnoticeable.

🙌 Acknowledgment

This project was developed as part of learning and research in Cryptography & Steganography.

📝 License

This project is intended for educational use only. Do not use it for illegal or malicious activities.


---

If you want, I can now **add:**
- A professional **Abstract**
- **Block Diagram / Workflow Diagram**
- **Sample screenshots**
- **References section**

Just tell me: **Do you want your README to look more academic or more industry/professional?**
```

```bash
pip install pillow
