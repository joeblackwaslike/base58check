# Base58Check
[![Build Status](https://travis-ci.org/joeblackwaslike/base58check.svg?branch=master)](https://travis-ci.org/joeblackwaslike/base58check) [![Github Repo](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/joeblackwaslike/base58check) [![Pypi Version](https://img.shields.io/pypi/v/base58check.svg)](https://pypi.python.org/pypi/base58check) [![Pypi License](https://img.shields.io/pypi/l/base58check.svg)](https://pypi.python.org/pypi/base58check) [![Pypi Wheel](https://img.shields.io/pypi/wheel/base58check.svg)](https://pypi.python.org/pypi/base58check) [![Pypi Versions](https://img.shields.io/pypi/pyversions/base58check.svg)](https://pypi.python.org/pypi/base58check)


## Maintainer
Joe Black | <me@joeblack.nyc> | [github](https://github.com/joeblackwaslike)


## Introduction
A python implementation of the Base58Check encoding scheme.


The Base58Check encoding scheme is a modified Base 58 binary-to-text encoding.  More generically, Base58Check encoding is used for encoding byte arrays in Bitcoin into human-typable strings.


*PLEASE NOTE*: For consistency with encoding schemes in python, encode inputs must be bytes and will be enforced.  Use `.encode('ascii')` on text input to encode to bytes.

* ref: https://en.bitcoin.it/wiki/Base58Check_encoding


## Installation
```shell
pip3 install base58check
```


## Usage
```python
>>> import base58check
```

### encoding
```python
>>> base58check.b58encode(b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT')
b'\x00v\x80\xad\xec\x8e\xab\xca\xba\xc6v\xbe\x9e\x83\x85J\xde\x0b\xd2,\xdb\x0b\xb9`\xde'
```

### decoding (input can be text or bytes here)
```python
>>> base58check.b58decode('\x00v\x80\xad\xec\x8e\xab\xca\xba\xc6v\xbe\x9e\x83\x85J\xde\x0b\xd2,\xdb\x0b\xb9`\xde')
b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT'
```

## Changes
* [CHANGELOG](CHANGELOG.md)
