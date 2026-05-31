class AuthService:
    @staticmethod
    def login(daftar_user, username_input, password_input):
        for user in daftar_user:
            if user.login(username_input, password_input):
                return user
        return None

    @staticmethod
    def logout(user):
        if user:
            user.logout()
