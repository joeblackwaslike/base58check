import unittest

import base58check


TEST_DATA = [
    (b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT',
     b'\x00v\x80\xad\xec\x8e\xab\xca\xba\xc6v\xbe\x9e\x83\x85J\xde\x0b\xd2,\xdb\x0b\xb9`\xde'),
    (b'3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC',
     b'\x05\xf8\x15\xb06\xd9\xbb\xbc\xe5\xe9\xf2\xa0\n\xbd\x1b\xf3\xdc\x91\xe9U\x10\xcd\x001\x07'),
    (b'mkwV3DZkgYwKaXkphBtcXAjsYQEqZ8aB3x',
     b'o;|F\xa5\xa6\x00\xb2\x98k\xd8\x04\x13|\xf9\x1d\xbbZE\xa2|\xa8\x00l+'),
    (b'n1tpDjEJw32qGwkdQKPfACpcTtCa6hDVBw',
     b'o\xdf\x84\xed0\x95\xc6_\xddu\xf4j\xd8|3\xe0\xb1\xf4\x14\xff\xe6\xf8\t\x8f\xaa'),
    (b'LeF6vC9k1qfFDEj6UGjM5e4fwHtiKsakTd',
     b'0\xd0\xa2\x07\xd1\x82\xa7\xe0]\x7fD\xb6\\5\xf9\xe1\xd1v\xeb\xde\xa7\xba\x08\x90\\'),
    (b'muE4dcYXagWA7WT8ZnCriiy65FELikhdUy',
     b'o\x96_\xfa\xccH\xe6\x87\xe0\xd3NJ\x8a\x86\x83*\x8dl\xfc\xf0{\xf1#\xb76')
]

CUSTOM_CHARSET = b'rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz'
CUSTOM_CHARSET_DATA = [
    (b'rDTXLQ7ZKZVKz33zJbHjgVShjsBnqMBhmN',
     b'\x00\x88\xa5\xa5|\x82\x9f@\xf2^\xa83\x85\xbb\xdel=\x8bL\xa0\x82\xedC\x86A')
]


class Base58Tests(unittest.TestCase):
    def test_base(self):
        """Assert that BASE is equal to 58"""
        self.assertEqual(58, len(base58check.DEFAULT_CHARSET))

    def test_encoding_text_raises_typeerror(self):
        """Assert encoding text (nonbinary) raises TypeError"""
        with self.assertRaises(TypeError):
            base58check.b58encode('test text')

    def test_encoding(self):
        """Assert correct encoding and return type"""
        for encoded, raw in TEST_DATA:
            result = base58check.b58encode(raw)
            self.assertEqual(result, encoded)
            self.assertIsInstance(result, bytes)

    def test_decoding(self):
        """Assert correct decoding and return type from bytes"""
        for encoded, raw in TEST_DATA:
            result = base58check.b58decode(encoded)
            self.assertEqual(result, raw)
            self.assertIsInstance(result, bytes)

    def test_decoding_from_unicode(self):
        """Assert correct decoding and return type from text"""
        for encoded, raw in TEST_DATA:
            result = base58check.b58decode(encoded.decode())
            self.assertEqual(result, raw)
            self.assertIsInstance(result, bytes)

    def test_custom_charset_encoding(self):
        """Assert correct encoding and return type for custom character set"""
        for encoded, raw in CUSTOM_CHARSET_DATA:
            result = base58check.b58encode(raw, charset=CUSTOM_CHARSET)
            self.assertEqual(result, encoded)
            self.assertIsInstance(result, bytes)

    def test_custom_charset_decoding(self):
        """Assert correct decoding and return type for custom character set"""
        for encoded, raw in CUSTOM_CHARSET_DATA:
            result = base58check.b58decode(encoded, charset=CUSTOM_CHARSET)
            self.assertEqual(result, raw)
            self.assertIsInstance(result, bytes)


if __name__ == '__main__':
    unittest.main()
