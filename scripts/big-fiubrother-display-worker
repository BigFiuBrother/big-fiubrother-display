 #!/usr/bin/env python3

import yaml
import argparse
from queue import Queue
from big_fiubrother_display import DisplayThread, FrameConsumer
from big_fiubrother_core import SignalHandler


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Big Fiubrother Display Application')
    parser.add_argument('environment', type=str, nargs='?', default='development', help='Environment to run applicacion. By default it is development.')

    args = parser.parse_args()

    print('[*] Configuring big-fiubrother-display')

    with open('config/{}.yml'.format(args.environment.lower())) as config_file:    
        settings = yaml.safe_load(config_file)

    queue = Queue(maxsize=settings['buffer_size'])

    display = Display(settings['fps'], queue)
    display.start()

    frame_consumer = FrameConsumer(settings['frame_consumer'], queue)
    frame_consumer.start()
    
    signal_handler = SignalHandler(processes_to_stop=[display, frame_consumer])

    print('[*] Starting big-fiubrother-display')

    frame_consumer.wait()
    display.wait()

    print('[*] Stopping big-fiubrother-display')




