# 文件名：生成树
import pandas as pd


# 构建节点
class Node():
    def __init__(self, ID: int, distance=0, parent=None):
        self.ID = ID
        self.distance = distance
        self.parent = parent
        self.son = []

    def add_son(self, s):
        if isinstance(s, list):
            self.son.extend(s)
        else:
            self.son.append(s)
        pass


class Tree():
    """通过位置ID列表，构建从起点到重点的路径树"""

    def __init__(self, List: list, table: pd.DataFrame):
        self.T = table

        self.r = Node(List[0])
        self.L = List[1:]

        self.__tree(self.r)
        self.leaList = []
        self.__out(self.r)

        pass

    # 生成树
    def __tree(self, a: Node):
        if a.ID == 27:  # 叶节点
            return None
        a.son = [Node(i, self.T.at[a.ID, i] + a.distance, a)
                 for i in self.L
                 if self.T.at[a.ID, i] > 0 and self.T.at[a.ID, i] + a.distance + self.T.at[i, 27] <= 30]
        if not a.son:
            # 叶节点
            # table.at[a.ID,i] + a.distance + table.at[i,27] >= 30 就为叶节点
            return None
        for j in a.son:
            self.__tree(j)

    def __out(self, a: Node):
        # 输出所有叶节点
        if not a.son:
            self.leaList.append(a)
        for i in a.son:
            self.__out(i)

    @staticmethod
    def output(b: Node, s: list):
        """
        :param b: 叶节点
        :param s: 含叶节点ID的列表
        :return: 路径
        """
        if s == []:
            s.append(b.ID)
        if b.parent == None:
            return
        s.insert(0, b.parent.ID)
        Tree.output(b.parent, s)

    @staticmethod
    def routeToPara(r: list):
        """
        :param r:路线列表
        :return: the number of parameters and the bounds of parameters
        """
        Dict = {1: [2, [400, 600]], 12: [1, [30]], 15: [2, [400, 600]], 27: [0, []]}
        a = []
        [a.extend(Dict[r[i]][1]) for i in range(len(r))]
        return sum(Dict[r[i]][0] for i in range(len(r))), a


# if __name__ == '__main__':
#
#     table = pd.read_excel("./最短天数邻阶矩阵.xlsx", index_col=0, header=0)
#     List = list(table.index)
#
#     a = Tree(List, table)
#     for leaf in a.leaList:
#         route = []
#         Tree.output(leaf, route)
#         #print(route)
#         print(Tree.routeToPara(route))




