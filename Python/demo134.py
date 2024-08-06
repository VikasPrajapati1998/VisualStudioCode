class PlatformException(Exception):
    """Incompatible platform."""


def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise PlatformException("Function is only execute in linux system.")
    print("Doing Linux things.")


if __name__ == "__main__":
    linux_interaction()
