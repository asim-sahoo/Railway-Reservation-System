class DataBase1:
    def __init__(self, filename):
        self.filename = filename
        self.train = None
        self.file = None

    def add_train(self, f_st, t_st, date, month, day):
        self.train = [f_st,";", t_st,";", date,";", month,";", day]
        self.save()
        return 1

    def save(self):
        with open(self.filename, "w") as f:
            for i in range(9):
                f.write(self.train[i])