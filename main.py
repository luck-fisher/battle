import sys
import pygame
from pygame import surface, transform
import importlib
save = importlib.import_module("save")
action = importlib.import_module("action")


pygame.init()

# 设置主屏幕尺寸
size = (1550, 800)

# 创建主屏幕
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
# 设置窗口标题
pygame.display.set_caption("wargame")
# 设置标题文本
text_title = pygame.font.Font(None, 120).render("wargame", True, (0, 0, 0))
textRect_title = text_title.get_rect()
textRect_title.center = (size[0] / 2, size[1] * (1 / 3))

# 开始按钮
bottom_start = surface.Surface((300, 60), pygame.SRCALPHA)
bottom_start_rect = bottom_start.get_rect()
bottom_start_rect.center = (size[0] / 2, size[1] / 2)
# 设置开始按钮的文本
text_sle1 = pygame.font.Font(None, 60).render("start game", True, (0, 0, 0))
textRect_sle1 = text_title.get_rect()
# 将文字导入到bottom上
bottom_start.blit(text_sle1, textRect_sle1)

# 继续游戏按钮
bottom_continue = surface.Surface((300, 60), pygame.SRCALPHA)
bottom_continue_rect = bottom_start.get_rect()
bottom_continue_rect.center = (size[0] / 2, size[1] / 2 + 100)
# 设置继续按钮文本
text_sle2 = pygame.font.Font(None, 60).render("continue game", True, (0, 0, 0))
textRect_sle2 = text_title.get_rect()
# 文字导入
bottom_continue.blit(text_sle2, textRect_sle2)

# 退出游戏按钮
bottom_exit = surface.Surface((300, 60), pygame.SRCALPHA)
bottom_exit_rect = bottom_start.get_rect()
bottom_exit_rect.center = (size[0] / 2, size[1] / 2 + 200)
# 退出游戏文本
text_sle3 = pygame.font.Font(None, 60).render("exit", True, (0, 0, 0))
textRect_sle3 = text_title.get_rect()
# 文字导入
bottom_exit.blit(text_sle3, textRect_sle3)

# 创建主界面背景
surface_bg_image = transform.scale(pygame.image.load("image/bg1.jpg"), size)
imageRect = surface_bg_image.get_rect()

# 获取时钟对象
clock = pygame.time.Clock()

# 设置主界面文字
surface_bg_image.blit(text_title, textRect_title)
surface_bg_image.blit(bottom_start, bottom_start_rect)
surface_bg_image.blit(bottom_continue, bottom_continue_rect)
surface_bg_image.blit(bottom_exit, bottom_exit_rect)

# 将主界面写入屏幕
screen.blit(surface_bg_image, imageRect)

# 程序主循环
while True:
    # 设置FPS为60
    clock.tick(60)

    # 获取事件
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            if save.show_confirm_dialog():
                pygame.quit()
                sys.exit()
        # 键盘按压事件
        if event.type == pygame.KEYDOWN:
            pass
        # 鼠标事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 当鼠标点击开始按钮时进入关卡
            if bottom_start_rect.collidepoint(event.pos):
                flag = action.start_game()
                if flag:
                    screen.blit(surface_bg_image, imageRect)
            # 当鼠标点击继续按钮时从文件中读取上次的存档
            if bottom_continue_rect.collidepoint(event.pos):
                pass
            # 当鼠标点击bottom_exit时退出游戏
            if bottom_exit_rect.collidepoint(event.pos):
                if save.show_confirm_dialog():
                    pygame.quit()
                    sys.exit()

    pygame.display.update()
