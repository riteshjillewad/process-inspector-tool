#==================================================================================
#
# THIS MODULE CONTAINS ALL THE FILE INFORMATION RELATED TO THE PROCESS
#
#==================================================================================

# Importing necessary modules
import psutil
import os

#==================================================================================
# Name          : get_executable_path()
# Description   : Returns full path of executable
# Input         : Process object
# Output        : Executable path
#==================================================================================

def get_executable_path(process):
    
    try:
        return process.exe()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_current_working_directory()
# Description   : Returns current working directory
# Input         : Process object
# Output        : Current working directory
#==================================================================================

def get_current_working_directory(process):
    
    try:
        return process.cwd()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_open_files()
# Description   : Returns the list of files currently opened by the process
# Input         : Process object
# Output        : List of files opened by the process
#==================================================================================

def get_open_files(process):
    
    try:
        return process.open_files()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_memory_maps()
# Description   : Returns memory mapped files by the process
# Input         : Process object
# Output        : Memory mapped files by the process
#==================================================================================

def get_memory_maps(process):
    
    try:
        return process.memory_maps()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : show_file_info()
# Description   : Display file related information
# Input         : Process object
# Output        : File related information
#==================================================================================

def show_file_info(process):
    
    WIDTH = 80
    
    print("\n" + "=" * WIDTH)
    print("FILE RELATED INFORMATION".center(WIDTH))
    print("=" * WIDTH)
    
    executable = get_executable_path(process)
    
    if executable:
        print(f"\nExecutable Path :\n{executable}")
    else:
        print("\nExecutable Path : Access Denied")
        
    cwd = get_current_working_directory(process)
    
    if cwd:
        print(f"\nWorking Directory :\n{cwd}")
    else:
        print("\nWorking Directory : Access Denied")
        
    print("\n" + "-" * WIDTH)
    print("OPEN FILES")
    print("-" * WIDTH)
    
    open_files = get_open_files(process)
    
    if open_files:
        for index, file in enumerate(open_files, start=1):

            print(f"\nFile {index}")
            print(f"Path     : {file.path}")
            print(f"FD       : {file.fd}")
            print(f"Position : {getattr(file, 'position', 'Not Supported on Windows')}")
            print(f"Mode     : {getattr(file, 'mode', 'Not Supported on Windows')}")
            print(f"Flags    : {getattr(file, 'flags', 'Not Supported on Windows')}")

    elif open_files == []:
        print("No open files found.")

    else:
        print("Unable to retrieve open file information.")
        
    print("\n" + "-" * WIDTH)
    print("MEMORY MAPPED FILES")
    print("-" * WIDTH)

    memory_maps = get_memory_maps(process)

    if isinstance(memory_maps, list):

        if not memory_maps:
            print("No memory mapped files found!")

        # Windows
        elif os.name == "nt":

            print(f"{'No.':<5}{'RSS (KB)':<12}{'Path'}")
            print("-" * WIDTH)

            for index, mmap in enumerate(memory_maps, start=1):
                rss = getattr(mmap, "rss", 0) // 1024
                path = mmap.path if mmap.path else "[Anonymous]"

                print(
                    f"{index:<5}"
                    f"{rss:<12}"
                    f"{path}"
                )

        # Linux
        else:

            print(
                f"{'No.':<5}"
                f"{'RSS(KB)':<10}"
                f"{'Size(KB)':<10}"
                f"{'Private':<10}"
                f"{'Shared':<10}"
                f"{'Swap':<10}"
                f"{'Path'}"
            )

            print("-" * WIDTH)

            for index, mmap in enumerate(memory_maps, start=1):

                rss = getattr(mmap, "rss", 0) // 1024
                size = getattr(mmap, "size", 0) // 1024

                private = (
                    getattr(mmap, "private_clean", 0)
                    + getattr(mmap, "private_dirty", 0)
                ) // 1024

                shared = (
                    getattr(mmap, "shared_clean", 0)
                    + getattr(mmap, "shared_dirty", 0)
                ) // 1024

                swap = getattr(mmap, "swap", 0) // 1024

                path = mmap.path if mmap.path else "[Anonymous]"

                print(
                    f"{index:<5}"
                    f"{rss:<10}"
                    f"{size:<10}"
                    f"{private:<10}"
                    f"{shared:<10}"
                    f"{swap:<10}"
                    f"{path}"
                )

    else:
        print(memory_maps)

    print("-" * WIDTH)
    
        
    
    
