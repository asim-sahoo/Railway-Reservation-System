class DataBase2:
    def __init__(self, filename):
        self.filename = filename
        self.details = None
        self.file = None
        self.load_pnr()

    def load_pnr(self):
        self.file = open(self.filename, "r")
        self.details = {}

        for line in self.file:
            pnr,tx,dt,mon,fsc,fsn,tsc,tsn,passenger = line.strip().split(";")
            self.details[pnr] = (pnr,tx,dt,mon,fsc,fsn,tsc,tsn,passenger)
            # self.details.append(line)
        

        self.file.close()
    def get_pnr(self,pnr):
        if pnr in self.details:
            return self.details[pnr]
        else:
            return -1
        # return self.details
    def add_details(self,pnr,tx,dt,mon,fsc,fsn,tsc,tsn,passenger):
        self.details[pnr.strip()]=[pnr.strip(),tx.strip(),dt.strip(),mon.strip(),fsc.strip(),fsn.strip(),tsc.strip(),tsn.strip(),passenger]
        self.write()
    
    def validate(self, pnr):
        if self.get_pnr(pnr) != -1:
            return self.details[pnr][0] == pnr
        else:
            return False

    def write(self):
        with open(self.filename, "w") as f:
            for user in self.details:
                f.write(self.details[user][0] + ";" + self.details[user][1] + ";" + self.details[user][2] + ";" + self.details[user][3] + ";" + self.details[user][4] + ";" + self.details[user][5] + ";" + self.details[user][6] + ";" + self.details[user][7] + ";" + str(self.details[user][8]) + "\n")
            # f.write(str(self.details)+";")

        