def main():
    print("Welcome to email slicer...")
    email_input = input("enter your email")
    username, domain = email_input.split("@")
    domain_name, TLD = domain.split(".")
    print(
        f"""
    Username: {username}
    Domain: {domain_name}
    Top Level Domain: {TLD}
    """
    )


main()
