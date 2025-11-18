import subprocess


def run_qemu(image_path=None, vm_start=False, arch='x86_64', cpu='host', disk_name=None, use_kvm=True, enable_io_uring=False):
    qemu_cmd = ['qemu-system-' + arch]

    # Выключаем KVM
    if not use_kvm:
        qemu_cmd.append('-enable-kvm')

    # Включаем io_uring
    if enable_io_uring:
        qemu_cmd += ['-object', 'iouring-default']

    # Указываем образ для установки или запуска
    if image_path:
        if vm_start:
            # Запуск ВМ с диском
            qemu_cmd += ['-drive', f'file={image_path},format=qcow2,if=virtio']
        else:
            # Установка из ISO
            qemu_cmd += ['-cdrom', image_path, '-boot', 'd']

    # Указываем CPU
    if cpu:
        qemu_cmd += ['-cpu', cpu]

    # Если задан дополнительный диск
    if disk_name:
        qemu_cmd += ['-drive', f'file={disk_name},format=qcow2,if=virtio']

    # Печатаем команду и запускаем QEMU
    print('Запускается команда:', ' '.join(qemu_cmd))
    subprocess.run(qemu_cmd)
