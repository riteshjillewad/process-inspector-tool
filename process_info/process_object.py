#==================================================================================
# Name          : process_object
# Description   : Responsibilites:
#                 1. Create a process object using current PID
#                 2. Validiitng the process object information
#                 3. Return the process object to main
# Input         : pid
# Output        : process object
#==================================================================================

import psutil
import sys

def create_process(pid):
    
    try:
        process = psutil.Process(pid)
        return process

    except psutil.NoSuchProcess:
        print(f"Error: No process found with PID {pid}.")
        sys.exit(1)

    except psutil.AccessDenied:
        print(f"Error: Access denied to process with PID {pid}.")
        sys.exit(1)

    except psutil.ZombieProcess:
        print(f"Error: Process with PID {pid} is a zombie process.")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected Error: {e}")
        sys.exit(1)
    
    """
        Instead of using psutil.Process(pid) eveywhere, we create object and use that object everywhere
    """