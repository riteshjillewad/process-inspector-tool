#==================================================================================
#
# THIS MODULE CONTAINS ALL THE NETWORK INFORMATION RELATED TO THE PROCESS
#
#==================================================================================

# Importing necessary modules
import psutil
import socket

#==================================================================================
# Name          : get_connections()
# Description   : Returns the network connections opened by the process
# Input         : Process object
# Output        : Network connections
#==================================================================================

def get_connections(process):
    
    try:
        return process.net_connections()
    
    except psutil.AccessDenied:
        return "Access Denied"

    except psutil.NoSuchProcess:
        return "No such process exists!"
    
#==================================================================================
# Name          : get_connections_count()
# Description   : Returns total number of network connections
# Input         : Process object
# Output        : Number of network connections
#==================================================================================

def get_connections_count(process):
    
    connections = get_connections(process)
    
    if connections is None:
        return None
    
    return len(connections)
    
#==================================================================================
# Name          : show_network_info()
# Description   : Display network related information of the process
# Input         : Process object
# Output        : Network related information
#==================================================================================

def show_network_info(process):
    
    WIDTH = 80
    
    print("\n" + "=" * WIDTH)
    print("NETWORK RELATED INFORMATION".center(WIDTH))
    print("=" * WIDTH)
    
    connection_count = get_connections_count(process)
    
    if connection_count is None:
        print("Unable to retrieve network information.")
        print("=" * WIDTH)
        return
    
    print(f"Total Connections: {connection_count}")
    
    connections = get_connections(process)
    
    if not connections:
        print("\nNo active network connections.")
        print("=" * WIDTH)
        return
    
    print("\n" + "-" * 110)
    print(
        f"{'FD':<6}"
        f"{'Type':<8}"
        f"{'Local Address':<30}"
        f"{'Remote Address':<30}"
        f"{'Status':<20}"
    )
    print("-" * 110)

    for connection in connections:

        # Socket Type
        if connection.type == socket.SOCK_STREAM:
            socket_type = "TCP"

        elif connection.type == socket.SOCK_DGRAM:
            socket_type = "UDP"

        else:
            socket_type = str(connection.type)

        # Local Address
        if connection.laddr:
            local_address = f"{connection.laddr.ip}:{connection.laddr.port}"
        else:
            local_address = "-"

        # Remote Address
        if connection.raddr:
            remote_address = f"{connection.raddr.ip}:{connection.raddr.port}"
        else:
            remote_address = "-"

        # Connection Status
        status = connection.status if connection.status else "-"

        print(
            f"{connection.fd:<6}"
            f"{socket_type:<8}"
            f"{local_address:<30}"
            f"{remote_address:<30}"
            f"{status:<20}"
        )

    print("=" * WIDTH)