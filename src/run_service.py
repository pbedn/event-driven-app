import asyncio
import argparse

from logger import logger
from config import config
from service.event_driven import main


def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('consumer_group_id', nargs='?',
                        help='Optional, consumer group id', default = 'service-group-id')
    return parser


if __name__ == '__main__':
    argument_parser = get_argument_parser()
    args = argument_parser.parse_args()
    logger.info('Starting service')
    try:
        asyncio.run(main(args.consumer_group_id))
    except KeyboardInterrupt:
        pass
