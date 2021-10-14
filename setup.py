import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="backupy2win",
    version="0.0.0.1",
    author="Cristian Penteado",
    author_email="cristianpenteado@protonmail.ch",
    description="simple file and folder backup for windows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cristianpdev/backupy2win",
    project_urls={
        "Bug Tracker": "https://github.com/cristianpdev/backupy2win/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "backupy2win"},
    packages=setuptools.find_packages(where="backupy2win"),
    python_requires=">=3.9.7",
)