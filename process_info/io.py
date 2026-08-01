#==================================================================================
#
# THIS MODULE CONTAINS ALL THE I/O INFORMATION RELATED TO THE PROCESS
#
#==================================================================================

import psutil

from utils.size_utils import bytes_to_human_readable

#==================================================================================
# Name          : get_io_counters()
# Description   : Returns the i/o counters of the process
# Input         : Process object
# Output        : I/O counters
#==================================================================================

def get_io_counters(process):
    
    try:
        return process.io_counters()
    
    except AttributeError:
        return "Invalid Attribute"
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : show_io_info()
# Description   : Display I/O statistics of the process
# Input         : Process object
# Output        : I/O counters
#==================================================================================
    
def show_io_info(process):
    
    WIDTH = 80
    
    print("\n" + "=" * WIDTH)
    print("I/O INFORMATION".center(WIDTH))
    print("=" * WIDTH)
    
    io = get_io_counters(process)

    if io is None:
        print("Unable to retrieve I/O information.")
        print("=" * WIDTH)
        return

    print(f"{'Read Operations':25}: {io.read_count}")
    print(f"{'Write Operations':25}: {io.write_count}")

    print(
        f"{'Bytes Read':25}: "
        f"{bytes_to_human_readable(io.read_bytes)}"
    )

    print(
        f"{'Bytes Written':25}: "
        f"{bytes_to_human_readable(io.write_bytes)}"
    )

    print(
        f"{'Characters Read':25}: "
        f"{getattr(io, 'read_chars', 'Not Supported')}"
    )

    print(
        f"{'Characters Written':25}: "
        f"{getattr(io, 'write_chars', 'Not Supported')}"
    )

    print("=" * WIDTH)