"""
:mod:`base58check`
~~~~~~~~~~~

A python implementation of the Base58Check encoding scheme.

The Base58Check encoding scheme is a modified Base 58 binary-to-text encoding.
More generically, Base58Check encoding is used for encoding byte arrays in
Bitcoin into human-typable strings.

ref: `<https://en.bitcoin.it/wiki/Base58Check_encoding>`_

.. note::
    For consistency with encoding schemes in python, encode inputs must be
    bytes and will be enforced.  Use `.encode('ascii')` on text input to
    encode to bytes.

Usage::

    >>> import base58check
    >>> base58check.b58encode(b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT')
    b'\x00v\x80\xad\xec\x8e\xab\xca\xba\xc6v\xbe\x9e\x83\x85J\xde\x0b\xd2,\xdb\x0b\xb9`\xde'

    >>> base58check.b58decode('\x00v\x80\xad\xec\x8e\xab\xca\xba\xc6v\xbe\x9e'
    ...                       '\x83\x85J\xde\x0b\xd2,\xdb\x0b\xb9`\xde')
    b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT'

:copyright: (c) 2018 by Joseph Black.
:license: MIT, see LICENSE for more details.
"""

__version__ = '1.0.2'


from hashlib import sha256
from collections import deque


DEFAULT_CHARSET = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
# BASE = len(CHARSET)


def b58encode(val, charset=DEFAULT_CHARSET):
    """Encode input to base58check encoding.

    :param bytes val: The value to base58check encode.
    :param bytes charset: (optional) The character set to use for encoding.
    :return: the encoded bytestring.
    :rtype: bytes
    :raises: TypeError: if `val` is not bytes.

    Usage::

      >>> import base58check
      >>> base58check.b58encode(b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT')
      b'\x00v\x80\xad\xec\x8e\xab\xca\xba\xc6v\xbe\x9e\x83\x85J\xde\x0b\xd2,\xdb\x0b\xb9`\xde'
    """

    def _b58encode_int(int_, default=bytes([charset[0]])):
        if not int_ and default:
            return default
        output = b''
        while int_:
            int_, idx = divmod(int_, base)
            output = charset[idx:idx+1] + output
        return output

    if not isinstance(val, bytes):
        raise TypeError(
            "a bytes-like object is required, not '%s', "
            "use .encode('ascii') to encode unicode strings" %
            type(val).__name__)

    if isinstance(charset, str):
        charset = charset.encode('ascii')

    base = len(charset)

    if not base == 58:
        raise ValueError('charset base must be 58, not %s' % base)

    pad_len = len(val)
    val = val.lstrip(b'\0')
    pad_len -= len(val)

    p, acc = 1, 0
    for char in deque(reversed(val)):
        acc += p * char
        p = p << 8

    result = _b58encode_int(acc, default=False)
    prefix = bytes([charset[0]]) * pad_len
    return prefix + result


def b58decode(val, charset=DEFAULT_CHARSET):
    """Decode base58check encoded input to original raw bytes.

    :param bytes val: The value to base58cheeck decode.
    :param bytes charset: (optional) The character set to use for decoding.
    :return: the decoded bytes.
    :rtype: bytes

    Usage::

      >>> import base58check
      >>> base58check.b58decode('\x00v\x80\xad\xec\x8e\xab\xca\xba\xc6v\xbe'
      ...                       '\x9e\x83\x85J\xde\x0b\xd2,\xdb\x0b\xb9`\xde')
      b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT'
    """

    def _b58decode_int(val):
        output = 0
        for char in val:
            output = output * base + charset.index(char)
        return output

    if isinstance(val, str):
        val = val.encode()

    if isinstance(charset, str):
        charset = charset.encode()

    base = len(charset)

    if not base == 58:
        raise ValueError('charset base must be 58, not %s' % base)

    pad_len = len(val)
    val = val.lstrip(bytes([charset[0]]))
    pad_len -= len(val)

    acc = _b58decode_int(val)

    result = deque()
    while acc > 0:
        acc, mod = divmod(acc, 256)
        result.appendleft(mod)

    prefix = b'\0' * pad_len
    return prefix + bytes(result)
