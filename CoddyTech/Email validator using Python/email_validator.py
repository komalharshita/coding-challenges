def validate(mail):
    if mail.count('@') != 1:
        return "Email is invalid"
    
    recipient, domain = mail.split('@')
    RECIPIENT_PERMITS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
    DOMAIN_PERMITS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
    
    if not (3 <= len(recipient) <= 12):
        return "Email is invalid"

    domain_name = domain.split('.')[0]  
    if not (3 <= len(domain_name) <= 12):
        return "Email is invalid"
    
    for c in recipient:
        if c not in RECIPIENT_PERMITS:
            return "Email is invalid"
    for c in domain_name:
        if c not in DOMAIN_PERMITS:
            return "Email is invalid"
            
    if recipient.startswith(('.', '_')) or recipient.endswith(('.', '_')):
        return "Email is invalid"
    if domain_name.startswith('-') or domain_name.endswith('-'):
        return "Email is invalid"
    top_level = domain.split('.')[-1]
    valid_domains = ('com', 'net', 'org', 'tech')
    if top_level not in valid_domains:
        return "Email is invalid"
    
    return "Email is valid"

if __name__ == "__main__":
    print("Enter email:")
    email = input()

print(validate(email))