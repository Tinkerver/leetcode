# class Solution:
#     def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
#         m = [[0 for i in range(n)] for i in range(n)]
#         for edge in graph:
#             m[edge[0]][edge[1]] = 1
#
#         visit = [0 for i in range(n)]
#         q = []
#         q.append(start)
#         visit[start] = 1
#         while len(q):
#             tmp = q.pop(0)
#             for node in range(n):
#                 if m[tmp][node]==1:
#                     if node == target:
#                         return True
#                     if visit[node] == 0:
#                         visit[node] = 1
#                         q.append(node)
#         return False
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        dic={}
        for edge in graph:
            dic = defaultdict(set)

            for key, value in graph:  # 用字典来构建邻接表
                dic[key].add(value)
            time.sleep(0.1)
            visit = [0 for i in range(n)]
            q = []
            q.append(start)
            visit[start] = 1
            while len(q):
                tmp = q.pop(0)
                for node in list(dic[tmp]):
                    if node == target:
                        return True
                    if visit[node] == 0:
                        visit[node] = 1
                        q.append(node)
            return False
