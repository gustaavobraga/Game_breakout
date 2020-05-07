import sys, pygame,random

def collision(ball, bar, bar_targets, speed_ball, direc_ball):
    #x
    if (ball.x + 20) >= 650:
        direc_ball[0] = -speed_ball[0]
    elif ball.x <= 0:
        direc_ball[0] = speed_ball[0]
    #y
    if ball.y <= 0:
        direc_ball[1] = speed_ball[1]
    elif ball.colliderect(bar) == 1:
        if ((ball.x + 15) >= bar.x) and (ball.x < bar.x + 75):
            direc_ball[1] = -speed_ball[1]
            direc_ball[0] = -speed_ball[0]
        else:
            direc_ball[1] = -speed_ball[1]
            direc_ball[0] = speed_ball[0]
    elif (ball.y + 20) >= 600:
        return 10

    for x, line in enumerate(bar_targets):
        for i, targets in enumerate(bar_targets[line]):
            if ball.colliderect(targets) == 1:
                if ball.y <= (targets.y + 15) and direc_ball[1] == -speed_ball[1]:
                    direc_ball[1] = speed_ball[1]
                    bar_targets[line].pop(i)
                    return x
                elif (ball.y + 20) >= targets.y and direc_ball[1] == speed_ball[1]:
                    direc_ball[1] = -speed_ball[1]
                    bar_targets[line].pop(i)
                    return x


def to_move(ball, speed_ball):
    ball.move_ip(speed_ball)

def target(bar_targets):
    top = 65
    width = [50, 50, 45, 45, 44, 40, 40, 36, 37, 35, 35, 30, 30, 28, 28, 25, 20]

    keys = ['targets_red', 'targets_yellow', 'targets_green']
    for xx in range(0,3):
        width = random.sample(width, 17)

        for i in range(0,17):
            one_width = width[i]
            if i == 0:
                bar_targets[keys[xx]].append(pygame.Rect(0, top, one_width, 20))
            else:
                x = (bar_targets[keys[xx]][-1].x + bar_targets[keys[xx]][-1].width) + 2
                bar_targets[keys[xx]].append(pygame.Rect(x, top, one_width, 20))
        top += 22

def text(answer, color, score, cor_text, spped_ball):
    line = cor_text
    position = 0
    if answer == 0:
        score += 15
        line = color['targets'][answer]
        spped_ball[0] += 1.5
        spped_ball[1] += 1.5
    elif answer == 1:
        score += 10
        line = color['targets'][answer]
        spped_ball[0] += 1
        spped_ball[1] += 1
    elif answer == 2:
        score += 5
        line = color['targets'][answer]
        spped_ball[0] += 0.5
        spped_ball[1] += 0.5

    if score >= 10 and score < 100:
        position = (585, 8)
    elif score >= 100:
        position = (565, 8)
    else:
        position = (610, 8)


    return [score, line, position]

#main
def main():
    pygame.init()

    size = (650, 600)
    color = {'background': (40, 42, 54), 'ball': (248, 248, 242), 'bar': (139, 233, 253),
             'targets': [(255, 85, 85), (241, 250, 140), (80, 250, 123)]}
    bar_targets = {'targets_red': [], 'targets_yellow': [], 'targets_green': []}
    speed_ball = [2.5, 2.5]
    direc_ball = [-2.5, -2.5]
    score = 0
    cor_text = (80, 250, 123)


    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Breakout')
    ball = pygame.Rect(630,580, 20, 20)
    bar = pygame.Rect(0, 570, 150, 10)
    font = pygame.font.SysFont(None, 80)


    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    target(bar_targets)


    # loop
    while True:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[0] <= 500:
            bar.x = pygame.mouse.get_pos()[0]
            pygame.mouse.set_visible(False)

        screen.fill(color['background'])

        to_move(ball, direc_ball)
        answer = collision(ball, bar, bar_targets, speed_ball, direc_ball)
        if answer == 10:
            break
        else:
            x1 = text(answer, color, score, cor_text, speed_ball)
            score = x1[0]
            cor_text = x1[1]
            position = x1[2]

            text1 = font.render(str(score), True, cor_text)
            screen.blit(text1, position)


        pygame.draw.ellipse(screen, color['ball'], ball)
        pygame.draw.rect(screen, color['bar'], bar)


        for i, line in enumerate(bar_targets):
            for targets in bar_targets[line]:
                pygame.draw.rect(screen, color['targets'][i], targets)

        pygame.display.flip()


if __name__ == '__main__':
    while True:
        main()
