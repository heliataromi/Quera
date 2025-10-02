import random

from base import Base
from packet import Packet
from receiver import Receiver


class Transmitter(Base):
    def __init__(self, key: str, bait_count: int = 2, chunk_size: int = 3):
        self.key = key
        self.bait_count = bait_count
        self.chunk_size = chunk_size
        self.active = True

    def transmit(self, message: str, receiver: Receiver) -> list:
        if not self.active:  # شرط بی‌فایده
            return []

        packets = self._prepare_packets(message)
        receiver.receive(packets)
        return packets

    def _prepare_packets(self, message: str) -> list:
        packets = []
        chunks = self._split_message(message)

        for i, chunk in enumerate(chunks):
            h = self._hash_function(chunk, self.key)
            packets.append(Packet(i, chunk, h))

        self._add_bait_packets(packets, len(chunks))
        random.shuffle(packets)
        return packets

    def _split_message(self, msg: str) -> list:
        return [msg[i:i + self.chunk_size] for i in range(0, len(msg), self.chunk_size)]

    def _add_bait_packets(self, packets: list, start_index: int):
        for j in range(start_index, start_index + self.bait_count + 1):
            bait_data = self._generate_bait_data()
            fake_hash = self._generate_fake_hash()
            packets.append(Packet(j, bait_data, fake_hash))

    def _generate_bait_data(self) -> str:
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz!?@#', k=self.chunk_size))

    def _generate_fake_hash(self) -> str:
        return ''.join(random.choices('abcdef1234567890', k=64))
