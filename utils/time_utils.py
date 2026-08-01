#==================================================================================
#
# THIS FILE CONTAINS HELPER FUNCTIONS RELATED TO TIMES
#
#==================================================================================

from datetime import datetime

def timestamp_to_date(timestamp):
    """
    Converts a UNIX timestamp into
    a readable date and time.
    """

    return datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y %H:%M:%S")


def seconds_to_hms(seconds):
    """
    Converts seconds into HH:MM:SS format.
    """

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


def current_time():
    """
    Returns the current system time.
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")