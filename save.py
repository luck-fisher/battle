# 存档确认
import importlib
from tkinter import messagebox

main = importlib.import_module("main")


# 退出确认
def show_confirm_dialog():
    result = messagebox.askokcancel(title="wargame", message="确认退出游戏？")
    return result
