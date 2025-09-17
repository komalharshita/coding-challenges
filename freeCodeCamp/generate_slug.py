def generate_slug(string):
    res = ""
    string = string.lower()
    for char in string:
        if char.isalnum() or char.isspace():
            if char == " ":
                if res and not res.endswith("%20"):
                    res += "%20"
            else:
                res += char
    return res.strip("%20")