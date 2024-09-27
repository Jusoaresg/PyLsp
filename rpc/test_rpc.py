import rpc
import unittest

class EncodingTestingMessage:
    def __init__(self, test):
        self.test = test


class encoding_testing(unittest.TestCase):

    def test_message_encode(self):

        expected = 'Content-Length 15\r\n\r\n{"test": false}'
        result = rpc.encode_message(EncodingTestingMessage(False).__dict__)
        self.assertEqual(expected, result, "Testing")

    def test_message_decoding(self):
        msg = 'Content-Length 15\r\n\r\n{"method": "hi"}'
        msg_incoded = msg.encode("utf-8")
        content = rpc.decode_message(msg_incoded)

        self.assertEqual(content, ('hi', 15))

if __name__ == '__main__':
    unittest.main()
