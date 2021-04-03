# Base imports
from datetime import datetime
from typing import Optional

# Third-party imports
import speedtest
import pandas as pd

# Project imports
from common import settings


def log_speed_into_spreadsheet(output_file: str, sheet_name: Optional[str] = 'base') -> None:
    """Function that logs the network speed samples in a spreadsheet."""
    data_frame = pd.read_excel(output_file, sheet_name=sheet_name)

    now = datetime.now()
    sample_date = now.strftime(settings.LOG_DATE_FORMAT)
    sample_time = now.strftime(settings.LOG_TIME_FORMAT)

    tester = speedtest.Speedtest()
    raw_speed = tester.download(threads=None) * settings.DOWNLOAD_SCALE_FACTOR
    sample_speed = round(raw_speed, settings.DOWNLOAD_SPEED_DECIMAL_PLACES)

    print(f'{sample_date} - {sample_time} - Saving network speed value: {sample_speed}')

    data_frame.loc[len(data_frame)] = [
        sample_date,
        sample_time,
        sample_speed,
    ]
    data_frame.to_excel(output_file, sheet_name=sheet_name, index=False)
