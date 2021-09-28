import pygame
from plane_sprites import GameSprite

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1>  加载图像数据
bg = pygame.image.load("./images/background.png")
# 2>  blit 绘制图像
screen.blit(bg, (0, 0))
# 3>  update 更新显示
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 300))
# 3>  update 更新显示
pygame.display.update()
# 创建始终对象
clock = pygame.time.Clock()
# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 300, 102, 126)

# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy)

# 游戏循环->意味着游戏的正式开始
while True:
    # 可以制定循环体内部的代码的执行频率
    clock.tick(60)
    # 监听事件
    for event in pygame.event.get():
        # 判断事件类型是是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")
            # quit卸载所有的模块
            pygame.quit()
            # exit() 直接终止当前正在执行的程序
            exit()
    # 2. 修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= 0:
        hero_rect.y = 700
    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update
    enemy_group.update()
    # draw
    enemy_group.draw(screen)
    # 4.调用update方法更新显示
    pygame.display.update()
