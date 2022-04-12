#!/usr/bin/env python3
import subprocess


SCRIPTS_ROOT_PATH = "/kaggle/cross-view-localization-bag"


def generate_dsm_descriptors():
    print("Generating DSM descriptors...")
    return subprocess.check_call(
        ["python", f"{SCRIPTS_ROOT_PATH}/DSM/script/generate_descriptors.py"]
    )


def generate_siam_fca_net_descriptor():
    print("Generating Siam-FCANet descriptors...")
    return subprocess.check_call(
        ["python", f"{SCRIPTS_ROOT_PATH}/Siam-FCANet/generate_sat_descriptors.py"]
    )


def generate_l2ltr_descriptor():
    print("Generating L2LTR descriptors...")
    return subprocess.check_call(
        ["python", f"{SCRIPTS_ROOT_PATH}/L2LTR/generate_sat_descriptors.py"]
    )

def generate_coming_dte_descriptor():
    print('Generating Coming-D2E descriptors...')
    return subprocess.check_call(
        ["python", f"{SCRIPTS_ROOT_PATH}/comingdowntoearth/generate_descriptors.py"]
    )


def generate_descriptors():
    p1 = generate_dsm_descriptors()
    p2 = generate_siam_fca_net_descriptor()
    p3 = generate_l2ltr_descriptor()
    p4 = generate_coming_dte_descriptor()


if __name__ == "__main__":
    generate_descriptors()
