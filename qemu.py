import subprocess


def run_qemu(
    image_path: str | None = None,
    vm_start: bool = False,
    arch: str = "x86_64",
    cpu: str = "host",
    disk_name: str | None = None,
    use_kvm: bool = True,
    enable_io_uring: bool = False,
) -> None:
    """
    Run QEMU with specified parameters.

    Args:
        image_path: Path to installation ISO or VM disk image.
        vm_start: If True, start VM; if False, boot from ISO for installation.
        arch: CPU architecture (e.g., 'x86_64', 'arm64').
        cpu: CPU model or 'host' to use host CPU features.
        disk_name: Path to additional disk image.
        use_kvm: Whether to enable KVM acceleration.
        enable_io_uring: Enable io_uring support if available.
    """

    qemu_cmd = ["qemu-system-" + arch]

    # Выключаем KVM
    if not use_kvm:
        qemu_cmd.append("-enable-kvm")

    # Включаем io_uring
    if enable_io_uring:
        qemu_cmd += ["-object", "iouring-default"]

    # Указываем образ для установки или запуска
    if image_path:
        if vm_start:
            # Запуск ВМ с диском
            qemu_cmd += ["-drive", f"file={image_path},format=qcow2,if=virtio"]
        else:
            # Установка из ISO
            qemu_cmd += ["-cdrom", image_path, "-boot", "d"]

    # Указываем CPU
    if cpu:
        qemu_cmd += ["-cpu", cpu]

    # Если задан дополнительный диск
    if disk_name:
        qemu_cmd += ["-drive", f"file={disk_name},format=qcow2,if=virtio"]

    # Печатаем команду и запускаем QEMU
    print("Запускается команда:", " ".join(qemu_cmd))
    subprocess.run(qemu_cmd)
