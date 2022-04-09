from multiprocessing import Process
import os
import zipfile

import gdown


MODLES_DIR = "/kaggle/working/models"
DSM_DIR = f"{MODLES_DIR}/DSM"
L2LTR_DIR = f"{MODLES_DIR}/L2LTR"
SiamFCANet_DIR = f"{MODLES_DIR}/Siam-FCANet"


def create_models_dirs():
    os.mkdir(MODLES_DIR)
    os.mkdir(DSM_DIR)
    os.mkdir(SiamFCANet_DIR)
    os.mkdir(L2LTR_DIR)


def download_dsm():
    archive_path = "/kaggle/DSM_Model.zip"
    gdown.download(id="1jmBn6D6hfifKm6JYw0dc_WMRJ9bSLb5h", output=archive_path)

    with zipfile.ZipFile(archive_path, "r") as f:
        f.extractall(DSM_DIR)

    os.remove(archive_path)


def download_siam_fca_net():
    gdown.download(
        id="11D3xEgwcnx3pe6Ipy2SAwZ1Vu4tv67LY",
        output=f"{SiamFCANet_DIR}/SFCANet_18.pth",
    )
    gdown.download(
        id="1qC39of4UMexg6WxfV2aQLg44avwDrvqx",
        output=f"{SiamFCANet_DIR}/SFCANet_18_VH.pth",
    )


def download_l2ltr():
    archive_path = "/kaggle/EgoTR_model.zip"
    gdown.download(id="1IOiElf_8-9Dq7n8vTAOi3kq8QAriFAjp", output=archive_path)

    with zipfile.ZipFile(archive_path, "r") as f:
        f.extractall(L2LTR_DIR)

    os.remove(archive_path)


def download_models():
    create_models_dirs()

    download_commands = (download_dsm, download_siam_fca_net, download_l2ltr)
    download_processes = []

    for command in download_commands:
        p = Process(target=command)
        p.start()
        download_processes.append(p)

    for p in download_processes:
        p.join()


if __name__ == "__main__":
    download_models()
