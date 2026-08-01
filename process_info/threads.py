#==================================================================================
#
# THIS FILE CONTAINS ALL THE THREAD RELATED INFORMATION RELATED TO THE PROCESS
#
#==================================================================================

# Importing necessary modules
import psutil
import os

#==================================================================================
# Name          : get_thread_count()
# Description   : Returns the total number of threads used by process
# Input         : Process object
# Output        : Number of threads
#==================================================================================

def get_thread_count(process):
    
    try:
        return process.num_threads()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_threads()
# Description   : Returns detailed information about the threads
# Input         : Process object
# Output        : Detailed information
#==================================================================================

def get_threads(process):
    
    try:
        return process.threads()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : show_thread_info()
# Description   : Display detailed information about threads
# Input         : Process object
# Output        : Detailed information
#==================================================================================

def show_thread_info(process):
    
    WIDTH = 80
    
    print("\n" + "=" * WIDTH)
    print("THREAD INFORMATION".center(WIDTH))
    print("=" * WIDTH)
    
    thread_count = get_thread_count(process)
    
    if thread_count is None:
        print("Unable to retrieve thread information.")
        print("=" * WIDTH)
        return
    
    print(f"Total threads: {thread_count}")
    
    threads = get_threads(process)
    
    if threads:

        print("\n" + "-" * WIDTH)
        print(f"{'No.':<6}{'Thread ID':<20}{'User Time (s)':<20}{'System Time (s)':<20}")
        print("-" * WIDTH)

        for index, thread in enumerate(threads, start=1):
            print(
                f"{index:<6}"
                f"{thread.id:<20}"
                f"{thread.user_time:<20.4f}"
                f"{thread.system_time:<20.4f}"
            )

    else:
        print("\nNo thread details available.")

    print("=" * WIDTH)
    print()