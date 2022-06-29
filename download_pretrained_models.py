from multiprocessing import Process
import os
import zipfile
import requests

import gdown


MODELS_DIR = "/kaggle/working/models"
DSM_DIR = f"{MODELS_DIR}/DSM"
L2LTR_DIR = f"{MODELS_DIR}/L2LTR"
COMING_D2E_DIR = f"{MODELS_DIR}/coming_dte"
SAFA_DIR = f"{MODELS_DIR}/SAFA"


def create_models_dirs():
    os.makedirs(MODELS_DIR, exist_ok=True)
    os.makedirs(DSM_DIR, exist_ok=True)
    os.makedirs(L2LTR_DIR, exist_ok=True)
    os.makedirs(COMING_D2E_DIR, exist_ok=True)
    os.makedirs(SAFA_DIR, exist_ok=True)


def download_dsm():
    archive_path = "/kaggle/DSM_Model.zip"
    gdown.download(id="1jmBn6D6hfifKm6JYw0dc_WMRJ9bSLb5h", output=archive_path)

    with zipfile.ZipFile(archive_path, "r") as f:
        f.extractall(DSM_DIR)
    print("DSM Model Successfully Downloaded")

    os.remove(archive_path)


def download_l2ltr():
    archive_path = "/kaggle/EgoTR_model.zip"
    gdown.download(id="1IOiElf_8-9Dq7n8vTAOi3kq8QAriFAjp", output=archive_path)

    with zipfile.ZipFile(archive_path, "r") as f:
        f.extractall(L2LTR_DIR)
    print("L2LTR Model Successfully Downloaded")
    os.remove(archive_path)


def download_coming_dte():
    MODEL_NAME = "rgan_best_ckpt.pth"
    response = requests.get(
        "https://vision.in.tum.de/webshare/u/toker/coming_dte_ckp/cvact/rgan_best_ckpt.pth"
    )
    response.raise_for_status()  # ensure we notice bad responses

    with open(f"{COMING_D2E_DIR}/{MODEL_NAME}", "wb") as f:
        f.write(response.content)

    print("Toker Model Successfully Downloaded")
    


def download_safa():
    archive_path = "/kaggle/SAFA_Model.zip"
    gdown.download(id="1dH44xSMXCekih8-8CK1_x-76vrMj4whr", output=archive_path)

    with zipfile.ZipFile(archive_path, "r") as f:
        f.extractall(SAFA_DIR)

    print("SAFA Model Successfully Downloaded")
    os.remove(archive_path)



def download_models():
    create_models_dirs()

    download_commands = (
        download_dsm,
        download_l2ltr,
        download_coming_dte,
        download_safa,
    )
    download_processes = []

    for command in download_commands:
        p = Process(target=command)
        p.start()
        download_processes.append(p)

    for p in download_processes:
        p.join()


if __name__ == "__main__":
    download_models()
