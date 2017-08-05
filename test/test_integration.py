import collections
import socket
import unittest

from iofus.binaryio import ByteArray
from iofus.denums import Metadata
from iofus.dmessages import (IdentificationMessage, HelloConnectMessage,
                             ProtocolRequired, BasicPingMessage)
from iofus.network import MessageBuilder


class ReachServerTests(unittest.TestCase):

    def setUp(self):
        self.socket_ = socket.socket()
        self.socket_.connect(("213.248.126.39", 5555))

    def tearDown(self):
        self.socket_.close()

    def test_protocol_version_check(self):
        """ receive and parse the first message to check protocol version """
        data = self.socket_.recv(2048)

        # The server is responding to connection
        self.assertNotEqual(len(data), 0)

        # We receive the first messages
        message_builder = MessageBuilder()
        message_queue = collections.deque()
        messages = message_builder.receive(data)
        for message in messages:
            message_queue.append(message)
        self.assertGreaterEqual(len(message_queue), 1)

        # Check if the protocol is up to date
        message = message_queue.popleft()
        self.assertIsInstance(message, ProtocolRequired)
        self.assertGreaterEqual(message.requiredVersion, Metadata.PROTOCOL_BUILD)

        # Receive HelloConnectMessage
        if len(message_queue) < 1:
            data = self.socket_.recv(2048)
            messages = message_builder.receive(data)
            for message in messages:
                message_queue.append(message)
        message = message_queue.popleft()
        self.assertIsInstance(message, HelloConnectMessage)
