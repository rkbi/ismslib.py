from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ismslib',
    version='2.1',
    packages=['ismslib'],
    url='https://github.com/rkbi/ismslib.py',
    license='GPLv3',
    author='Rakibul Islam',
    author_email='rkbssl@outlook.com',
    description='Very simple and easy to use library for integrating SSLWireless SMS API.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests', 'xmltodict'],
    keywords=['sslwireless', 'sms', 'isms', 'ismslib', 'official', 'api'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.6'
)
