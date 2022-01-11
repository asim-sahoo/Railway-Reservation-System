class Temp:
    def __init__(self, filename):
        self.filename = filename
        self.details = None
        self.file = None
        self.load_pass()

    def load_pass(self):
        self.file = open(self.filename, "r")
        self.details = []

        for line in self.file:
            self.details = line

        self.file.close()

    def get_pass(self):
        return self.details
          
    def add_details(self,pnr,tx,dt,mon,fsc,fsn,tsc,tsn,passenger):
        self.details=[pnr,tx,dt,mon,fsc,fsn,tsc,tsn,passenger]
        self.write()

    def write(self):
        with open(self.filename, "w") as f:
            f.write(str(self.details))