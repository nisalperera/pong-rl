class LastLocationsList(list):
    def __init__(self, seq=[], length=5):
        self.length = length

        if len(seq) > length:
            seq = seq[-length:]

        super(LastLocationsList, self).__init__(seq)

    def append(self, item):
        if len(self) > self.length:
            del self[0]
        super(LastLocationsList, self).append(item)
        