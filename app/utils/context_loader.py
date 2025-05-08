def load_company_context():
    try:
        with open("app/assets/company_profile.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Company info not found."