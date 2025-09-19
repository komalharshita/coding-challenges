def number_of_photos(photo_size_mb, drive_size_gb):
    nop = 0
    drive_size_mb = drive_size_gb * 1000

    nop = drive_size_mb // photo_size_mb

    return nop


"""
Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB), 
return the number of photos the hard drive can store using the following constraints:
1 gigabyte equals 1000 megabytes.
Return the number of whole photos the drive can store.

"""