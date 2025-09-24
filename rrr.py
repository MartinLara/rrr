import psutil
import time

# This script monitors and prints the RAM usage of the system.

def get_ram_usage():
    """
    Retrieves the current RAM usage in a human-readable format.
    """
    # Get the virtual memory statistics.
    # The psutil.virtual_memory() method provides information about RAM usage.
    # It returns a named tuple with various attributes.
    ram = psutil.virtual_memory()
    
    # Calculate the total, used, and free RAM in gigabytes (GB).
    # The values from psutil are in bytes, so we convert them to GB for readability.
    total_ram_gb = ram.total / (1024 ** 3)
    used_ram_gb = ram.used / (1024 ** 3)
    free_ram_gb = ram.free / (1024 ** 3)
    
    # Calculate the percentage of RAM used.
    used_percentage = ram.percent
    
    # Return a formatted string with the RAM usage information.
    return (
        f"Total RAM: {total_ram_gb:.2f} GB\n"
        f"Used RAM: {used_ram_gb:.2f} GB ({used_percentage:.1f}%)\n"
        f"Free RAM: {free_ram_gb:.2f} GB"
    )

if __name__ == "__main__":
    print("Starting RAM usage monitoring...")
    print("Press Ctrl+C to stop.\n")
    
    try:
        while True:
            # Clear the terminal for a cleaner display on each update.
            # This works on most Linux-based systems like Raspberry Pi OS.
            print("\033[H\033[J", end="") 
            
            # Get the RAM usage and print it to the console.
            ram_info = get_ram_usage()
            print(ram_info)
            
            # Wait for 1 second before the next update.
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
