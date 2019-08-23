from big_fiubrother_core.messages import FrameMessage


class FrameConsumer:

    def __init__(self, consumer_settings, output_queue):
        self.consumer = QueueConsumer(consumer_settings['host'], consumer_settings['queue'], self.consumer_callback)
        self.output_queue = output_queue

    def start(self):
        self.consumer.start()

    def consumer_callback(self, body):
        output_queue.put(FrameMessage.decode(body))

    def stop(self):
        self.consumer.stop()

    def wait(self): 
        self.consumer.wait()
