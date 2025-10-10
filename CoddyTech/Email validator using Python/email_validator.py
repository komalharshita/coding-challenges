def validate(mail):
    if mail.count('@') != 1:
        return False
    
    recipient, domain = mail.split('@')
    PERMITS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
    
    if not (3 <= len(recipient) <= 24):
        return False
    
    for c in recipient:
        if c not in PERMITS:
            return False
            
    if recipient.startswith(('.', '_')) or recipient.endswith(('.', '_')):
        return False
   
    return True

