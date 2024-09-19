# -*- coding:utf-8 -*-
import sys  # 导入sys模块
import pygame  # 导入pygame模块
import btn  # 导入自定义按钮模块

pygame.init()  # 初始化pygame
size = width, height = 320, 240  # 设置窗口
# 定义颜色
WHITE = (255, 255, 255)
BLUE = (72, 61, 139)

screen = pygame.display.set_mode(size)  # 显示窗口
# 设置背景颜色
screen.fill(WHITE)
# 执行死循环，确保窗口一直显示
while True:
    # 创建识别按钮
    button1 = btn.Button(screen, (90, 50), 140, 60, BLUE, WHITE, "关闭窗口", 20)
    # 绘制创建的按钮
    button1.draw_button()
    # 更新窗口
    pygame.display.update()
    # 检查事件
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()  # 退出pygame
            sys.exit()
        # 判断点击
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标点击位置
            if 20 <= event.pos[0] and event.pos[0] <= 90 + 70 \
                    and 20 <= event.pos[1] and event.pos[1] <= 50 + 30:
                pygame.quit()  # 退出pygame
                sys.exit()     # 系统退出
                pass