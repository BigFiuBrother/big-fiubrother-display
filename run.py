#!/usr/bin/env python3

import queue
import signal
import multiprocessing
from big_fiubrother_core import (
    SignalHandler,
    StoppableThread,
    ConsumeFromRabbitMQ,
    setup
)
from big_fiubrother_display import (
    StoreVideoInFileSystem,
    ReadVideoFrames,
    DisplayVideo
)


def consume(configuration, interprocess_queue):
    thread_queue = queue.Queue()

    process = StoppableThread(
        ConsumeFromRabbitMQ(configuration=configuration['consumer'],
                            output_queue=thread_queue))

    thread = StoppableThread(
        StoreVideoInFileSystem(configuration=configuration['persistance'],
                               input_queue=thread_queue,
                               output_queue=interprocess_queue))

    signal_handler = SignalHandler(callback=process.stop)

    thread.start()
    process.run()

    # Signal STOP received!
    thread.stop()
    thread.wait()


def display(configuration, interprocess_queue):
    # 5 seconds max size of queue of frames
    fps = configuration['display']['fps']
    window_size = configuration['display']['window_size']

    thread_queue = queue.Queue(fps * window_size)

    thread = StoppableThread(
        ReadVideoFrames(input_queue=interprocess_queue,
                        output_queue=thread_queue))

    process = StoppableThread(
        DisplayVideo(configuration=configuration['display'],
                     input_queue=thread_queue))

    signal_handler = SignalHandler(callback=process.stop)

    thread.start()
    process.run()

    # Signal STOP received!
    thread.stop()
    thread.wait()


if __name__ == "__main__":
    configuration = setup('Big Fiubrother Display Application')

    print('[*] Configuring big-fiubrother-display')

    interprocess_queue = multiprocessing.Queue()

    consumer_process = multiprocessing.Process(
        target=consume, args=(configuration, interprocess_queue,))
    display_process = multiprocessing.Process(
        target=display, args=(configuration, interprocess_queue,))

    signal.signal(signal.SIGINT, signal.SIG_IGN)

    print('[*] Starting big-fiubrother-display')

    consumer_process.start()
    display_process.start()

    consumer_process.join()
    display_process.join()

    print('[*] big-fiubrother-display stopped!')
