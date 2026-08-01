#==================================================================================
#   
#   ENTRY POINT FUNCTION OF APPLICATION
#
#==================================================================================

import sys

from utils.banner import show_banner
from utils.banner import show_manual
from utils.banner import show_about
from utils.banner import show_footer

from process_info.process_object import create_process
from process_info.basic import show_basic_info
from process_info.cpu import show_cpu_info
from process_info.memory import show_memory_info
from process_info.threads import show_thread_info
from process_info.files import show_file_info
from process_info.network import show_network_info
from process_info.io import show_io_info
from process_info.children import show_children_info

#=================================================================================
# Name       : get_pid()
# Description: Function to read and validate process PID
# Input      : PID (command line)
# Output     : int (valid process id)
#==================================================================================

def get_pid():
    
    # Filter to check number of arguments
    if len(sys.argv) != 2:
        print("ERROR: Invalid number of arguments")
        print("Use 'python main.py --help' for usage information.")
        print()
        sys.exit(1)
        
    # Fetching the PID
    argument = sys.argv[1]
    
    # case 1: usage: --h or --help
    if argument == "--h" or argument == "--help":
        show_manual()
        show_footer()
        sys.exit(0)
        
    # case 2: usage: --a or --about
    if argument == "--a" or argument == "--about":
        show_about()
        show_footer()
        sys.exit(0)
        
    # PID validation
    try:
        pid = int(argument)
        
        if pid <= 0:
            raise ValueError
        
        return pid
    
    except ValueError:
        print("ERROR: PID must be a positive integer")
        sys.exit(1)
        

#==================================================================================
# Name       : main()
# Description: Entry point function
#==================================================================================

def main():
    
    show_banner()
    
    # We get the required pid
    pid = get_pid()
    
    # We get the process object using that pid
    process = create_process(pid)
    
    # Now we can access the psutil functions 
    print(f"\nTarget Process ID : {process.pid}")
    
    # <--- OUR UTILITY FUNCTIONS --->
    show_basic_info(process)
    show_cpu_info(process)
    show_memory_info(process)
    show_thread_info(process)
    show_file_info(process)
    show_network_info(process)
    show_io_info(process)
    show_children_info(process)
    
    show_footer()
    
#==================================================================================
# STARTER FUNCTION
#==================================================================================
if __name__ == "__main__":
    main()
    