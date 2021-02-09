from setuptools import setup, find_packages
from bluhood.version import __version__

VERSION = __version__

requirements = open('requirements.txt', 'r').read().splitlines()

setup(
    name='bluhood',
    packages=find_packages(),
    version=VERSION,
    license='MIT',
    description='Cryptography Module.',
    author='Victor Zoni',
    author_email='vczoni@gmail.com',
    url='https://github.com/vczoni/charcad',
    download_url=VERSION.join(
        ['https://github.com/vczoni/charcad/archive/v', '.tar.gz']),
    keywords=['STRING', 'CRYPTOGRAPHY', 'ENCRYPTION', 'DECRYPTION', 'BASIC'],
    install_requires=requirements,
    python_requires='>=3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
