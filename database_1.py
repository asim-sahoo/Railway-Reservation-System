class DataBase1:
    def __init__(self, filename):
        self.filename = filename
        self.train = None
        self.file = None
        self.load_train()

<<<<<<< HEAD
    def load_train(self):
        self.file = open(self.filename, "r")
        self.train = []

        for line in self.file:
            self.train = line

        self.file.close()

    def get_train(self):
        for i in self.train:
            return i

    def add_train(self,tx):
        self.train = [tx]
=======
    def add_train(self, f_st, t_st, date, month, day):
        self.train = [f_st,";", t_st,";", date,";", month,";", day]
>>>>>>> 74274e71cfe55309511ea99273a69e3fc633e110
        self.save()
        return 1

    def save(self):
        with open(self.filename, "w") as f:
            for i in range(9):
                f.write(self.train[i])