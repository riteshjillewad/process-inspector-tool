#==================================================================================
#
# THIS MODULE CONTAINS ALL THE CPU INFORMATION RELATED TO THE PROCESS
#
#==================================================================================

# Importing necessary modules
import psutil
import os

#==================================================================================
# Name          : get_cpu_usage()
# Description   : Returns the CPU percentage of process
# Input         : Process object
# Output        : CPU percentage
#==================================================================================

def get_cpu_usage(process):
    
    try:
        # first call will initialize the measurement
        process.cpu_percent(interval = None)
        
        # Now measure the after 0.1 second
        return process.cpu_percent(interval = 0.1)
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_cpu_times()
# Description   : Returns how CPU time process has consumed
# Input         : Process object
# Output        : CPU percentage
#==================================================================================

def get_cpu_times(process):
    
    try:
        # returns tuples (user, system)
        # user   -> how much time in user mode
        # system -> how much time in kernel mode
        return process.cpu_times()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_cpu_affinity()
# Description   : Returns the list of CPU cores assigned to the process
# Input         : Process object
# Output        : List of CPU cores
#==================================================================================

def get_cpu_affinity(process):
    
    try:
        return process.cpu_affinity()
    
    except AttributeError:
        return "Not Supported"
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_cpu_number()
# Description   : Returns the CPU core currenlty exeuting the process
# Input         : Process object
# Output        : Running CPU core
#==================================================================================

def get_cpu_number(process):
    
    # Windows does not support individual process cpu_num
    if os.name == "nt":
        return "N/A"
        
    try:
        return process.cpu_num()
    
    except AttributeError:
        return "Not Supported"
    
    except NotImplementedError:
        return "Not Supported"
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_context_switches()
# Description   : Returns the number of context switches of the process
# Input         : Process object
# Output        : Number of context switches
#==================================================================================

def get_context_switches(process):
    
    try:
        return process.num_ctx_switches()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"

#==================================================================================
# Name          : show_cpu_info()
# Description   : Displays the CPU related information
# Input         : Process object
# Output        : Process CPU related information
#==================================================================================

def show_cpu_info(process):
    
    WIDTH = 80
    
    print("\n" + "=" * WIDTH)
    print("CPU INFORMATION".center(WIDTH))
    print("=" * WIDTH)
    
    print(f"{'CPU Usage (%)':25}: {get_cpu_usage(process)}")
    
    cpu_times = get_cpu_times(process)

    if cpu_times:
        print(f"{'User Time':25}: {cpu_times.user}")
        print(f"{'System Time':25}: {cpu_times.system}")

    else:
        print(f"{'User Time':25}: Access Denied")
        print(f"{'System Time':25}: Access Denied")
        
    print(f"{'CPU Affinity':25}: {get_cpu_affinity(process)}")
    print(f"{'CPU Number':25}: {get_cpu_number(process)}")

    context = get_context_switches(process)

    if context:
        print(f"{'Voluntary Switches':25}: {context.voluntary}")
        print(f"{'Involuntary Switches':25}: {context.involuntary}")
        print(f"{'Total Switches':25}: {context.voluntary + context.involuntary}")

    else:
        print(f"{'Voluntary Switches':25}: Access Denied")
        print(f"{'Involuntary Switches':25}: Access Denied")

    print("=" * WIDTH)
    print()