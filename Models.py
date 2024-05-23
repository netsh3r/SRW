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
    __cost_max: dict[int] = {}
    __max_way: list[int] = None

    def __init__(self, graf: dict[tuple[int, int], GrafTable]):
        self.Graf: dict[tuple[int, int], GrafTable] = graf

    # Произвести вычисления данных
    def do_calculate(self):
        self.__prepare_data()
        self.__calculate()
        self.__get_max_way(self.__max_obj, [])
        print(self.__graf_nodes)
        print(self.__desc_graf_nodes)
        for i in [
            "{0}: T: {3} | RN: {1} | RO: {2} | PN: {4}| PO: {5}| RP: {6}".format(i, self.Graf[i].RN, self.Graf[i].RO,
                                                                                 self.Graf[i].T, self.Graf[i].PN,
                                                                                 self.Graf[i].PO,
                                                                                 self.Graf[i].RP) for i in self.Graf]:
            print(i)
        print("MAX: ", self.__max_val, " ", self.__max_obj)
        self.__max_way = sorted(self.__max_way)
        print("Max way: ", " -> ".join(map(str, self.__max_way)))

    # произвести подготовительные данные для работы с нодами
    # построить выходные и входные действия для нод начала и завершения действия
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

    # Получить максимальное значение завершения работы для "раннего времени"
    def __get_max_ro(self, j: int):
        if self.__desc_graf_nodes.get(j) is None:
            return 0
        return max([self.Graf[(gn, j)].RO for gn in self.__desc_graf_nodes[j]])

    # Получить минимальное значение начала работы "позднего времени" по ноде начала действия
    def __get_min_pn(self, i: int):
        if self.__graf_nodes.get(i) is None:
            return 0
        return min([self.Graf[(i, gn)].PN for gn in self.__graf_nodes[i]])

    # Вычислить данные для таблицы
    def __calculate(self):
        # Пройтись по всем нодам начала действий
        for i in self.__graf_nodes.keys():
            # Пройти по всем выходным нодам начала действия
            for j in self.__graf_nodes[i]:
                # Получить граф
                gr = self.Graf[(i, j)]
                # Получить максимальное значение для начала работы "раннего времени"
                gr.RN = self.__get_max_ro(i)
                # Записать значение для завершения работы
                gr.RO = gr.RN + gr.T
                # Если значение завершения работы больше или равно текущему максимальному значению -> перезаписать
                if gr.RO >= self.__max_val:
                    self.__max_val = gr.RO
                    self.__max_obj = (i, j)
        # Пройти по всем нодам завершения действия
        for j in self.__desc_graf_nodes.keys():
            # Пройти по всем входным нодам завершения действия
            for i in self.__desc_graf_nodes[j]:
                # Получить граф
                gr = self.Graf[(i, j)]
                # Если завершающее действие - последнее, то записать максимальное значение
                if j is self.__max_obj[1]:
                    gr.PO = self.__max_val
                # Иначе найти минимальное значение начала работы "позднего времени"
                else:
                    gr.PO = self.__get_min_pn(j)
                # Вычислить начало работы
                gr.PN = gr.PO - gr.T
                # Вычислить резерв времени
                gr.RP = gr.PN - gr.RN

    # Поиск критического пути. На вход получаем верхнюю обработанную ноду и список
    def __get_max_way(self, node: tuple[int, int], res: list[int]):  # (9,11), 30
        # Текущее максимальное значение
        m = 0
        # Максимальная текущая нода
        mn = None
        # Добавить ноду завершения действия
        res.append(node[1])
        # Найти входные ноды в ноду начала действия
        for n in self.__desc_graf_nodes[node[0]]:
            # Если RO больше текущего максимального значения, то заменяем
            if self.Graf[(n, node[0])].RO > m:
                m = self.Graf[(n, node[0])].RO
                mn = (n, node[0])
        # Если дошли до ноды начала (1), то добавляем завершающую ноду и ноду начала и выходим из Рекурсии
        if mn[0] is 1:
            res.append(mn[1])
            res.append(1)
            self.__max_way = res
            return
        else:
            self.__get_max_way(mn, res)
