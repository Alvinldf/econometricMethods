import codecs 
from setuptools import setup, find_packages
import os


PATH = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(PATH, "README.md"), encoding="utf-8") as file:
    long_description = "\n" + file.read()

VERSION = '0.0.0.1'
DESCRIPTION = 'Economic models'
LONG_DESCRIPTION = 'Here some formulas to use in some economic models'

setup(
        name="econometricMethodsESAN",
        version=VERSION,
        author="Alvin Sulca Vega",
        author_email="<alvinldf@gmail.com>",
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=[
            'cycler',
            'Cython',
            'joblib',
            'kiwisolver',
            'matplotlib',
            'numpy',
            'pandas',
            'patsy',
            'Pillow',
            'pmdarima',
            'pyparsing',
            'python-dateutil',
            'pytz',
            'scikit-learn',
            'scipy',
            'seaborn',
            'six',
            'statsmodels',
            'threadpoolctl',
            'urllib3',
            'bleach',
            'certifi',
            'cffi',
            'chardet',
            'colorama',
            'cryptography',
            'cycler',
            'Cython',
            'docutils',
            'idna',
            'importlib-metadata',
            'jeepney',
            'joblib',
            'kiwisolver',
            'matplotlib',
            'numpy',
            'packaging',
            'pandas',
            'patsy',
            'Pillow',
            'pkginfo',
            'pmdarima',
            'pycparser',
            'Pygments',
            'pyparsing',
            'python-dateutil',
            'pytz',
            'readme-renderer',
            'requests',
            'requests-toolbelt',
            'rfc3986',
            'scikit-learn',
            'scipy',
            'seaborn',
            'SecretStorage',
            'six',
            'statsmodels',
            'threadpoolctl',
            'tqdm',
            'twine',
            'urllib3',
            'webencodings',
            'zipp'
            ],
        keywords=['python'],
        classifiers=[
                "Development Status :: 1 - Planning",
                "Intended Audience :: Developers",
                "Programming Language :: Python :: 3",
                "Operating System :: Unix",
                "Operating System :: MacOS :: MacOS X",
                "Operating System :: Microsoft :: Windows",
                ]

)



