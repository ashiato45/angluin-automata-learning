class Learner:
    def __init__(self, t, a="01"):
        self.teacher = t
        self.alphabets = a
        self.rows = [""]
        self.columns = [""]
        self.table = self.make_table(self.rows, self.columns)
    def get_row(self, t, r):
        return [t[(r, c)] for c in self.columns]
    def update(self):
        rows_trans = []
        for r in self.rows:
            for a in self.alphabets:
                rows_trans.append(r + a)
        print("rows_trans:", rows_trans)
        table_trans = self.make_table(rows_trans, self.columns)
        print("table_trans:", table_trans)
        # is closed?
        for rt in rows_trans:
            found = False
            for r in self.rows:
                if self.get_row(table_trans, rt) == self.get_row(self.table, r):
                    found = True
                    break
            if not found:
                # not closed
                self.rows.append(rt)
                self.table = self.make_table(self.rows, self.columns)
                return False
        # closed
        print("closed")
        # is consistent?
        for i in range(len(self.rows)):
            for j in range(i+1, len(self.rows)):
                print("hoge:", self.rows[i], self.rows[j])
                if self.get_row(self.table, self.rows[i]) == self.get_row(self.table, self.rows[j]):
                    for a in sef.alphabets:
                        if get_row(table_trans, self.rows[i]+a) != get_row(table_trans, self.rows[j]+a):
                            #incosnsitent!
                            newcol = [c+a for c in self.columns]
                            self.columns += newcol
                            return False
        return True
    def make_table(self, rows_, columns_):
        t = {}
        for row in rows_:
            for col in columns_:
                t[(row, col)] = self.teacher(row + col)
        return t


def teacher_even(s):
    return (s.count("0")%2 == 0 and s.count("1")%2 == 0)
l = Learner(teacher_even)

print(l.rows, l.columns)
print("table:", l.table)
print("-"*80)
while not l.update():
    print(l.rows, l.columns)
    print("table:", l.table)
    print("-"*80)

        
        
