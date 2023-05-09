import pygame
import role
import main


# 敌人数量
enemies_num = [(2, 1, 0), (4, 1, 0), (5, 2, 1), (6, 3, 2)]

# 角色出生点
player_birth = (8, 8)

# 当前关卡
current_level = 0

# 初始化角色
player = role.Player(5, 1, 100, 1)
player.place = player_birth

# 地块字典
block_dict = {
    "普通地块": 0,
    "下层地块": 1,
    "角色出生点": 2,
    "障碍物": 6
}


# 棋盘
chess_board = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for i in range(16):
    for j in range(9):
        chess_board[i].append((i * 80, j * 80, 79, 79))

# 第一关棋盘的标记
chess_board1_mark = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for i in range(16):
    for j in range(9):
        if 5 <= i <= 10 and 3 <= j <= 9:
            chess_board1_mark[i].append(block_dict.get("普通地块"))
        else:
            chess_board1_mark[i].append(block_dict.get("障碍物"))
        if (i == 6 and j == 7) or (i == 6 and j == 6) or (i == 6 and j == 5):
            chess_board1_mark[i][j] = 6
        if (i == 8 and j == 5) or (i == 8 and j == 3) or (i == 9 and j == 6):
            chess_board1_mark[i][j] = block_dict.get("障碍物")
        # 特殊地块额外标记
        if i == 10 and j == 3:
            chess_board1_mark[i][j] = block_dict.get("下层地块")

# 第二关棋盘的标记
chess_board2_mark = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for i in range(16):
    for j in range(9):
        if 3 <= i <= 12:
            chess_board2_mark[i].append(block_dict.get("普通地块"))
        else:
            chess_board2_mark[i].append(block_dict.get("障碍物"))
        if (i == 3 and j == 3) or (i == 5 and j == 3) or (i == 6 and j == 3):
            chess_board2_mark[i][j] = block_dict.get("障碍物")
        if (i == 6 and j == 2) or (i == 6 and j == 1) or (7 <= i <= 10 and j == 1):
            chess_board2_mark[i][j] = block_dict.get("障碍物")
        if (i == 6 and 5 <= j <= 7) or (i == 7 and j == 5) or (10 <= i <= 11 and 3 <= j <= 7):
            chess_board2_mark[i][j] = block_dict.get("障碍物")
        # 特殊地块额外标记
        if i == 5 and j == 2:
            chess_board2_mark[i][j] = block_dict.get("下层地块")

# 第三关棋盘的标记
chess_board3_mark = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for i in range(16):
    for j in range(9):
        if 0 <= i <= 2:
            chess_board3_mark[i].append(block_dict.get("障碍物"))
        else:
            chess_board3_mark[i].append(block_dict.get("普通地块"))
        if (i == 8 and j == 4) or (i == 9 and j == 5) or (i == 10 and j == 6) or (i == 11 and j == 7) or (
                3 <= i <= 4 and j == 6) or (6 <= i <= 7 and (0 <= j <= 2 or 4 <= j <= 8)):
            chess_board3_mark[i][j] = block_dict.get("障碍物")
        if (9 <= i <= 13 and j == 2) or (i == 13 and 3 <= j <= 7) or (i == 11 and 3 <= j <= 4) or (
                i == 4 and 2 <= j <= 3):
            chess_board3_mark[i][j] = block_dict.get("障碍物")
        # 特殊地块额外标记
        if i == 5 and j == 8:
            chess_board3_mark[i][j] = block_dict.get("下层地块")

# 第四关棋盘的标记
chess_board4_mark = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for i in range(16):
    for j in range(9):
        chess_board4_mark[i].append(block_dict.get("普通地块"))
        if (3 <= i <= 7 and j == 5) or (i == 7 and 6 <= j <= 7) or (8 <= i <= 9 and j == 7) or (i == 9 and 2 <= j <= 7):
            chess_board4_mark[i][j] = block_dict.get("障碍物")
        if (i == 0 and j == 8) or (i == 1 and j == 7) or (10 <= i <= 12 and j == 2) or (7 >= i >= 2 == j) or (
                4 <= i <= 6 and j == 3):
            chess_board4_mark[i][j] = block_dict.get("障碍物")
        if (i == 13 and (3 <= j <= 5 or 7 <= j <= 8)) or (i == 11 and 4 <= j <= 8) or (i == 15 and 3 <= j <= 7):
            chess_board4_mark[i][j] = block_dict.get("障碍物")
        if (i == 13 and j == 0) or (i == 14 and j == 1) or (i == 1 and j == 3) or (i == 3 and j == 0) or (
                i == 5 and j == 1) or (i == 7 and j == 0) or (i == 9 and j == 1) or (i == 11 and j == 0):
            chess_board4_mark[i][j] = block_dict.get("障碍物")
        # 特殊地块额外标记
        if i == 8 and j == 6:
            chess_board4_mark[i][j] = block_dict.get("下层地块")

# 棋盘标记集合
chess_board_mark_list = [chess_board1_mark, chess_board2_mark, chess_board3_mark, chess_board4_mark]

# 当前关卡棋盘所带标记
chessboard_mark = chess_board_mark_list[current_level]


# 绘制棋盘
def drawBoard():
    # 刻画棋盘
    for a in range(len(chess_board)):
        for b in range(len(chess_board[a])):
            # 普通地块
            if chessboard_mark[a][b] == block_dict.get("普通地块"):
                pygame.draw.rect(main.screen, (192, 192, 192), chess_board[a][b], 0)
            # 入口
            elif chessboard_mark[a][b] == block_dict.get("下层地块"):
                enter_image = pygame.transform.scale(pygame.image.load("image/enter.jpeg"), (80, 80))
                main.screen.blit(enter_image, chess_board[a][b])
            # 障碍物
            elif chessboard_mark[a][b] == block_dict.get("障碍物"):
                pygame.draw.rect(main.screen, (34, 139, 34), chess_board[a][b], 0)
            # 敌人一位置
            elif chessboard_mark[a] == 2:
                pass
            # 敌人二位置
            elif chessboard_mark[a] == 3:
                pass
            # 敌人三位置
            elif chessboard_mark[a] == 4:
                pass
            # 角色位置
            if player.place == (a, b):
                protagonist_image = pygame.transform.scale(pygame.image.load("image/spare_protagonist2.jpg"), (80, 80))
                main.screen.blit(protagonist_image, chess_board[a][b])


# 切换棋盘
def change_chessboard():
    # 更换当前棋盘
    global current_level
    current_level += 1
    global chessboard_mark
    chessboard_mark = chess_board_mark_list[current_level]
    # 角色重置回出生点
    global player
    player.place = player_birth
    drawBoard()
