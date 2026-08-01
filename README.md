# 🖥️ Process Inspector Tool

A **Python Command-Line Utility** to inspect and display detailed information about running system processes using the **psutil** library.

The tool accepts a **Process ID (PID)** as input and provides comprehensive information about the selected process, including CPU usage, memory consumption, threads, files, network connections, disk I/O, and child processes.

This project is designed to demonstrate **Python system programming**, **process management**, **modular programming**, and **command-line application development**.

---

## 📌 Features

- Display basic process information
- Display CPU information
- Display memory usage
- Display thread information
- Display open files
- Display executable path
- Display working directory
- Display network connections
- Display disk I/O statistics
- Display parent and child processes
- Professional command-line interface
- Modular project architecture
- Error handling for invalid PID and permission issues

---

# 📂 Project Structure

```
process-inspector-tool/
│
├── main.py
├── requirements.txt
├── README.md
│
├── process_info/
│   ├── __init__.py
│   ├── process_object.py
│   ├── basic.py
│   ├── cpu.py
│   ├── memory.py
│   ├── threads.py
│   ├── files.py
│   ├── network.py
│   ├── io.py
│   └── children.py
│
└── utils/
    ├── __init__.py
    ├── banner.py
    ├── constants.py
    ├── size_utils.py
    └── time_utils.py
```

---

# ⚙️ Requirements

- Python 3.8+
- psutil

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/process-inspector-tool.git
```

Move into the project directory

```bash
cd process-inspector-tool
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📄 requirements.txt

```
psutil
```

---

# 🚀 Usage

Run the program

```bash
python main.py <PID>
```

Example

```bash
python main.py 1234
```

---

# 📚 Command-Line Options

Display help page

```bash
python main.py --help
```

Display project information

```bash
python main.py --about
```

Display version

```bash
python main.py --version
```

---

# 📖 Information Displayed

## 1. Basic Information

- Process ID
- Parent Process ID
- Process Name
- Process Status
- Username
- Executable Path
- Working Directory
- Command Line
- Creation Time
- Priority
- Running Status

---

## 2. CPU Information

- CPU Usage Percentage
- CPU Times
- CPU Affinity
- CPU Number
- Process Priority
- Context Switches

---

## 3. Memory Information

- RSS Memory
- VMS Memory
- Shared Memory
- Text Memory
- Data Memory
- USS Memory
- PSS Memory
- Swap Memory
- Memory Usage Percentage

---

## 4. Thread Information

- Total Threads
- Thread ID
- User Time
- System Time

---

## 5. File Information

- Executable Path
- Current Working Directory
- Open Files
- Memory Mapped Files

---

## 6. Network Information

- Total Connections
- Socket Type
- Local Address
- Remote Address
- Connection Status

---

## 7. Disk I/O Information

- Read Operations
- Write Operations
- Bytes Read
- Bytes Written
- Characters Read
- Characters Written

---

## 8. Parent & Child Processes

### Parent Process

- PID
- Name
- Status
- Creation Time

### Child Processes

- PID
- Name
- Status
- Creation Time

---

# 🛠 Technologies Used

- Python
- psutil
- sys
- socket
- datetime

---

# 📚 Python Concepts Used

- Modules
- Packages
- Functions
- Exception Handling
- Command-Line Arguments
- Modular Programming
- Object-Oriented APIs
- Process Management
- File Handling
- Network Programming
- System Programming

---

# ❗ Error Handling

The application gracefully handles various runtime exceptions.

Examples include:

- Invalid PID
- Process does not exist
- Access denied
- Zombie process
- Unsupported platform-specific features

---

# 📷 Sample Output

```
======================================================================
                      PROCESS INSPECTOR TOOL
======================================================================

PID                  : 1234
Name                 : python.exe
Status               : Running

======================================================================
CPU INFORMATION
======================================================================

CPU Usage            : 8.25 %
CPU Number           : 4

======================================================================
MEMORY INFORMATION
======================================================================

RSS Memory           : 31.42 MB
VMS Memory           : 156.20 MB

======================================================================
THREAD INFORMATION
======================================================================

Total Threads        : 7

======================================================================
NETWORK INFORMATION
======================================================================

Connections          : 2

======================================================================
I/O INFORMATION
======================================================================

Bytes Read           : 18.24 MB
Bytes Written        : 9.31 MB

======================================================================
```

---

# 🎯 Learning Objectives

This project demonstrates:

- System Programming using Python
- Process Inspection using psutil
- Python Package Organization
- Writing Professional CLI Applications
- Modular Software Design
- Python Exception Handling
- Working with Operating System APIs

---

# 🔮 Future Improvements

Potential enhancements include:

- Process Tree View
- Live Monitoring Mode
- Search Process by Name
- Colored Terminal Output
- Interactive CLI Menu
- CPU & Memory Graphs
- Logging Support
- Unit Tests
- Cross-platform Performance Optimizations

---

# 👨‍💻 Author

**Ritesh Jillewad**

Final Year B.Tech (Computer Science & Engineering - AI & DS)

---

# 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute it for learning and educational purposes.

---

# ⭐ If you found this project useful

Consider giving the repository a **Star ⭐** on GitHub.