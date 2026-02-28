def add_punctuation(sentences):
    result = []
    i = 0
    while i < len(sentences):
        if sentences[i] == " " and i + 1 < len(sentences) and sentences[i+1].isupper():
            result.append(".")
        result.append(sentences[i])
        i += 1
        
    if not result or result[-1] != ".":
        result.append(".")
    return "".join(result)


"""
Given a string of sentences with missing periods, add a period (".") in the following places:

Before each space that comes immediately before an uppercase letter
And at the end of the string
Return the resulting string.


"""