#!/usr/bin/env python3
import subprocess


SCRIPTS_ROOT_PATH = "/kaggle/cross-view-localization-bag"


def generate_dsm_descriptors():
    print("Generating DSM descriptors...")
    return subprocess.check_call(
        ["python", f"{SCRIPTS_ROOT_PATH}/DSM/script/generate_descriptors.py"]
    )

def generate_l2ltr_descriptor():
    print("Generating L2LTR descriptors...")
    return subprocess.check_call(
        ["python", f"{SCRIPTS_ROOT_PATH}/L2LTR/generate_descriptors.py"]
    )


def generate_coming_dte_descriptor():
    print("Generating Coming-D2E descriptors...")
    return subprocess.check_call(
        ["python", f"{SCRIPTS_ROOT_PATH}/comingdowntoearth/generate_descriptors.py"]
    )


def generate_safa_descriptor():
    print("Generating SAFA descriptors...")
    return subprocess.check_call(
        ["python", f"{SCRIPTS_ROOT_PATH}/SAFA/script/generate_descriptors.py"]
    )


def generate_descriptors():
    p1 = generate_dsm_descriptors()
    p3 = generate_l2ltr_descriptor()
    p4 = generate_coming_dte_descriptor()
    p5 = generate_safa_descriptor()


if __name__ == "__main__":
    generate_descriptors()
