#==================================================================================
#
#   THIS FUNCTION WILL DISPLAY BANNER ACROSS OUR APPLICATION
#
#==================================================================================

# GLOBAL VARIABLES
WIDTH = 80
INNER_WIDTH = WIDTH - 2

#==================================================================================
# Name       : show_banner() 
# Description: Displays the banner at start
# Input      : None
# Output     : None
#==================================================================================

def show_banner():
        
    print()
    print("=" * WIDTH)
    
    print("|" + "".center(INNER_WIDTH) + "|")
    
    print("|" + "PROCESS INSPECTOR TOOL".center(INNER_WIDTH) + "|")
    
    print("|" + "".center(INNER_WIDTH) + "|")
    
    print("|" + "A Python Command-Line Utility for Process Inspection".center(INNER_WIDTH) + "|")
    
    print("|" + "".center(INNER_WIDTH) + "|")
    
    print("|" + "Inspect running processes, monitor resource usage, and".center(INNER_WIDTH) + "|")
    print("|" + "retrieve detailed system-level process information using psutil.".center(INNER_WIDTH) + "|")
    
    print("|" + "".center(INNER_WIDTH) + "|")
    
    print("=" * WIDTH)
    
#==================================================================================
# Name       : show_manual() 
# Description: Displays the manual page for the project
# Input      : None
# Output     : None
#==================================================================================

def show_manual():
        
    print("=" * WIDTH)
    print("|" + "USER MANUAL".center(INNER_WIDTH) + "|")
    print("=" * WIDTH)

    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("|" + " DESCRIPTION".ljust(INNER_WIDTH) + "|")
    print("|" + "   Process Inspector Tool displays detailed information".ljust(INNER_WIDTH) + "|")
    print("|" + "   about any running process using its Process ID (PID).".ljust(INNER_WIDTH) + "|")

    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("|" + " USAGE".ljust(INNER_WIDTH) + "|")
    print("|" + "   python main.py <PID>".ljust(INNER_WIDTH) + "|")

    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("|" + " EXAMPLES".ljust(INNER_WIDTH) + "|")
    print("|" + "   python main.py 1234".ljust(INNER_WIDTH) + "|")
    print("|" + "   python main.py 5678".ljust(INNER_WIDTH) + "|")

    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("|" + " OPTIONS".ljust(INNER_WIDTH) + "|")
    print("|" + "   -h, --help      Show this manual".ljust(INNER_WIDTH) + "|")
    print("|" + "   -a, --about     About the project".ljust(INNER_WIDTH) + "|")

    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("|" + " NOTES".ljust(INNER_WIDTH) + "|")
    print("|" + "   • PID must be a valid running process.".ljust(INNER_WIDTH) + "|")
    print("|" + "   • Administrator privileges may be required".ljust(INNER_WIDTH) + "|")
    print("|" + "     for inspecting some system processes.".ljust(INNER_WIDTH) + "|")

    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("=" * WIDTH)
    
#==================================================================================
# Name       : show_about() 
# Description: Displays the about page for the project
# Input      : None
# Output     : None
#==================================================================================
    
def show_about():

    print("=" * WIDTH)
    print("|" + "ABOUT".center(INNER_WIDTH) + "|")
    print("=" * WIDTH)

    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("|" + " Process Inspector Tool is a command-line application developed".ljust(INNER_WIDTH) + "|")
    print("|" + " using Python and the psutil library.".ljust(INNER_WIDTH) + "|")
    
    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("|" + " The project allows users to inspect any running process by".ljust(INNER_WIDTH) + "|")
    print("|" + " providing its Process ID (PID).".ljust(INNER_WIDTH) + "|")
    
    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("|" + " The tool retrieves important process information including:".ljust(INNER_WIDTH) + "|")
    
    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("|" + "  • General Information".ljust(INNER_WIDTH) + "|")
    print("|" + "  • Process Status".ljust(INNER_WIDTH) + "|")
    print("|" + "  • CPU Usage".ljust(INNER_WIDTH) + "|")
    print("|" + "  • Memory Usage".ljust(INNER_WIDTH) + "|")
    print("|" + "  • Thread Information".ljust(INNER_WIDTH) + "|")
    print("|" + "  • Parent Process Details".ljust(INNER_WIDTH) + "|")
    print("|" + "  • Open Files".ljust(INNER_WIDTH) + "|")
    print("|" + "  • Network Connections".ljust(INNER_WIDTH) + "|")
    print("|" + "  • I/O Statistics".ljust(INNER_WIDTH) + "|")
    print("|" + "  • Creation Time".ljust(INNER_WIDTH) + "|")
    print("|" + "  • Executable Path".ljust(INNER_WIDTH) + "|")
    print("|" + "  • Command-Line Arguments".ljust(INNER_WIDTH) + "|")
    print("|" + "  • User Information".ljust(INNER_WIDTH) + "|")
    
    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("|" + " The primary objective of this project is to demonstrate".ljust(INNER_WIDTH) + "|")
    print("|" + " system programming concepts, process management, and the".ljust(INNER_WIDTH) + "|")
    print("|" + " effective use of the psutil library for system monitoring.".ljust(INNER_WIDTH) + "|")
    
    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("|" + " The project follows a modular architecture for improved".ljust(INNER_WIDTH) + "|")
    print("|" + " readability, maintainability, and future enhancements.".ljust(INNER_WIDTH) + "|")
    
    print("|" + "".ljust(INNER_WIDTH) + "|")
    print("=" * WIDTH)
    
#==================================================================================
# Name       : show_footer() 
# Description: Displays the footer page for the project
# Input      : None
# Output     : None
#==================================================================================  

def show_footer():

    print("-" * WIDTH)
    
    print("|" + "".center(INNER_WIDTH) + "|")
    
    print("|" + "Version : 1.0.0".center(INNER_WIDTH) + "|")
    print("|" + "Author  : Ritesh Jillewad".center(INNER_WIDTH) + "|")
    print("|" + "Python  : 3.x".center(INNER_WIDTH) + "|")
    print("|" + "Library : psutil".center(INNER_WIDTH) + "|")
    
    print("|" + "".center(INNER_WIDTH) + "|")
    
    print("-" * WIDTH)
