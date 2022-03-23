class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)-1):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(int(len(matrix)/2)):
             for j in range(len(matrix)):
                 matrix[i][j], matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1], matrix[i][j]