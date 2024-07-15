import time
import os
from SshUtils import create_ssh_client, download_images
from ImageProcessing import process_and_send_image_from_folder

api_url = "https://localhost:50000/api/analize-results/create"

def main():
    server = 'ip'
    port = port
    user = 'user'
    password = 'password'
    remote_path = 'path'
    local_path = '.'
    interval = 1  # Time interval in seconds between checks
    
    # Ensure local path exists
    os.makedirs(local_path, exist_ok=True)

    # Create SSH client
    ssh_client = create_ssh_client(server, port, user, password)

    try:
        while True:
            download_images(ssh_client, remote_path, local_path, process_and_send_image_from_folder, api_url)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Oprirea descărcării continue.")
    finally:
        ssh_client.close()

if __name__ == "__main__":
    main()
