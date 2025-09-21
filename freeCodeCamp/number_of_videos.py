def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    unit_conversion = {
        "KB": 1000,
        "MB": 1000**2,
        "GB": 1000**3,
        "TB": 1000**4
    }

    valid_video_units = ["KB", "MB", "GB"]
    valid_drive_units = ["GB", "TB"]

    if video_unit not in valid_video_units:
        return "Invalid video unit"
    if drive_unit not in valid_drive_units:
        return "Invalid drive unit"

    video_size_in_bytes = video_size * unit_conversion[video_unit]
    drive_size_in_bytes = drive_size * unit_conversion[drive_unit]

    return drive_size_in_bytes // video_size_in_bytes

