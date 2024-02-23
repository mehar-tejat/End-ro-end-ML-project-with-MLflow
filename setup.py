import setuptools

# this read me file is to publish your project as package in pypi then this README.md is important, we are not publishing but keeping l;ocally but its imp to do so
with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME = "NLP-project-text-summariser"
AUTHOR_USER_NAME = "mehar-tejat"
SRC_REPO = "textsummariser"
AUTHOR_EMAIL = "meharteja.t@gmail.com"

setuptools.setup(

    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
)
