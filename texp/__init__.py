"""texp - LaTeX source privacy protector: strip stylistic fingerprints from .tex files before sharing."""

__version__ = "0.1.0"

from .obfuscator import Obfuscator
from .cli import main
