import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("test window")
screen.fill((255, 255, 255))
pygame.display.update()

size = 1
color = (0, 0, 0)


while True:
    pygame.event.pump()
    inp = input().split()

    if inp[0] == 'change':
        if inp[1] == 'size':
            size = int(inp[2])
        if inp[1] == 'color':
            color = tuple(map(int, inp[2:]))

    if inp[0] == 'draw':
        if inp[1] == 'line':
            pygame.draw.line(screen, color, tuple(map(int, inp[2:4])), tuple(map(int, inp[4:6])), size)
        if inp[1] == 'circle':
            pygame.draw.circle(screen, color, tuple(map(int, inp[2:4])), int(inp[4]), size)
        if inp[1] == 'polygon':
            lst = []
            tup = []
            for i in range(len(inp[2:])):
                tup.append(int(inp[2:][i]))
                if i % 2 != 0:
                    lst.append(tuple(tup))
                    tup.clear()
            pygame.draw.polygon(screen, color, lst, size)

    pygame.display.update()

    if inp[0] == 'end' and inp[1] == 'drawing':
        pygame.image.save(screen, 'draw.png')
        pygame.quit()
        exit()
