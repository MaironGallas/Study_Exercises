def create_phone_number(n):
    n_string = str(n)[1:-1].replace(', ', '')
    return f"({n_string[0:3]}) {n_string[3:6]}-{n_string[6:10]}"
