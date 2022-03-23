def floodFill(image, sr: int, sc: int, newColor: int):
    list = []
    lenx = len(image)
    leny = len(image[0])
    color = image[sr][sc]
    if color == newColor:
        return image
    list.append((sr, sc))
    while len(list) > 0:
        point = list[0]
        if point[0] > 0:
            if image[point[0] - 1][point[1]] == color:
                list.append((point[0] - 1, point[1]))
        if point[1] > 0:
            if image[point[0]][point[1] - 1] == color:
                list.append((point[0], point[1] - 1))
        if point[0] < lenx - 1:
            if image[point[0] + 1][point[1]] == color:
                list.append((point[0] + 1, point[1]))
        if point[1] < leny - 1:
            if image[point[0]][point[1] + 1] == color:
                list.append((point[0], point[1] + 1))
        image[point[0]][point[1]] = newColor
        list.pop(0)
    return image


floodFill(image=[[0, 0, 0], [0, 1, 1]], sr=1, sc=1, newColor=1)
