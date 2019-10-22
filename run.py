#!/usr/bin/env python3

from queue import Queue
from big_fiubrother_core import SignalHandler
from big_fiubrother_display import FrameConsumer, DisplayThread


if __name__ == "__main__":
    configuration = setup('Big Fiubrother Display Application')

    print('[*] Configuring big-fiubrother-display')

    queue = Queue(maxsize=settings['buffer_size'])
    frame_consumer = FrameConsumer(settings['frame_consumer'], queue)
    display_thread = DisplayThread(settings['fps'], queue)

    signal_handler = SignalHandler(frame_consumer.stop, '[*] Stopping big-fiubrother-display')

    print('[*] Starting big-fiubrother-display')

    display_thread.start()
    frame_consumer.start()
    
    display_thread.stop()
    display_thread.wait()

    print('[*] big-fiubrother-display stopped!')