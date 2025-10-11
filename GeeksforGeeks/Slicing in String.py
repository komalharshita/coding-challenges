def join_middle(bound_by, tag_name):
    n = len(bound_by)
    n //= 2

    return bound_by[:n] + tag_name + bound_by[n:]