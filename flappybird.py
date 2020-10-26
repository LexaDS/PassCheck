import pygame
import random
import sys

def floor_loop():
    screen.blit(floor_surface,(floor_motion,900))
    screen.blit(floor_surface,(floor_motion+576,900))

def create_new_pipe():
    random_pipe_placement=random.choice(pipe_height)
    new_pipe_top=pipes.get_rect(midbottom=(700,random_pipe_placement-300))
    new_pipe_bottom=pipes.get_rect(midtop=(700,random_pipe_placement))
    return new_pipe_bottom, new_pipe_top

def pipe_movement(pipes):
    for pipe in pipes:
        pipe.centerx-=5
    return pipes

def build_pipes(pipe_l):
    for pipe in pipe_l:
        if pipe.bottom>=1024:
            screen.blit(pipes,pipe)
        else:
            fliped_pipe=pygame.transform.flip(pipes,False,True)
            screen.blit(fliped_pipe,pipe)

def check_collisions(pipe_l):
    for pipe in pipe_l:
        if bird1_rect.colliderect(pipe):
            game_over_sound.play()
            return False
    if bird1_rect.top <=-100 or bird1_rect.bottom >= 900:
        return False

    return True

def rotate_bird(bird):
    new_bird1=pygame.transform.rotozoom(bird,-bird_animation * 3,1)
    return new_bird1

def animated_bird():
    new_bird=bird1_frames[bird_index]
    new_bird_rect=new_bird.get_rect(center=(100,bird1_rect.centery))
    return new_bird,new_bird_rect

def score_screen(game_status):
    if game_status=='main_game':
        score_surf=game_font.render(str(int(score)),True,(255,255,255))
        score_rect=score_surf.get_rect(center=(288,100))
        screen.blit(score_surf,score_rect)
    if game_status=='game_over':
        score_surf = game_font.render('Score:{}'.format(str(int(score))), True, (255, 255, 255))
        score_rect = score_surf.get_rect(center=(288, 100))
        screen.blit(score_surf, score_rect)

        high_score_surf = game_font.render('High score:{}'.format(str(int(high_score))), True, (255, 255, 255))
        high_score_rect = high_score_surf.get_rect(center=(288, 850))
        screen.blit(high_score_surf, high_score_rect)

def update_score(score,high_score):
    if score > high_score:
        high_score = score
    return high_score

pygame.mixer.pre_init(frequency=44100,size=-16,channels=2,buffer=512)
pygame.init()

screen = pygame.display.set_mode((576,1024))
clock=pygame.time.Clock()
game_font=pygame.font.SysFont('dejavuserif.ttf',40)


#game variables

gravity=0.25
bird_animation=0
game_on=True
score=0
high_score=0

backgroung_surface=pygame.image.load('/home/lexa/Desktop/flappyimg/background-day.png').convert()
backgroung_surface=pygame.transform.scale2x(backgroung_surface)
floor_surface=pygame.image.load('/home/lexa/Desktop/flappyimg/base.png').convert()
floor_surface=pygame.transform.scale2x(floor_surface)
floor_motion=0

#bird

bird1_down=pygame.transform.scale2x(pygame.image.load('/home/lexa/Desktop/flappyimg/bluebird-downflap.png'))
bird1_mid=pygame.transform.scale2x(pygame.image.load('/home/lexa/Desktop/flappyimg/bluebird-midflap.png'))
bird1_up=pygame.transform.scale2x(pygame.image.load('/home/lexa/Desktop/flappyimg/bluebird-upflap.png'))
bird1_frames=[bird1_down,bird1_mid,bird1_up]
bird_index=0
bird1=bird1_frames[bird_index]
bird1_rect=bird1.get_rect(center = (100,512))

BIRDFLAP=pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP,200)


pipes=pygame.image.load('/home/lexa/Desktop/flappyimg/pipe-green.png').convert()
pipes=pygame.transform.scale2x(pipes)
pipe_list=[]
SPAWNPIPES=pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPES,1200)
pipe_height=[400,600,800]

game_over=pygame.image.load('/home/lexa/Desktop/flappyimg/message.png').convert_alpha()
game_over=pygame.transform.scale2x(game_over)
game_over_rect=game_over.get_rect(center=(288,512))

#sounds
flap_sound=pygame.mixer.Sound('/home/lexa/Desktop/flappysounds/soundEffects/sfx_wing.wav')
game_over_sound=pygame.mixer.Sound('/home/lexa/Desktop/flappysounds/soundEffects/sfx_hit.wav')
score_sound=pygame.mixer.Sound('/home/lexa/Desktop/flappysounds/soundEffects/sfx_point.wav')
score_sound_contdown=100

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_on:
                bird_animation=0
                bird_animation-=12
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_on == False:
                game_on= True
                pipe_list.clear()
                bird1_rect.center=(100,512)
                bird_animation=0
                score=0

        if event.type==SPAWNPIPES:
            pipe_list.extend(create_new_pipe())

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index+=1
            else:
                bird_index = 0
            bird1,bird1_rect = animated_bird()

    screen.blit(backgroung_surface,(0,0))
    floor_motion-=1
    floor_loop()
    if floor_motion<=-576:
        floor_motion=0
    screen.blit(floor_surface,(floor_motion,900))

    if game_on:
        bird_animation+=gravity
        rotated_bird=rotate_bird(bird1)
        bird1_rect.centery+=bird_animation
        screen.blit(rotated_bird,bird1_rect)
        game_on=check_collisions(pipe_list)

        pipe_list=pipe_movement(pipe_list)
        build_pipes(pipe_list)

        score+=0.01
        score_screen('main_game')
        score_sound_contdown -=1
        if score_sound_contdown<=0:
            score_sound.play()
            score_sound_contdown=100
    else:
        screen.blit(game_over,game_over_rect)
        high_score=update_score(score,high_score)
        score_screen('game_over')

    pygame.display.update()
    clock.tick(120)


