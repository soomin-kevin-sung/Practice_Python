def solution(wallpaper):
    max_x, max_y, min_x, min_y = 0, 0, 50, 50
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                max_x = max(i, max_x)
                max_y = max(j, max_y)
                min_x = min(i, min_x)
                min_y = min(j, min_y)
                print(min_x, min_y, max_x, max_y)
                
    answer = [min_x, min_y, max_x + 1, max_y + 1]
                
    return answer