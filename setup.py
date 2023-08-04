import setuptools

with open("README.md","r",encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME =  "MLflow-Project"
AUTHOR_USER_NAME = "shek_abhi"
SRC_REPO = "mlflowProject"

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python package for ml app",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)