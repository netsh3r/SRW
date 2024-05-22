from Models import GrafTable, GrafModel

graf = {
    (1, 2): GrafTable(7),
    (1, 3): GrafTable(5),
    (3, 4): GrafTable(6),
    (2, 5): GrafTable(5),
    (2, 6): GrafTable(6),
    (2, 7): GrafTable(12),
    (5, 8): GrafTable(3),
    (6, 8): GrafTable(3),
    (8, 9): GrafTable(3),
    (7, 9): GrafTable(6),
    (4, 10): GrafTable(11),
    (9, 11): GrafTable(5),
    (10, 11): GrafTable(4)
}


def main():
    graf_obj = GrafModel(graf)
    graf_obj.do_calculate()


if __name__ == "__main__":
    main()
