# BBWorkspace

`BBWorkspace.py` is a simple Python tool for creating and organizing Bug Bounty target workspaces automatically.

Supports:

* Windows
* WSL
* Linux
* VPS
* Parrot OS
* Kali Linux

---

# Features

* Auto-detect operating system
* Automatic workspace path selection
* Interactive mode
* Direct CLI mode
* Auto-create target folders
* Auto-open created workspace
* Multi-platform support
* Organized Bug Bounty structure

---

# Workspace Structure

```text
Bug_Hunt_targets/
└── HackerOne/
    └── paypal/
        ├── Assets/
        ├── Recon/
        ├── Results/
        ├── Screenshots/
        └── Notes/
```

---

# Supported Platforms

* HackerOne
* Bugcrowd
* Intigriti
* YesWeHack
* Synack
* HackenProof
* Immunefi
* External
* Other (custom platform)

---

# Default Workspace Paths

The script automatically detects the environment and uses the correct workspace path.

## Windows

```text
G:\Bug_Hunt_targets
```

## WSL

```text
/mnt/g/Bug_Hunt_targets
```

## Linux / VPS

```text
~/Bug_Hunt_targets
```

---

# Usage

## Interactive Mode

```bash
python BBWorkspace.py
```

Choose:

* Platform
* Target name

---

## Direct Mode

```bash
python BBWorkspace.py hackerone paypal
```

```bash
python BBWorkspace.py bugcrowd spotify
```

```bash
python BBWorkspace.py external tesla
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/0xShadowVoid/BBWorkspace.git
```

Enter the directory:

```bash
cd BBWorkspace
```

Run the script:

```bash
python3 BBWorkspace.py
```

---

# License

MIT License
