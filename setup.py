import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = "Chest-CT-Classification-MLflow-DVC"
AUTHOR_USER_NAME = "vindhyaregonda"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "vindhya22208@iiitd.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A template python package for CNN classifier App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    )