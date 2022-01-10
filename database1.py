class DataBase1:
    def __init__(self, filename):
        self.filename = filename
        self.train = None
        self.file = None
        self.load_train()

    def load_train(self):
        self.file = open(self.filename, "r")
        self.train = []

        for line in self.file:
            self.train = line

        self.file.close()

    def get_train(self):
        for i in self.train:
            return i
    def get_data(self):
        return self.train

    def add_train(self,tx,dt,mon,fsc,fsn,tsc,tsn):
        self.train = [tx,dt,mon,fsc,fsn,tsc,tsn]
        self.save()

    def save(self):
        with open(self.filename, "w") as f:
            f.write(str(self.train))