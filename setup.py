from setuptools import find_packages, setup


def get_requirement(file_path:str) ->list:
    """
    This function will return the list of requirements
    """
    requires = []
    with open(file_path) as f:
        requires = f.readlines()
        [r.replace("\n","") for r in requires]

    return requires

setup(
    name="mlproject",
    version="0.0.1",
    author="Abhishek",
    author_email="abhishekiitr999@gmail.com",
    packages=find_packages(),
    requires=get_requirement("requirements.txt")
)