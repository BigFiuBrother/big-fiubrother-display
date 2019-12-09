from queue import PriorityQueue


class FrameBuffer:

    def __init__(self, size):
        self.size = size
        self._queue = PriorityQueue(self.size)

    def qsize(self):
        return self._queue.qsize()

    def put(self, message):
        if self._queue.full():
            self._queue.get()

        self._queue.put(message, block=False)

    def get(self):
        return self._queue.get()
