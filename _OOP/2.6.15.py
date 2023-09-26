class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email: str):
        if isinstance(email, str) and len(email.split("@")) == 2 and "." in email[email.find("@"):]:
            self.__email = email
        else:
            print(f"ErrorMail:{email}")

    email = property(fget=get_email, fset=set_email)
            