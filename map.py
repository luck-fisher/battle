import pygame

import main

# 角色当前位置
player_place = (0, 0)

# 棋盘
chess_board = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for i in range(16):
    for j in range(9):
        chess_board[i].append((i * 80, j * 80, 80, 80))

# 第一关棋盘的标记
chess_board1_mark = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for i in range(16):
    for j in range(9):
        if 5 <= i <= 10 and 3 <= j <= 9:
            chess_board1_mark[i].append(0)
        else:
            chess_board1_mark[i].append(6)
        if i == 8 and j == 8:
            player_place = (i, j)

# 第二关棋盘的标记
chess_board2_mark = []
for i in range(16):
    for j in range(8):
        chess_board2_mark.append(0)

# 第三关棋盘的标记
chess_board3_mark = []
for i in range(16):
    for j in range(9):
        chess_board3_mark.append(0)

# 第四关棋盘的标记
chess_board4_mark = []
for i in range(16):
    for j in range(9):
        chess_board4_mark.append(0)

# 棋盘标记集合
chess_board_mark_list = [chess_board1_mark, chess_board2_mark, chess_board3_mark, chess_board4_mark]


# 绘制棋盘
def drawBoard(chessboard, chessboard_mark):
    # 刻画棋盘
    for a in range(len(chessboard)):
        for b in range(len(chessboard[a])):
            # 普通地块
            if chessboard_mark[a][b] == 0:
                pygame.draw.rect(main.screen, (192, 192, 192), chessboard[a][b], 0)
            # 障碍物
            elif chessboard_mark[a][b] == 6:
                pygame.draw.rect(main.screen, (34, 139, 34), chessboard[a][b], 0)
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
            if player_place == (a, b):
                protagonist_image = pygame.transform.scale(pygame.image.load("image/spare_protagonist2.jpg"), (80, 80))
                main.screen.blit(protagonist_image, chessboard[a][b])
    # 更新
    pygame.display.update()
