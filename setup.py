import re
from setuptools import setup, find_packages


with open('base58check/__init__.py', 'rt') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

try:
    from m2r import parse_from_file
    long_description = parse_from_file('README.md')
except ImportError:
    with open('README.md') as fd:
        long_description = fd.read()


setup(
    name='base58check',
    version=version,
    description='Base58check encoding and decoding of binary data',
    long_description=long_description,
    keywords=[
        'base58',
        'base58check',
        'encoding',
        'decoding',
        'bitcoin',
        'altcoin',
    ],
    author='Joe Black',
    author_email='me@joeblack.nyc',
    maintainer='Joe Black',
    maintainer_email='me@joeblack.nyc',
    url='https://github.com/joeblackwaslike/base58check',
    download_url=(
        'https://github.com/joeblackwaslike/base58check/tarball/v%s' % version),
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: Security :: Cryptography',
        'Topic :: Text Processing',
        'Topic :: Utilities',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
