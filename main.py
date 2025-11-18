from parser import get_args
from qemu import run_qemu

if __name__ == '__main__':

    args = get_args()

    run_qemu(
        image_path=args.image,
        vm_start=args.start,
        arch=args.arch,
        cpu=args.cpu,
        disk_name=args.disk,
        use_kvm=args.no_kvm,
        enable_io_uring=args.io_uring
    )
