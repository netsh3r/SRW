class GrafTable:
    def __init__(self, t):
        self.T = t
        self.RN: int = 0
        self.RO: int = 0
        self.PN: int = 0
        self.PO: int = 0
        self.RP: int = 0


class GrafModel:
    __max_val: int = 0
    __max_obj: tuple[int, int] = None
    __graf_nodes: dict[int, list[int]] = {}
    __desc_graf_nodes: dict[int, list[int]] = {}

    def __init__(self, graf: dict[tuple[int, int], GrafTable]):
        self.Graf: dict[tuple[int, int], GrafTable] = graf

    def do_calculate(self):
        self.__prepare_data()
        self.__calculate()
        print(self.__graf_nodes)
        print(self.__desc_graf_nodes)
        for i in [
            "{0}: T: {3} | RN: {1} | RO: {2} | PN: {4}| PO: {5}| RP: {6}".format(i, self.Graf[i].RN, self.Graf[i].RO,
                                                                                 self.Graf[i].T, self.Graf[i].PN,
                                                                                 self.Graf[i].PO,
                                                                                 self.Graf[i].RP) for i in self.Graf]:
            print(i)
        print("MAX: ", self.__max_val, " ", self.__max_obj)

    def __prepare_data(self):
        for g in self.Graf.keys():
            if self.__graf_nodes.get(g[0]) is None:
                self.__graf_nodes[g[0]] = []
            if not self.__graf_nodes.get(g[0]).__contains__(g[1]):
                self.__graf_nodes[g[0]].append(g[1])
            if self.__desc_graf_nodes.get(g[1]) is None:
                self.__desc_graf_nodes[g[1]] = []
            if not self.__desc_graf_nodes.get(g[1]).__contains__(g[0]):
                self.__desc_graf_nodes[g[1]].append(g[0])
        self.__graf_nodes = dict(sorted(self.__graf_nodes.items()))
        self.__desc_graf_nodes = dict(sorted(self.__desc_graf_nodes.items(), reverse=True))

    def __get_max_rn(self, j: int):
        if self.__desc_graf_nodes.get(j) is None:
            return 0
        return max([self.Graf[(gn, j)].RO for gn in self.__desc_graf_nodes[j]])

    def __get_min_pn(self, i: int):
        if self.__graf_nodes.get(i) is None:
            return 0
        return min([self.Graf[(i, gn)].PN for gn in self.__graf_nodes[i]])

    def __calculate(self):
        for i in self.__graf_nodes.keys():
            for j in self.__graf_nodes[i]:
                gr = self.Graf[(i, j)]
                gr.RN = self.__get_max_rn(i)
                gr.RO = gr.RN + gr.T
                if gr.RO >= self.__max_val:
                    self.__max_val = gr.RO
                    self.__max_obj = (i, j)
        for j in self.__desc_graf_nodes.keys():
            for i in self.__desc_graf_nodes[j]:
                gr = self.Graf[(i, j)]
                if j is self.__max_obj[1]:
                    gr.PO = self.__max_val
                else:
                    gr.PO = self.__get_min_pn(j)
                gr.PN = gr.PO - gr.T
                gr.RP = gr.PN - gr.RN
