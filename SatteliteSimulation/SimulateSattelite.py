import os
import subprocess
from datetime import datetime
import random
import time

# Calea de bază unde sunt localizate folderele ROI
base_path = r"path"

# Listă pentru a stoca căile imaginilor
images = []

# Buclă prin folderele ROI
for i in range(1, 8):
    roi_path = os.path.join(base_path, "ROI_1000" + str(i))
    # Listează toate folderele din fiecare cale ROI
    if os.path.exists(roi_path):
        for folder in os.listdir(roi_path):
            folder_path = os.path.join(roi_path, folder)
            if os.path.isdir(folder_path):
                images.append(os.path.join(folder_path, 'S2L1C.tif'))

# Calea destinației
destination = "root@ip:/path"

# Calea către cheia SSH
ssh_key_path = r"key_path"

# Funcție pentru a transfera o imagine aleatorie
def transfer_random_image():
    if images:
        random_image_path = random.choice(images)
        if os.path.exists(random_image_path):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            dest_file_name = f"{timestamp}.tiff"
            scp_command = f"scp -i {ssh_key_path} {random_image_path} {destination}/{dest_file_name}"
            try:
                subprocess.run(scp_command, shell=True, check=True)
                print(f"Transferat cu succes {random_image_path} ca {dest_file_name}")
            except subprocess.CalledProcessError as e:
                print(f"Transferul a eșuat pentru {random_image_path}: {e}")
        else:
            print(f"Imaginea nu există: {random_image_path}")
    else:
        print("Nu s-au găsit imagini de transferat.")

#while True:

while True:
    transfer_random_image()
    time.sleep(1)
