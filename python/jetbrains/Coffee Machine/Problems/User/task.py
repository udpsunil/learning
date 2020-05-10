class User:
    # create the class here
    n_active = 0
    users = []

    def __init__(self, active, name):
        self.active = active
        self.user_name = name
