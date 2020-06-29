import graphviz

class Learner:
    def __init__(self, t, a="ab"):
        self.teacher = t
        self.alphabets = a
        self.rows = [""]
        self.columns = [""]
        self.table = self.make_table(self.rows, self.columns)
        self.status = "init"
    def get_row(self, t, r):
        return [t[(r, c)] for c in self.columns]
    def get_row_as_str(self, t, r):
        return "".join(["1" if x else "0" for x in self.get_row(t, r)])
    def make_rows_trans(self):
        rows_trans = []
        for r in self.rows:
            for a in self.alphabets:
                rows_trans.append(r + a)
        return rows_trans
    def update(self):
        rows_trans = self.make_rows_trans()
        table_trans = self.make_table(rows_trans, self.columns)
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
                self.status = "not closed (%s; %s)" % (r, rt)
                return False
        # closed
        # is consistent?
        for i in range(len(self.rows)):
            for j in range(i+1, len(self.rows)):
                if self.get_row(self.table, self.rows[i]) == self.get_row(self.table, self.rows[j]):
                    for a in self.alphabets:
                        if self.get_row(table_trans, self.rows[i]+a) != self.get_row(table_trans, self.rows[j]+a):
                            #incosnsitent!
                            newcol = [a+c for c in self.columns]
                            self.columns += newcol
                            self.status = "not consistent (%s, %s; %s)" % (self.rows[i], self.rows[j], a)
                            self.table = self.make_table(self.rows, self.columns)
                            return False
        self.status = "ok"
        return True
    def make_table(self, rows_, columns_):
        t = {}
        for row in rows_:
            for col in columns_:
                t[(row, col)] = self.teacher(row + col)
        return t
    def print_table(self):
        rows_trans = []
        for r in self.rows:
            for a in self.alphabets:
                rows_trans.append(r + a)
        table_trans = self.make_table(rows_trans, self.columns)
        def f(x):
            if x == "":
                return "[]"
            else:
                return x

        print("<table rules=groups>")
        print("<colgroup/>")
        print("<thead>")
        print("<tr>")
        print("<td>*</td>")
        for c in self.columns:
            print("<td>%s</td>" % f(c))
        print("</tr>")
        print("</thead>")
        print("<tbody>")                
        for r in self.rows:
            print("<tr>")
            print("<td>%s</td>" % f(r))
            for c in self.columns:
                print("<td>%s</td>" % self.table[(r, c)])
            print("</tr>")
        print("</tbody>")
        print("<tbody>")                        
        for r in rows_trans:
            print("<tr>")
            print("<td>%s</td>" % f(r))            
            for c in self.columns:
                print("<td>%s</td>" % table_trans[(r, c)])
            print("</tr>")
        print("</tbody>")                                    
        print("</table>")
    def learn(self, exs=[]):
        print("<html>")
        self.print_table()
        print("<hr/>")
        while True:
            self.update()
            self.print_table()
            print("status:%s" % self.status)
            print("<hr/>")
            if self.status == "ok":
                if len(exs) == 0:
                    break
                else:
                    ex = exs.pop(0)
                    for i in range(len(ex)):
                        prefix = ex[:i]
                        if self.rows.count(prefix) == 0:
                            print("<p>Adding %s into the table.</p>" % prefix)
                            self.rows.append(prefix)
                        self.table = self.make_table(self.rows, self.columns)
                    print("<hr/>")
        print("</html>")
    def draw(self):
        d = graphviz.Digraph()
        starting = [self.get_row_as_str(self.table, "")]
        accepting = []
        for i in self.rows:
            if self.table[(i, "")]:
                accepting.append(self.get_row_as_str(self.table, i))
        def f(s):
            ss = s
            if s in starting:
                ss += "S"
            if s in accepting:
                ss += "A"
            return ss
        for i in self.rows:
            d.node(f(self.get_row_as_str(self.table, i)))
        done = set()
        for i in self.rows:
            src_str = f(self.get_row_as_str(self.table, i))
            rows_trans = self.make_rows_trans()
            next_table = self.make_table(rows_trans, self.columns)
            for a in self.alphabets:
                dest = i + a
                dest_str = f(self.get_row_as_str(next_table, dest))
                if (src_str, dest_str, a) in done:
                    continue
                d.edge(src_str, dest_str, a)
                done.add((src_str, dest_str, a))
                # print("hoge")
        return d


        


def teacher_even(s):
    return (s.count("a")%2 == 0 and s.count("b")%2 == 0)


if __name__ == "__main__":
    exs = ["ab","abab"]


    l = Learner(teacher_even)
    l.learn(exs)    

            
            
