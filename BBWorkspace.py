# Choose target platform (hackerone, bugcrowd, hackenproof, yeswehack, ,external)

import os
import sys
import platform
import subprocess

# =========================================================
# AUTO WORKSPACE PATH
# =========================================================

SYSTEM = platform.system()
RELEASE = platform.uname().release.lower()

# Windows
if SYSTEM == "Windows":

    BASE_PATH = r"G:\Bug_Hunt_targets"

# WSL
elif "microsoft" in RELEASE:

    BASE_PATH = "/mnt/g/Bug_Hunt_targets"

# Linux / VPS / Parrot / Kali
else:

    BASE_PATH = os.path.expanduser(
        "~/Bug_Hunt_targets"
    )

# create workspace if not exists
os.makedirs(BASE_PATH, exist_ok=True)

# =========================================================
# PLATFORMS
# =========================================================

PLATFORMS = {
    "1": "HackerOne",
    "2": "Bugcrowd",
    "3": "Intigriti",
    "4": "YesWeHack",
    "5": "External",
    "6": "HackenProof",
    "7": "Immunefi",
    "8": "Open Bug Bounty",
    "9": "Cobalt",
    "10": "Yogosha",
    "11": "Detectify",
    "12": "Federacy",
    "13": "SafeHats",
    "14": "BountyFactory",
    "15": "Bug Bounty Switzerland",
    "16": "Synack",
    "99": "Other"
}

# =========================================================
# OPEN FOLDER
# =========================================================

def open_folder(path):

    path = os.path.abspath(path)

    try:

        # Windows
        if SYSTEM == "Windows":
            os.startfile(path)

        # WSL
        elif "microsoft" in RELEASE:
            subprocess.Popen(["explorer.exe", path])

        # Linux Desktop
        else:
            subprocess.Popen(["xdg-open", path])

    except:
        pass


# =========================================================
# SELECT PLATFORM
# =========================================================

def select_platform():

    print("\n========== Platforms ==========\n")

    for key, value in PLATFORMS.items():
        print(f"{key}. {value}")

    choice = input("\nChoose platform: ").strip()

    # OTHER
    if choice == "99":

        custom_platform = input(
            "\nEnter custom platform name: "
        ).strip()

        if not custom_platform:
            print("[-] Invalid platform")
            sys.exit()

        return custom_platform

    if choice not in PLATFORMS:
        print("[-] Invalid choice")
        sys.exit()

    return PLATFORMS[choice]


# =========================================================
# CREATE TARGET
# =========================================================

def create_target(platform, target):

    target_path = os.path.join(
        BASE_PATH,
        platform,
        target
    )

    folders = [
        "Assets",
        "Recon",
        "Results",
        "Screenshots",
        "Notes"
    ]

    for folder in folders:

        os.makedirs(
            os.path.join(target_path, folder),
            exist_ok=True
        )

    print("\n[+] Created Target:")
    print(target_path)

    open_folder(target_path)


# =========================================================
# MAIN
# =========================================================

def main():

    print(f"\n[Workspace]")
    print(BASE_PATH)

    # =====================================================
    # DIRECT MODE
    # python bb.py hackerone paypal
    # =====================================================

    if len(sys.argv) >= 3:

        platform = sys.argv[1]
        target = " ".join(sys.argv[2:])

        create_target(
            platform,
            target
        )

        return

    # =====================================================
    # INTERACTIVE MODE
    # =====================================================

    platform = select_platform()

    target = input(
        "\nEnter target name: "
    ).strip()

    if not target:
        print("[-] Invalid target")
        return

    create_target(
        platform,
        target
    )


if __name__ == "__main__":
    main()