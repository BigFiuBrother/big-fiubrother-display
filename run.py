#!/usr/bin/env python3

import queue
import signal
import multiprocessing
from big_fiubrother_core import SignalHandler, setup
from big_fiubrother_display import VideoChunkConsumer, LocalPersistanceThread, VideoReaderThread, DisplayThread


def consume(configuration, interprocess_queue):
    video_chunk_consumer_to_local_persistance_thread_queue = queue.Queue()

    video_chunk_consumer = VideoChunkConsumer(configuration['consumer'], video_chunk_consumer_to_local_persistance_thread_queue)
    local_persistance_thread = LocalPersistanceThread(configuration['persistance'], video_chunk_consumer_to_local_persistance_thread_queue, interprocess_queue)
    
    signal_handler = SignalHandler(callback=video_chunk_consumer.stop)

    local_persistance_thread.start()
    video_chunk_consumer.run()
    
    # Signal STOP received!

    local_persistance_thread.stop()
    local_persistance_thread.wait()


def display(configuration, interprocess_queue):
    # 5 seconds max size of queue of frames
    video_reader_thread_to_display_thread_queue = queue.Queue(configuration['display']['fps'] * configuration['display']['window_size'])

    video_reader_thread = VideoReaderThread(interprocess_queue, video_reader_thread_to_display_thread_queue)
    display_thread = DisplayThread(configuration['display'], video_reader_thread_to_display_thread_queue)

    signal_handler = SignalHandler(callback=display_thread.stop)

    video_reader_thread.start()
    display_thread.run()

    # Signal STOP received!

    video_reader_thread.stop()
    video_reader_thread.wait()

if __name__ == "__main__":
    configuration = setup('Big Fiubrother Display Application')

    print('[*] Configuring big-fiubrother-display')

    interprocess_queue = multiprocessing.Queue()

    consumer_process = multiprocessing.Process(target=consume, args=(configuration, interprocess_queue,))
    display_process = multiprocessing.Process(target=display, args=(configuration, interprocess_queue,))

    print('[*] Starting big-fiubrother-display')

    consumer_process.start()
    display_process.start()

    signal.signal(signal.SIGINT, signal.SIG_IGN)

    consumer_process.join()
    display_process.join()

    print('[*] big-fiubrother-display stopped!')