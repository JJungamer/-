import pygame
import random

# 초기화
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
BLUE = (100, 150, 255)
GREEN = (0, 200, 0)

# 새 (플레이어)
bird = pygame.Rect(100, 250, 30, 30)
bird_vel = 0
gravity = 0.5
jump_strength = -10

# 파이프
pipes = []
pipe_width = 60
pipe_gap = 150
pipe_timer = 0
score = 0
font = pygame.font.SysFont(None, 36)

# 게임 루프
running = True
while running:
    clock.tick(60)
    screen.fill(BLUE)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            bird_vel = jump_strength

    # 중력 적용
    bird_vel += gravity
    bird.y += int(bird_vel)

    # 바닥, 천장 충돌
    if bird.top < 0 or bird.bottom > HEIGHT:
        running = False

    # 파이프 생성
    pipe_timer += 1
    if pipe_timer > 90:
        pipe_timer = 0
        top_height = random.randint(50, HEIGHT - pipe_gap - 50)
        bottom_height = HEIGHT - top_height - pipe_gap
        pipes.append(pygame.Rect(WIDTH, 0, pipe_width, top_height))
        pipes.append(pygame.Rect(WIDTH, HEIGHT - bottom_height, pipe_width, bottom_height))

    # 파이프 이동 및 충돌 체크
    for pipe in pipes[:]:
        pipe.x -= 5
        if pipe.right < 0:
            pipes.remove(pipe)
            score += 0.5  # 상하 2개니까 0.5점씩

        if bird.colliderect(pipe):
            running = False

        pygame.draw.rect(screen, GREEN, pipe)

    # 새 그리기
    pygame.draw.ellipse(screen, WHITE, bird)

    # 점수 출력
    text = font.render(f"Score: {int(score)}", True, WHITE)
    screen.blit(text, (10, 10))

    # 업데이트
    pygame.display.flip()

pygame.quit()