from queue import Queue
import yaml
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Big Fiubrother Display Application')
    parser.add_argument('environment', type=str, nargs='?', default='development', help='Environment to run applicacion. By default it is development.')

    args = parser.parse_args()

    print('[*] Configuring big-fiubrother-display')

    with open('config/{}.yml'.format(args.environment.lower())) as config_file:    
        settings = yaml.safe_load(config_file)

    queue = Queue(maxsize=settings['buffer_size']*settings['fps'])    