import torch
import torch.nn as nn
from PIL import Image
import numpy as np
import torchvision.transforms as transforms

# ============================
# 1) CNN MODELS (ENCODER + DECODER)
# ============================

class Encoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.image_conv = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1), nn.ReLU(),
            nn.Conv2d(64, 64, 3, padding=1), nn.ReLU()
        )
        self.msg_conv = nn.Sequential(
            nn.Conv2d(1, 64, 3, padding=1), nn.ReLU()
        )
        self.merge = nn.Sequential(
            nn.Conv2d(128, 64, 3, padding=1), nn.ReLU(),
            nn.Conv2d(64, 3, 3, padding=1)
        )

    def forward(self, image, message):
        img_feat = self.image_conv(image)
        msg_feat = self.msg_conv(message)
        combined = torch.cat((img_feat, msg_feat), dim=1)
        return self.merge(combined)


class Decoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.decode = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1), nn.ReLU(),
            nn.Conv2d(64, 1, 3, padding=1)
        )

    def forward(self, stego):
        return self.decode(stego)


# ============================
# 2) LOAD IMAGE (64×64)
# ============================

image_path = "input.png"    
image = Image.open(image_path).convert("RGB").resize((64, 64))
transform = transforms.ToTensor()
image = transform(image).unsqueeze(0)

# ============================
# 3) TAKE USER MESSAGE + CONVERT TO BINARY
# ============================

message = input("Enter the secret message to hide: ")

binary = ''.join(format(ord(c), '08b') for c in message)

if len(binary) > (64*64):
    raise ValueError("Message is too long to hide in this image")

binary = binary.ljust(64*64, '0')
binary_array = np.array([int(b) for b in binary]).reshape(1,1,64,64)
message_tensor = torch.tensor(binary_array).float()

# ============================
# 4) TRAIN
# ============================

encoder = Encoder()
decoder = Decoder()

optimizer = torch.optim.Adam(
    list(encoder.parameters()) + list(decoder.parameters()), lr=0.001
)

loss_image = nn.MSELoss()
loss_msg = nn.BCEWithLogitsLoss()

for epoch in range(300):
    raw_stego = encoder(image, message_tensor)
    stego = image + (raw_stego - image) * 0.01   # KEY FIX FOR CLEAR IMAGE

    extracted = decoder(stego)

    li = loss_image(stego, image)
    lm = loss_msg(extracted, message_tensor)
    loss = li + 10*lm

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print(f"Epoch: {epoch} Loss: {loss.item():.6f}")

# ============================
# 5) SAVE STEGO IMAGE
# ============================

stego_img = stego.detach().squeeze().permute(1,2,0).numpy()
stego_img = (stego_img * 255).clip(0,255).astype(np.uint8)
Image.fromarray(stego_img).save("stego_output.png")

print("\n✅ Message successfully hidden inside: stego_output.png")

# ============================
# 6) DECODE MESSAGE
# ============================

extracted = decoder(stego).detach().squeeze().numpy()
extracted = 1 / (1 + np.exp(-extracted))
extracted = (extracted > 0.5).astype(int).flatten()

decoded_bits = ''.join(str(b) for b in extracted)

chars = []
for i in range(0, len(decoded_bits), 8):
    byte = decoded_bits[i:i+8]
    if int(byte, 2) == 0:
        break
    chars.append(chr(int(byte, 2)))

final_message = ''.join(chars)

print("\n🔓 Extracted Message:")
print(final_message)
