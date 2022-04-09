import subprocess


SCRIPTS_ROOT_PATH = "/kaggle/cross-view-localization-bag/"


def generate_dsm_descriptors():
    print("Generating DSM descriptors...")
    return subprocess.Popen(
        ["python", f"{SCRIPTS_ROOT_PATH}/DSM/script/generate_descriptors.py"],
        shell=True,
    )


def generate_siam_fca_net_descriptor():
    print("Generating Siam-FCANet descriptors...")
    return subprocess.Popen(
        ["python", f"{SCRIPTS_ROOT_PATH}/Siam-FCANet/generate_sat_descriptors.py"],
        shell=True,
    )


def generate_l2ltr_descriptor():
    print("Generating L2LTR descriptors...")
    return subprocess.Popen(
        ["python", f"{SCRIPTS_ROOT_PATH}/L2LTR/generate_sat_descriptors.py"], shell=True
    )


def generate_descriptors():
    p1 = generate_dsm_descriptors()
    p2 = generate_siam_fca_net_descriptor()
    p3 = generate_l2ltr_descriptor()
    
    for p in (p1, p2, p3):
        p.wait() 


if __name__ == "__main__":
    generate_descriptors()
