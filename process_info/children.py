#==================================================================================
#
# THIS MODULE CONTAINS ALL THE CHILD PROCESS INFORMATION RELATED TO THE PROCESS
#
#==================================================================================

import psutil

from utils.time_utils import timestamp_to_date

#==================================================================================
# Name          : get_parent_process()
# Description   : Returns the parent process
# Input         : Process object
# Output        : Parent process
#==================================================================================

def get_parent_process(process):
    
    try:
        return process.parent()
    
    except psutil.NoSuchProcess:
        return "No such process exists!"
    
    except psutil.AccessDenied:
        return "Access Denied"
    
#==================================================================================
# Name          : get_child_processes()
# Description   : Returns the child process
# Input         : Process object
# Output        : Child process
#==================================================================================

def get_child_process(process):
    
    try:
        return process.children()
    
    except psutil.NoSuchProcess:
        return "No such process exists!"
    
    except psutil.AccessDenied:
        return "Access Denied"
    
#==================================================================================
# Name          : get_child_count()
# Description   : Returns the total number of child process
# Input         : Process object
# Output        : Child process
#==================================================================================

def get_child_count(process):
    
    children = get_child_process(process)
    
    if children is None:
        return None
    
    return len(children)

#==================================================================================
# Name          : show_children_info()
# Description   : Displays parent and child process information
# Input         : Process object
# Output        : Child process
#==================================================================================

def show_children_info(process):
    
    WIDTH = 80
    
    print("\n" + "=" * WIDTH)
    print("PARENT/CHILD PROCESS INFORMATION".center(WIDTH))
    print("=" * WIDTH)
    
    # -------------------------- PARENT PROCESS INFO --------------------------
    
    parent = get_parent_process(process)
    
    print("\nParent Process")
    
    if parent:
        
        try:
            print(f"{'PID':20}: {parent.pid}")
            print(f"{'Name':20}: {parent.name()}")
            print(f"{'Status':20}: {parent.status()}")
            print(
                f"{'Created':20}: "
                f"{timestamp_to_date(parent.create_time())}"
            )

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            print("Unable to retrieve parent process details.")

    else:
        print("No parent process found.")
        
        # ---------------- Child Processes ----------------

    children = get_child_process(process)

    if children is None:

        print("\nUnable to retrieve child processes.")
        print("=" * WIDTH)
        return

    print("\n" + "-" * WIDTH)
    print(f"Child Processes : {len(children)}")
    print("-" * WIDTH)

    if not children:

        print("No child processes.")

    else:

        print(
            f"{'PID':<10}"
            f"{'Name':<30}"
            f"{'Status':<18}"
            f"{'Created'}"
        )

        print("-" * WIDTH)

        for child in children:

            try:

                print(
                    f"{child.pid:<10}"
                    f"{child.name():<30}"
                    f"{child.status():<18}"
                    f"{timestamp_to_date(child.create_time())}"
                )

            except (psutil.NoSuchProcess, psutil.AccessDenied):

                continue
            
    print("=" * WIDTH)
            
    

    
