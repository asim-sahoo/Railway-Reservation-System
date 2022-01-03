import datetime

class DataBase1:
    def __init__(self, filename):
        self.filename = filename
        self.train = None
        self.file = None

    def add_train(self, f_st, t_st, date, month, day):
        self.train = [f_st.strip(), t_st.strip(), date.strip(), month.strip(), day.strip()]
        self.save()
        return 1

    def save(self):
        with open(self.filename, "w") as f:
            for i in self.train:
                f.write(i)