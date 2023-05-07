# 存档确认
import sys
import pygame
import importlib
main = importlib.import_module("main")


def show_confirm_dialog():
    # 退出提示文本
    font = pygame.font.Font(None, 30)
    message = font.render("Do you want to save your progress?", True, (0, 0, 0))
    yes_button = font.render("Yes", True, (0, 0, 0))
    no_button = font.render("No", True, (0, 0, 0))

    message_rect = message.get_rect(center=(main.size[0] / 2, main.size[1] / 2 - 50))
    yes_rect = yes_button.get_rect(center=(main.size[0] / 2 - 100, main.size[1] / 2))
    no_rect = no_button.get_rect(center=(main.size[0] / 2 + 80, main.size[1] / 2))

    pygame.draw.rect(main.screen, (255, 255, 255), ((main.size[0] - 200) / 2 - 90, (main.size[1] - 120) / 2 - 50, 400, 200))
    pygame.draw.rect(main.screen, (0, 0, 255), yes_rect)
    pygame.draw.rect(main.screen, (0, 0, 255), no_rect)
    main.screen.blit(message, message_rect)
    main.screen.blit(yes_button, yes_rect)
    main.screen.blit(no_button, no_rect)

    pygame.display.update()

    while True:
        for event_exit in pygame.event.get():
            if event_exit.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event_exit.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # 点击yes时保存游戏退出
                if yes_rect.collidepoint(mouse_pos):
                    return True
                # 点击no不保存
                elif no_rect.collidepoint(mouse_pos):
                    main.screen.blit(pygame.transform.scale(main.surface_bg_image, main.size), main.imageRect)
                    pygame.display.update()
                    return False
