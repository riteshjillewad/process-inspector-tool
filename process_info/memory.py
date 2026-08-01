#==================================================================================
#
# THIS MODULE CONTAINS ALL THE MEMORY INFORMATION RELATED TO THE PROCESS
#
#==================================================================================

# Importing necessary modules
import psutil
import os

from utils.size_utils import bytes_to_human_readable

#==================================================================================
# Name          : get_memory_info()
# Description   : Returns the basic memory information
# Input         : Process object
# Output        : Memory info
#==================================================================================

def get_memory_info(process):
    
    try:
        return process.memory_info()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_memory_full_info()
# Description   : Returns the detailed memory information
# Input         : Process object
# Output        : Memory info
#==================================================================================

def get_memory_full_info(process):
    
    try:
        return process.memory_full_info()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_memory_percent()
# Description   : Returns the memory usage percentage
# Input         : Process object
# Output        : Memory usage percentage
#==================================================================================

def get_memory_percent(process):
    
    try:
        return process.memory_percent()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : show_memory_info()
# Description   : Display memory information of process
# Input         : Process object
# Output        : Memory usage percentage
#==================================================================================

def show_memory_info(process):
    
    WIDTH = 80
    
    print("\n" + "=" * WIDTH)
    print("MEMORY INFORMATION".center(WIDTH))
    print("=" * WIDTH)

    memory = get_memory_info(process)

    if memory:

        print(f"{'Physical Memory':25}: {bytes_to_human_readable(memory.rss)}")
        print(f"{'Virtual Memory':25}: {bytes_to_human_readable(memory.vms)}")

        print(
            f"{'Shared Memory':25}: "
            f"{bytes_to_human_readable(memory.shared) if hasattr(memory, 'shared') else 'Not Supported'}"
        )

        print(
            f"{'Text Memory':25}: "
            f"{bytes_to_human_readable(memory.text) if hasattr(memory, 'text') else 'Not Supported'}"
        )

        print(
            f"{'Data Memory':25}: "
            f"{bytes_to_human_readable(memory.data) if hasattr(memory, 'data') else 'Not Supported'}"
        )

    else:

        print(f"{'Physical Memory':25}: Access Denied")
        print(f"{'Virtual Memory':25}: Access Denied")
        print(f"{'Shared Memory':25}: Access Denied")
        print(f"{'Text Memory':25}: Access Denied")
        print(f"{'Data Memory':25}: Access Denied")

    print(f"{'Memory Usage (%)':25}: {get_memory_percent(process):.2f} %")

    full_memory = get_memory_full_info(process)

    if full_memory:

        print(
            f"{'Unique Private Memory':25}: "
            f"{bytes_to_human_readable(full_memory.uss) if hasattr(full_memory, 'uss') else 'Not Supported'}"
        )

        print(
            f"{'Proportional Set Memory':25}: "
            f"{bytes_to_human_readable(full_memory.pss) if hasattr(full_memory, 'pss') else 'Not Supported'}"
        )

        print(
            f"{'Swap Memory':25}: "
            f"{bytes_to_human_readable(full_memory.swap) if hasattr(full_memory, 'swap') else 'Not Supported'}"
        )

    else:

        print(f"{'Unique Private Memory':25}: Access Denied")
        print(f"{'Proportional Set Memory':25}: Access Denied")
        print(f"{'Swap Memory':25}: Access Denied")

    print("=" * WIDTH)
    print()