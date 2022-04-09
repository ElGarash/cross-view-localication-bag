import subprocess


SCRIPTS_ROOT_PATH = "/kaggle/cross-view-localization-bag/"


def generate_dsm_descriptors():
    print("Generating DSM descriptors...")
    subprocess.check_call(
        ["python", f"{SCRIPTS_ROOT_PATH}/DSM/script/generate_descriptors.py"],
        shell=True,
    )


def generate_siam_fca_net_descriptor():
    print("Generating Siam-FCANet descriptors...")
    subprocess.check_call(
        ["python", f"{SCRIPTS_ROOT_PATH}/Siam-FCANet/generate_sat_descriptors.py"],
        shell=True,
    )


def generate_l2ltr_descriptor():
    print("Generating L2LTR descriptors...")
    subprocess.check_call(
        ["python", f"{SCRIPTS_ROOT_PATH}/L2LTR/generate_sat_descriptors.py"], shell=True
    )


def generate_descriptors():
    generate_dsm_descriptors()
    generate_siam_fca_net_descriptor()
    generate_l2ltr_descriptor()


if __name__ == "__main__":
    generate_descriptors()
