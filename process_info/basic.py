#==================================================================================
#
# THIS MODULE CONTAINS ALL THE BASIC INFORMATION RELATED TO PROCESS
#
#==================================================================================

# Importing necessary modules
import psutil
import os
from datetime import datetime

#==================================================================================
# Name          : get_process_id()
# Description   : Returns the PID of running process
# Input         : Process object
# Output        : PID
#==================================================================================

def get_process_id(process):

    return process.pid

#==================================================================================
# Name          : get_parent_process_id()
# Description   : Returns the PPID of running process
# Input         : Process object
# Output        : PPID
#==================================================================================

def get_parent_process_id(process):

    return process.ppid()
    
#==================================================================================
# Name          : get_process_name()
# Description   : Returns the name of running process
# Input         : Process object
# Output        : Name
#==================================================================================

def get_process_name(process):
    
    return process.name()

#==================================================================================
# Name          : get_process_status()
# Description   : Returns the status of running process
# Input         : Process object
# Output        : Status (process state)
#==================================================================================

def get_process_status(process):
    
    return process.status()

#==================================================================================
# Name          : get_username()
# Description   : Returns name of user that owns the process
# Input         : Process object
# Output        : Username
#==================================================================================

def get_username(process):
    
    return process.username()

#==================================================================================
# Name          : get_executable_path()
# Description   : Returns the absolute path of process executable
# Input         : Process object
# Output        : EXE path
#==================================================================================

def get_executable_path(process):

    try:
        return process.exe()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_working_directory()
# Description   : Returns the current working directory 
# Input         : Process object
# Output        : current working directory path
#==================================================================================

def get_working_directory(process):
    
    try:
        return process.cwd()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_command_line()
# Description   : Returns the command line arguments passed to process
# Input         : Process object
# Output        : Command line arguments passed to process
#==================================================================================

def get_command_line(process):
    
    try:
        command = process.cmdline()
        
        # .cmdline -> returns list of strings
        # join to make it look like the terminal command
        if command:
            return " ".join(command)
        
        return "N/A"
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_creation_time()
# Description   : Returns the process creation time
# Input         : Process object
# Output        : Process creation time
#==================================================================================

def get_creation_time(process):
    
    try:
        proc_time = process.create_time()
        
        # It returns process time in raw seconds 
        # We can use time module to make it readble
        # return time.ctime(proc_time)
        return datetime.fromtimestamp(proc_time).strftime("%d-%m-%Y %H:%M:%S")
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
# ==============================================================================
# Name          : get_priority()
# Description   : Returns the process priority formatted with readable labels
# Input         : Process object
# Output        : Process priority string
# ==============================================================================

def get_priority(process):
    
    try:
        nice_val = process.nice()
        
        # Windows Priority Classes mapping
        if os.name == "nt":
            windows_priorities = {
                64: "Idle",
                16384: "Below Normal",
                32: "Normal",
                32768: "Above Normal",
                128: "High",
                256: "Realtime"
            }
            
            label = windows_priorities.get(nice_val, "Unknown")
            return f"{label} ({nice_val})"
          
        # Linux / macOS Unix Nice values (-20 to 19)  
        elif os.name == "posix":
            if nice_val < 0:
                label = "High / Prioritized"
            elif nice_val > 0:
                label = "Low / Niced"
            else:
                label = "Normal"
            return f"{label} ({nice_val})"
            
        else:
            return str(nice_val)

    except psutil.AccessDenied:
        return "Access Denied"
    
    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : is_process_running()
# Description   : Checks whether process is running or not
# Input         : Process object
# Output        : True or false
#==================================================================================

def is_process_running(process):
    
    try:
        return process.is_running()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
    
#==================================================================================
# Name          : show_basic_info()
# Description   : Display the basic information of target process
# Input         : Process object
# Output        : None
#==================================================================================

def show_basic_info(process):
    
    WIDTH = 80
    
    print("\n" + "=" * WIDTH)
    print("BASIC PROCESS INFORMATION".center(WIDTH))
    print("=" * WIDTH)

    print()
    print(f"{'Process ID':25}: {get_process_id(process)}")
    print(f"{'Parent Process ID':25}: {get_parent_process_id(process)}")
    print(f"{'Process Name':25}: {get_process_name(process)}")
    print(f"{'Status':25}: {get_process_status(process)}")
    print(f"{'Username':25}: {get_username(process)}")
    print(f"{'Executable Path':25}: {get_executable_path(process)}")
    print(f"{'Working Directory':25}: {get_working_directory(process)}")
    print(f"{'Command Line':25}: {get_command_line(process)}")
    print(f"{'Creation Time':25}: {get_creation_time(process)}")
    print(f"{'Priority (Nice)':25}: {get_priority(process)}")
    print(f"{'Is Running':25}: {is_process_running(process)}")
    print()

    print("=" * WIDTH)
    print()