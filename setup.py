from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="texp",
    version="0.1.0",
    author="Sylvan",
    author_email="sylvan@example.com",
    description="LaTeX source privacy protector: remove stylistic fingerprints from .tex files before sharing, without changing PDF output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sylvanlisayhi-cyber/latex-privacy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    python_requires=">=3.7",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "texp=texp.cli:main",
        ],
    },
)
