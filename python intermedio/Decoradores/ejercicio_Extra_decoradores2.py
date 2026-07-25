user_logged_in = True

def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise Exception("Unauthenticated user")
        return func(*args, **kwargs)
    return wrapper


@requires_login
def view_profile(user):
    print("Showing user's profile", user)


try:
    view_profile("Abner")
except Exception as e:
    print("Error:", e)