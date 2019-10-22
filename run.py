#!/usr/bin/env python3

from queue import Queue
from big_fiubrother_core import SignalHandler, setup
from big_fiubrother_display import VideoChunkConsumer, LocalPersistanceThread, VideoReaderThread, DisplayThread


if __name__ == "__main__":
    configuration = setup('Big Fiubrother Display Application')

    print('[*] Configuring big-fiubrother-display')

    video_chunk_consumer_to_local_persistance_thread_queue = Queue()
    local_persistance_thread_to_video_reader_thread_queue = Queue()
    # 5 seconds max size of queue of frames
    video_reader_thread_to_display_thread_queue = Queue(configuration['display']['fps'] * configuration['display']['window_size'])

    video_chunk_consumer = VideoChunkConsumer(configuration['consumer'], video_chunk_consumer_to_local_persistance_thread_queue)
    local_persistance_thread = LocalPersistanceThread(configuration['persistance'], video_chunk_consumer_to_local_persistance_thread_queue, local_persistance_thread_to_video_reader_thread_queue)
    video_reader_thread = VideoReaderThread(local_persistance_thread_to_video_reader_thread_queue, video_reader_thread_to_display_thread_queue)
    display_thread = DisplayThread(configuration['display'], video_reader_thread_to_display_thread_queue)

    signal_handler = SignalHandler(callback=video_chunk_consumer.stop)

    print('[*] Starting big-fiubrother-display')

    display_thread.start()
    video_reader_thread.start()
    local_persistance_thread.start()
    video_chunk_consumer.start()

    # Signal STOP received!
    
    local_persistance_thread.stop()
    video_reader_thread.stop()
    display_thread.stop()

    local_persistance_thread.wait()
    video_reader_thread.wait()
    display_thread.wait()

    print('[*] big-fiubrother-display stopped!')