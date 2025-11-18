# QEMU Launcher Python Script

This project is a Python script for conveniently launching virtual machines via QEMU with customizable parameters.

## Description

The script allows you to start QEMU with the following options:
- Specify an image for installation (ISO) or a disk image to run the virtual machine,
- Select the CPU architecture (x86_64, arm64, etc.),
- Choose the CPU model or settings (e.g., host for using the host CPU features),
- Provide an additional disk image,
- Enable or disable KVM hardware acceleration,
- Enable io_uring support if supported by your system and QEMU version.

## Usage

Run the script from the command line with parameters:

    python main.py --image /path/to/ubuntu.iso --start --arch x86_64 --cpu host --disk /path/to/disk.qcow2 --io-uring

### Main Parameters

- --image — path to the ISO image for installation or disk image for VM startup.
- --start — flag to start the VM; if not provided, the script will boot from ISO for installation.
- --arch — CPU architecture (default is `x86_64`).
- --cpu — CPU model or parameters (e.g., host to match host CPU).
- --disk — path to an additional disk image.
- --no-kvm — disable KVM hardware acceleration.
- --io-uring — enable io_uring support (if available).

## Requirements

- QEMU installed with commands like qemu-system-<arch> available.
- Python 3.
- KVM support enabled in the system for hardware acceleration.
- Linux kernel supporting io_uring, if you want to enable that feature.

## Linters and Code Quality Tools

This project uses the following tools to ensure code quality and style:

- flake8: for Python style checks (PEP8 compliance)
- mypy: for static type checking using Python annotations
- black: for automatic code formatting

## Setting Up Automatic Linting with pre-commit

To automate running linters before each git commit, this project uses the [pre-commit](https://pre-commit.com/) framework.

### Installation

Install pre-commit using pip:

    pip install pre-commit

Install the pre-commit git hooks:

    pre-commit install

You can manually run all hooks on all files with:

    pre-commit run –all-files