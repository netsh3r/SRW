class GrafTable:
    def __init__(self, db: range):
        self.T = db[0]
        self.RN = db[1]
        self.RO = db[2]
        self.PN = db[3]
        self.PO = db[4]
        self.RRP = db[5]
        self.RRN = db[6]

    def set_rn(self, rn):
        self.RN = rn
        self.RO = rn + self.T
