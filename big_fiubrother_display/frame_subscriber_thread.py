from time import sleep
from threading import Thread

class ProcessedFrameConsumerThread:

    def __init__(self, consumer_settings, output_queue):
        self.consumer = QueueConsumer(consumer_settings['host'], consumer_settings['queue'], self.consumer_callback)
        self.output_queue = output_queue

        self.running = False

    def start(self):
        self.running = True
        self.consumer.start()

    def consumer_callback(self, body):
        # TODO: Convert to Message Object before pushing
        output_queue.push(body)

    def stop(self, wait=False):
        self.consumer.stop(wait=wait)
        self.running = False

    def wait_until_stopped(self): 
        self.consumer.wait_until_stopped()
