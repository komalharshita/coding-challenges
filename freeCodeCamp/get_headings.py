def get_headings(csv):
    lst = [ heading.strip() for heading in csv.split(",")]
    return lst


"""
Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

The first line of a CSV file contains headings separated by commas.
Remove any leading or trailing whitespace from each heading.
"""