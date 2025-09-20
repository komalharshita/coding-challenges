
def number_of_files(file_size, file_unit, drive_size_gb):
    num_files = 0

    if file_unit == "B":
        file_size_gb = file_size / 1_000_000_000  

    elif file_unit == "KB":
        file_size_gb = file_size / 1_000_000  

    elif file_unit == "MB":
        file_size_gb = file_size / 1_000  
        
    else:
        raise ValueError("Invalid file unit. Use 'B', 'KB', or 'MB'.")

    num_files = int(drive_size_gb / file_size_gb)
    
    return num_files