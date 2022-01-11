class DataBase2:
    def __init__(self, filename):
        self.filename = filename
        self.details = None
        self.file = None

    def add_details(self,pnr,tx,dt,mon,fsc,fsn,tsc,tsn,passenger):
        self.details=[pnr,tx,dt,mon,fsc,fsn,tsc,tsn,passenger]
        self.write()

    def write(self):
        with open(self.filename, "a") as f:
            f.write(str(self.details)+"\n")

        