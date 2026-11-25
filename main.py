"""Entry for make.fun bounty 'Sum up 24 November's world news in one image'.

Writes the pre-made image to /output/entry.png.
Deterministic, no network: it only copies the bundled image.png byte-for-byte.
The bundled file holds JPEG data under the .png name, as the rules allow
(a file is told apart by its first bytes); the copy keeps those bytes.
Python 3.13, no third-party dependencies.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "image.png"
OUT = Path("/output/entry.png")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
