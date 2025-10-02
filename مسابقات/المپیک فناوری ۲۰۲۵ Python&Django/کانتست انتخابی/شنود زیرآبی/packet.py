class Packet:
    def __init__(self, sequence_number: int, data: str, hashed_data: str):
        self.sequence_number = sequence_number
        self.data = data
        self.hashed_data = hashed_data
        self._flagged = False

    def mark_fake(self):
        self._flagged = True

    def is_fake(self) -> bool:
        return self._flagged

    def __len__(self):
        return len(self.data)
