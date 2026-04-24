def is_valid_variable(name):
    if not name:
        return False

    # Must not start with digit
    if name[0].isdigit():
        return False

    # Only letters, digits, underscore
    for ch in name:
        if not (ch.isalnum() or ch == "_"): # isalnum = alpha + numeric = a-z, A-Z, 0-9
            return False

    return True


# Main
var = input("Enter variable name: ")

if is_valid_variable(var):
    print("Accepted")
else:
    print("Rejected")