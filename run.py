#!/usr/bin/env python3

import yaml
import argparse
from queue import Queue
from big_fiubrother_core import SignalHandler
from big_fiubrother_display import FrameConsumer, DisplayThread


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Big Fiubrother Display Application')
    parser.add_argument('environment', type=str, nargs='?', default='development', help='Environment to run applicacion. By default it is development.')

    args = parser.parse_args()

    print('[*] Configuring big-fiubrother-display')

    with open('config/{}.yml'.format(args.environment.lower())) as config_file:    
        settings = yaml.safe_load(config_file)

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