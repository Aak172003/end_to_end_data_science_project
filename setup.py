from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requiremnts = []
    # Open file which pass as path
    with open(file_path) as file_obj:
        # read line by line
        requiremnts = file_obj.readlines()

        # store final requiremnts after removing /n after last character
        final_requiremnts = [req.replace("\n", "") for req in requiremnts]

        # It will remove -e . from requirements file
        if HYPEN_E_DOT in requiremnts:
            final_requiremnts.remove(HYPEN_E_DOT)

        print("final_requiremnts ::::: ", final_requiremnts)

    return final_requiremnts


setup(
    name="mlproject",
    version="0.0.1",
    author="Aakash Prajapati",
    author_email="prajapatiaakash364@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
