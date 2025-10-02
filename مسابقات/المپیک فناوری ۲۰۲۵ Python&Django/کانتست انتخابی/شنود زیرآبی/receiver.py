from base import Base
from packet import Packet


class Receiver(Base):
    def __init__(self, key: str):
        self.key = key
        self._real_packets = []
        self._buffer = []

    def receive(self, packets: list[Packet]) -> None:
        for packet in packets:
            if packet.hashed_data == self._hash_function(packet.data, self.key):
                self._real_packets.append(packet)

    def get_message(self) -> str:
        message = ""

        self._real_packets.sort(key=lambda x: x.sequence_number)

        for packet in self._real_packets:
            message += packet.data

        return message

    def _filter_valid_packets(self, packets: list[Packet]) -> list[Packet]:
        result = []
        for pkt in packets:
            if self._is_valid(pkt):
                result.append(pkt)
            else:
                self._log_rejected(pkt)
        return result

    def _sort_packets(self, packets: list[Packet]) -> list[Packet]:
        return sorted(packets, key=lambda p: p.sequence_number)

    def _is_valid(self, packet: Packet) -> bool:
        expected_hash = self._hash_function(packet.data, self.key)
        return packet.hashed_data == expected_hash

    def _log_rejected(self, packet: Packet) -> None:
        if len(packet.data) < 1:
            print(f"Packet #{packet.sequence_number} is empty.")
        elif packet.sequence_number < 0:
            print(f"Invalid packet sequence: {packet.sequence_number}")
