import random
import os

# 初始化游戏面板
def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

# 在随机空位上添加新砖块
def add_new_tile(board):
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        board[i][j] = 2 if random.random() < 0.9 else 4

# 打印游戏面板
def print_board(board):
    os.system('clear' if os.name == 'posix' else 'cls')
    for row in board:
        print("\t".join(str(num) if num != 0 else "." for num in row))
    print()

# 检查是否游戏结束
def is_game_over(board):
    if any(0 in row for row in board):
        return False
    for i in range(4):
        for j in range(4):
            if (i < 3 and board[i][j] == board[i + 1][j]) or (j < 3 and board[i][j] == board[i][j + 1]):
                return False
    return True

# 移动并合并砖块
def move(board, direction):
    if direction == 'w':
        for j in range(4):
            col = [board[i][j] for i in range(4) if board[i][j] != 0]
            new_col = merge(col)
            for i in range(4):
                board[i][j] = new_col[i] if i < len(new_col) else 0

    elif direction == 's':
        for j in range(4):
            col = [board[i][j] for i in range(4) if board[i][j] != 0][::-1]
            new_col = merge(col)
            for i in range(4):
                board[i][j] = new_col[::-1][i] if i < len(new_col) else 0

    elif direction == 'a':
        for i in range(4):
            row = [num for num in board[i] if num != 0]
            new_row = merge(row)
            board[i] = new_row + [0] * (4 - len(new_row))

    elif direction == 'd':
        for i in range(4):
            row = [num for num in board[i] if num != 0][::-1]
            new_row = merge(row)
            board[i] = new_row[::-1] + [0] * (4 - len(new_row))

# 合并砖块
def merge(line):
    if not line:
        return []
    new_line = []
    skip = False
    for i in range(len(line)):
        if skip:
            skip = False
            continue
        if i + 1 < len(line) and line[i] == line[i + 1]:
            new_line.append(line[i] * 2)
            skip = True
        else:
            new_line.append(line[i])
    return new_line

# 主函数
def main():
    board = initialize_board()
    while True:
        print_board(board)
        if is_game_over(board):
            print("游戏结束！")
            break
        move_direction = input("请输入移动方向 (w/a/s/d)：")
        if move_direction in ['w', 'a', 's', 'd']:
            previous_board = [row[:] for row in board]
            move(board, move_direction)
            if previous_board != board:  # 检查是否有移动
                add_new_tile(board)

if __name__ == "__main__":
    main()
