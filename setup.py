import setuptools

def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

setuptools.setup(    
    name="threadsnake",
    version=readfile("src/threadsnake/version.txt"),
    author="Erick Fernando Mora Ramirez",
    author_email="erickfernandomoraramirez@gmail.com",
    description="A tiny experimental server-side express-like library",
    long_description=readfile("src/threadsnake/README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/codeRookieErick/threadsnake",
    project_urls={
        "Bug Tracker": "https://dev.moradev.dev/threadsnake/issues/",
        "Documentation": "https://dev.moradev.dev/threadsnake/documentation/",
        "Examples": "https://dev.moradev.dev/threadsnake/examples/",
    },
    package_data={
        "":["*.txt"]
    },
    classifiers=[
    "Programming Language :: Python :: 3",
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)