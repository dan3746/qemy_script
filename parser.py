import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Запуск QEMU с параметрами")

    parser.add_argument("--image", type=str, help="Путь к образу (ISO или диск)")
    parser.add_argument("--start", action="store_true", help="Запустить ВМ (иначе установка)")
    parser.add_argument("--arch", type=str, default="x86_64", help="Архитектура (например x86_64, arm64)")
    parser.add_argument("--cpu", type=str, default="host", help="CPU")
    parser.add_argument("--disk", type=str, help="Имя дополнительного диска")
    parser.add_argument("--no-kvm", action="store_true", help="Отключить KVM")
    parser.add_argument("--io-uring", action="store_true", help="Включить io_uring (если поддерживается)")

    args = parser.parse_args()

    return args
