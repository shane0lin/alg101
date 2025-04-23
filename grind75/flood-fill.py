# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.
def floodFill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def isValid(x, y):
        return 0 <= x < len(image) and 0 <= y < len(image[0])
    
    que = [(sr, sc)]
    original_color = image[sr][sc]
    image[sr][sc] = color
    while que:
        x, y = que.pop(0)
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if isValid(new_x, new_y) and image[new_x][new_y] == original_color:
                que.append((new_x, new_y))
                image[new_x][new_y] = color
                
    return image