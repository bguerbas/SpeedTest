#!/usr/bin/env python3

# Base import
import sys

# Project imports
from common import settings
from logger.jobs import log_speed_into_spreadsheet
from logger.network import NetworkSpeedLogger


if __name__ == '__main__':
    try:
        print('Starting network speed logging service...')

        job_arguments = [
            settings.OUTPUT_FILE_PATH,  # output_file
        ]

        speed_logger = NetworkSpeedLogger(log_speed_into_spreadsheet)
        speed_logger.start(job_arguments)

    except (KeyboardInterrupt, SystemExit):
        print('Received keyboard interrupt, quitting threads...')
        speed_logger.cancel()
        sys.exit(0)
    except Exception as exception:
        print(f'{exception.__class__.__name__}: {str(exception)}')
        speed_logger.cancel()
        sys.exit(-1)
