import unittest

from receiver import Receiver
from transmitter import Transmitter


class ReceiverSampleTest(unittest.TestCase):
    def test_normal(self):
        key = 'a-secret-key-for-hashing-%^#@'
        transmitter = Transmitter(key, bait_count=10)
        receiver = Receiver(key)
        message = 'hellooooooooo from under water! this is spongebob sending message to patrik! do you copy?'
        transmitter.transmit(message, receiver)
        self.assertEqual(receiver.get_message(), message)

    def test_without_bait(self):
        key = 'secure-key'
        transmitter = Transmitter(key, bait_count=0, chunk_size=7)
        receiver = Receiver(key)
        message = 'this is a message that does not contains bait packets.'
        transmitter.transmit(message, receiver)
        self.assertEqual(receiver.get_message(), message)

    def test_wrong_key(self):
        key = 'wrong-key'
        transmitter = Transmitter(key)
        receiver = Receiver('so' + key)
        message = 'this message is not gonna be received by the receiver because of the wrong key!'
        transmitter.transmit(message, receiver)
        self.assertEqual(receiver.get_message(), '')
