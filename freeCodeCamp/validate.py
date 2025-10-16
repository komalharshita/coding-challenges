def validate(email):
    if email.count('@') != 1:
        return False
    
    recipient, domain = email.split('@')
    valid = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-_.'
    
    if recipient.startswith('.') or recipient.endswith('.'):
        return False
    
    if '..' in recipient or '..' in domain:
        return False
    
    for c in recipient:
        if c not in valid:
            return False
    
    if '.' not in domain or domain.endswith('.') or len(domain.split('.')[-1]) < 2:
        return False

    return True


"""
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.
"""