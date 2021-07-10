import codecs 
from setuptools import setup, find_packages
import os


PATH = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(PATH, "README.md"), encoding="utf-8") as file:
    long_description = "\n" + file.read()

VERSION = '0.0.1'
DESCRIPTION = 'Economic models'
LONG_DESCRIPTION = 'Here some formulas to use in some economic models'

setup(
        name="ecoform_alvin",
        version=VERSION,
        author="Alvin Sulca Vega",
        author_email="<alvinldf@gmail.com>",
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=long_description,
        packages=find_packages(),
        install_requires=[],
        keywords=['python'],
        classifiers=[
            "Development status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Programming language :: Python :: 3",
            "Operation System :: Unix",
            "Operation System :: MacOS :: MacOS X",
            "Operation System :: Microsoft :: Windows",
            ]
)



