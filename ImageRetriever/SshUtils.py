import paramiko
from scp import SCPClient
import os

def create_ssh_client(server, port, utilizator, parola):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, utilizator, parola)
    return client

def download_folder(scp, client_ssh, folder_remote, folder_local):
    os.makedirs(folder_local, exist_ok=True)
    
    stdin, stdout, stderr = client_ssh.exec_command(f'ls {folder_remote}')
    fisiere = stdout.read().decode().split()
    
    for fisier in fisiere:
        cale_fisier_remote = f"{folder_remote}/{fisier}"
        cale_fisier_local = os.path.join(folder_local, fisier)
        
        stdin, stdout, stderr = client_ssh.exec_command(f'if [ -d {cale_fisier_remote} ]; then echo "dir"; else echo "file"; fi')
        tip_fisier = stdout.read().decode().strip()
        
        if tip_fisier == "dir":
            download_folder(scp, client_ssh, cale_fisier_remote, cale_fisier_local)
        else:
            if not os.path.exists(cale_fisier_local):
                print(f"Se descarcă {cale_fisier_remote} la {cale_fisier_local}")
                try:
                    scp.get(cale_fisier_remote, cale_fisier_local)
                    print(f"Descărcat cu succes {fisier}.")
                except Exception as e:
                    print(f"Eșuat să descarce {fisier}: {e}")

def download_images(client_ssh, cale_remote, cale_local, proceseaza_si_trimite_imagine_din_folder, api_url):
    with SCPClient(client_ssh.get_transport()) as scp:
        stdin, stdout, stderr = client_ssh.exec_command(f'ls {cale_remote}')
        foldere = stdout.read().decode().split()
        
        if foldere:
            for folder in foldere:
                if folder.endswith('_files'):
                    folder_remote = f"{cale_remote}/{folder}"
                    folder_local = os.path.join(cale_local, folder)
                    if not os.path.exists(folder_local):
                        print(f"Se descarcă folder {folder_remote} la {folder_local}")
                        download_folder(scp, client_ssh, folder_remote, folder_local)
                        print(f"Descărcat cu succes folder {folder}. Se șterge de pe serverul remote.")
                        client_ssh.exec_command(f'rm -r {folder_remote}')
                        proceseaza_si_trimite_imagine_din_folder(folder_local, api_url)
                    else:
                        print(f"Folderul {folder_local} există deja. Se sare peste descărcare.")
        else:
            print("Nu s-au găsit foldere pentru descărcare.")
