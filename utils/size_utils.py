#==================================================================================
#
# THIS FILE CONTAINS HELPER FUNCTIONS RELATED TO SIZES
#
#==================================================================================

def bytes_to_kb(bytes_value):
    """
    Converts bytes to kilobytes.
    """
    return bytes_value / 1024

def bytes_to_mb(bytes_value):
    """
    Converts bytes to megabytes.
    """
    return bytes_value / (1024 * 1024)

def bytes_to_gb(bytes_value):
    """
    Converts bytes to gigabytes.
    """
    return bytes_value / (1024 * 1024 * 1024)

def bytes_to_tb(bytes_value):
    """
    Converts bytes to terabytes.
    """
    return bytes_value / (1024 * 1024 * 1024 * 1024)

def bytes_to_human_readable(bytes_value):
    """
    Converts bytes into the most suitable unit.
    """

    if bytes_value < 1024:
        return f"{bytes_value} Bytes"

    elif bytes_value < 1024 ** 2:
        return f"{bytes_to_kb(bytes_value):.2f} KB"

    elif bytes_value < 1024 ** 3:
        return f"{bytes_to_mb(bytes_value):.2f} MB"

    elif bytes_value < 1024 ** 4:
        return f"{bytes_to_gb(bytes_value):.2f} GB"

    else:
        return f"{bytes_to_tb(bytes_value):.2f} TB"