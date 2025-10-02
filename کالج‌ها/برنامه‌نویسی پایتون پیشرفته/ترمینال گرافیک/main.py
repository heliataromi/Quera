import pygame

pygame.init()

size = [300, 300]
screen = pygame.display.set_mode(size)

white = (255, 255, 255)
black = (0, 0, 0)

screen.fill(white)

pen_color = black
pen_size = 1

running = True
while running:
    command_line = input()
    command_parts = command_line.split()
    command = command_parts[0]

    if command == 'change':
        if command_parts[1] == 'size':
            pen_size = int(command_parts[2])

        elif command_parts[1] == 'color':
            r = int(command_parts[2])
            g = int(command_parts[3])
            b = int(command_parts[4])
            pen_color = (r, g, b)

    elif command == 'draw':
        shape = command_parts[1]

        if shape == 'line':
            x1 = int(command_parts[2])
            y1 = int(command_parts[3])
            x2 = int(command_parts[4])
            y2 = int(command_parts[5])
            pygame.draw.line(screen, pen_color, (x1, y1), (x2, y2), pen_size)

        elif shape == 'circle':
            cx = int(command_parts[2])
            cy = int(command_parts[3])
            radius = int(command_parts[4])
            pygame.draw.circle(screen, pen_color, (cx, cy), radius, pen_size)

        elif shape == 'polygon':
            points = []
            for i in range(2, len(command_parts), 2):
                x = int(command_parts[i])
                y = int(command_parts[i+1])
                points.append((x, y))
            pygame.draw.polygon(screen, pen_color, points, pen_size)

        pygame.display.update()

    elif command == 'end' and command_parts[1] == 'drawing':
        pygame.image.save(screen, 'draw.png')
        running = False

pygame.quit()

