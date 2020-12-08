from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ismslib',
    version='2.0b1',
    packages=['ismslib'],
    url='https://github.com/rkbi/ismslib.py',
    license='GPLv3',
    author='Rakibul Islam',
    author_email='rkbssl@outlook.com',
    description='Library for using SSLWireless iSMS API. The goal is to provide a very easy-to-use interface.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests', 'xmltodict'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
