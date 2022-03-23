from player import Player
from tree import Tree

from scipy.optimize import differential_evolution

import pandas as pd


def loss(x, table: pd.DataFrame, paraRoute: list, route: list):
    def line(a: Player, loc1, loc2, table=table):
        # 从一个地点到另一个地点
        STEP = table.at[loc1, loc2]
        while a.step != STEP:
            if not a.walk(a.day):
                return False
            # print(a.day, a.step, a.Weather[a.day])
        a.step = 0
        return True

    def mine(a: Player, T, table=table):
        if T > 0:  # 决定在矿山工作必须休息一天

            a.rest(a.day)
        T = a.day + T
        while a.day <= T:
            if not a.mining(a.day):
                return False
        return True

    a = Player()
    #print(x)
    X = [int(x[i] * j) for i, j in enumerate(paraRoute)]

    t = []
    for i in range(len(route) - 1):
        if route[i] in [1,15]:
            # t.append(a.buy(X.pop(0), X.pop(0)))
            t.append(a.buy(X.pop(0), X.pop(0), i))
        # if route[i] in [15]:
        #     # t.append(a.buy(X.pop(0), X.pop(0)))
        #     t.append(a.buy(X.pop(0), X.pop(0), 2))
        elif route[i] in [12]:
            t.append(mine(a, X.pop(0)))
        t.append(line(a, route[i], route[i + 1]))

    if not all(t):  # 生存时间越长分数越高
        score = 10
        for i in t:
            if i:
                score -= 1
            else:
                break
        return score
    return -a.score()


table = pd.read_excel("./最短天数邻阶矩阵.xlsx", index_col=0, header=0)
List = list(table.index)

a = Tree(List, table)
for leaf in a.leaList:
    route = []
    Tree.output(leaf, route)
    para = Tree.routeToPara(route)
    #print(para)
    # 差分进化算法
    res = differential_evolution(loss, bounds=[(0, 1) for i in range(para[0])], disp=False, popsize=10,
                                 args=(table, para[1], route))
    print(route, [int(res.x[i] * j) for i, j in enumerate(para[1])], -res.fun, sep='\t')

