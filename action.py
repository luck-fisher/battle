import sys
import map
import pygame
from pygame import transform, surface
import importlib

main = importlib.import_module("main")

# 敌人数量
enemies_num = [(2, 1, 0), (4, 1, 0), (5, 2, 1), (6, 3, 2)]

# 技能字典
skill_dict = {
    "技能1": "鹰眼",
    "技能2": "龙血强化",
    "技能3": "铁山靠"
}

# 技能是否解锁
skill_unlock = {
    "技能1": False,
    "技能2": False,
    "技能3": False
}

# 技能冷却回合,存储格式为当前冷却回合和技能释放冷却的集合
skill_cooldown = {
    "技能1": [0, 1],
    "技能2": [0, 2],
    "技能3": [0, 4]
}

# 当前关卡
current_level = 0

# 最大敌人数量
enemies_num_max = [0]


# 开始游戏
def start_game():
    # 切换到游戏背景
    game_image = transform.scale(pygame.image.load("image/game_bg1.jpg"), main.size)
    main.screen.blit(game_image, game_image.get_rect())
    pygame.display.update()

    # 绘制返回按钮
    exit_game_bottom = surface.Surface((200, 50), pygame.SRCALPHA)
    exit_game_font = pygame.font.Font(None, 50).render("return title", True, (255, 255, 255))
    exit_game_bottom.blit(exit_game_font, exit_game_font.get_rect())
    exit_game_bottom_rect = exit_game_bottom.get_rect()
    exit_game_bottom_rect.center = (main.size[0] - 100, main.size[1] - 50)
    main.screen.blit(exit_game_bottom, exit_game_bottom_rect)

    # 棋盘
    chessboard = map.chess_board
    # 棋盘所带标记
    # 0 - 普通格子，1- 角色当前位置，2-敌人1标记，3-敌人2 ,4-敌人3 ，5- 技能拾取点，6-障碍物so on
    chessboard_mark = map.chess_board_mark_list[current_level]

    # 绘制棋盘
    map.drawBoard(chessboard, chessboard_mark)

    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 点击返回按钮时返回主界面
                if exit_game_bottom_rect.collidepoint(event.pos):
                    return True
            # 键盘按压事件
            if event.type == pygame.KEYDOWN:
                # 棋子移动事件
                if event.key == pygame.K_LEFT:
                    player_move(pygame.K_LEFT, chessboard, chessboard_mark)
                if event.key == pygame.K_RIGHT:
                    player_move(pygame.K_RIGHT, chessboard, chessboard_mark)
                if event.key == pygame.K_UP:
                    player_move(pygame.K_UP, chessboard, chessboard_mark)
                if event.key == pygame.K_DOWN:
                    player_move(pygame.K_DOWN, chessboard, chessboard_mark)
                if event.key == pygame.K_a:
                    player_move(pygame.K_LEFT, chessboard, chessboard_mark)
                if event.key == pygame.K_s:
                    player_move(pygame.K_DOWN, chessboard, chessboard_mark)
                if event.key == pygame.K_d:
                    player_move(pygame.K_RIGHT, chessboard, chessboard_mark)
                if event.key == pygame.K_w:
                    player_move(pygame.K_UP, chessboard, chessboard_mark)
                # 技能释放事件
                if event.key == pygame.K_q:
                    pass
                if event.key == pygame.K_e:
                    pass

        pygame.display.update()


# 角色移动
def player_move(direction, chessboard, chessboard_mark):
    # 当玩家按左键时，改变玩家位置
    if direction == pygame.K_LEFT:
        if map.player_place[0] - 1 >= 0 and \
                chessboard_mark[map.player_place[0] - 1][map.player_place[1]] == 0:
            map.player_place = (map.player_place[0] - 1, map.player_place[1])
            # TODO: move enemies
            map.drawBoard(chessboard, chessboard_mark)
    # 当玩家按右键时，改变玩家位置
    if direction == pygame.K_RIGHT:
        if map.player_place[0] + 1 <= len(chessboard) - 1 \
                and chessboard_mark[map.player_place[0] + 1][map.player_place[1]] == 0:
            map.player_place = (map.player_place[0] + 1, map.player_place[1])
            # TODO: move enemies
            map.drawBoard(chessboard, chessboard_mark)
    # 当玩家按上键时，改变玩家位置
    if direction == pygame.K_UP:
        if map.player_place[1] - 1 >= 0 and \
                chessboard_mark[map.player_place[0]][map.player_place[1] - 1] == 0:
            map.player_place = (map.player_place[0], map.player_place[1] - 1)
            # TODO: move enemies
            map.drawBoard(chessboard, chessboard_mark)
    # 当玩家按下键时，改变玩家
    if direction == pygame.K_DOWN:
        if map.player_place[1] + 1 <= len(chessboard[0]) - 1 \
                and chessboard_mark[map.player_place[0]][map.player_place[1] + 1] == 0:
            map.player_place = (map.player_place[0], map.player_place[1] + 1)
            # TODO: move enemies
            map.drawBoard(chessboard, chessboard_mark)


# 敌人移动
def enemies_move(chessboard, chessboard_mark):
    pass