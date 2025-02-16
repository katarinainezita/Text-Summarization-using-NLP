# import library
# untuk menangani path file dan direktori
import os 
from pathlib import Path 

# untuk mencatat log selama proses eksekusi
import logging

# konfigurasi logging tujuannya untuk mencatat status proses pembuatan file dan debugging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# nama project
project_name = "textSummarization"

# daftar file yang akan dibuat
list_of_files = [
    ".github/workflows/.gitkeep", # untuk github action (CI/CD)
    f"src/{project_name}/__init__.py", # package utama
    f"src/{project_name}/components/__init__.py", # komponen proyek
    f"src/{project_name}/utils/__init__.py", # utility functions
    f"src/{project_name}/utils/common.py", # file untuk fungsi umum
    f"src/{project_name}/logging/__init__.py", # logging untuk proyek
    f"src/{project_name}/config/__init__.py", # konfigurasi proyek
    f"src/{project_name}/config/configuration.py", # file konfigurasi 
    f"src/{project_name}/pipeline/__init__.py", # pipeline proyek
    f"src/{project_name}/entity/__init__.py", # struktur data proyek
    f"src/{project_name}/constants/__init__.py", # konstanta proyek
    "config/config.yaml", # file konfigurasi berbasis yaml
    "params.yaml", # file parameter proyek
    "app.py", # file utama aplikasi 
    "main.py", # entry point proyek
    "Dockerfile", # file docker untuk containerization
    "requirements.txt", # dependencies proyek
    "setup.py", # script untuk instalasi proyek sebagai package
    "research/trials.ipynb" # notebook untuk eksplorasi
    
]

# iterasi melalui daftar file
for filepath in list_of_files:
    
    # mengambil setiap file dari list_of_files dan mengubahnya menjadi path object 
    # untuk mempermudah manipulasi path
    filepath = Path(filepath)

    # memisahkan direktori dan nama file
    filedir, filename = os.path.split(filepath)

    # membuat direktori jika belum ada
    # cek apakah filedirnya tidak kosong, kalau kosong berarti langsung buat filenya di root  
    if filedir != "":
        # membuat folder filedir jika belum ada
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # cek apakah file belum ada atau file kosong 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    # jika file sudah ada
    else:
        logging.info(f"{filename} is already exists.")