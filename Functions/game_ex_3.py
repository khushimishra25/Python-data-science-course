import pgzrun
from random import randint

HEIGHT=600
WIDTH=1200

p=Actor('ironman',center=(WIDTH//2,HEIGHT//2))
c=Actor('cookie_img',(randint(0,WIDTH),randint(0,HEIGHT)))

title="IRON-MAN GAME"
score=0
#music.play()

def draw():
    screen.fill('white')
    screen.draw.text(title,(10,10),fontsize=30,color='black',center=(WIDTH//2,30),align='center',shadow=(1,1),scolor="pink")
    screen.draw.text(f'score:{score}',(10,10),fontsize=40,color='black')
    p.draw()
    c.draw()


def p_move():
    if keyboard.right and p.right < WIDTH:
        p.x+=10         # for speed
        p.angle=-90
    if keyboard.left and p.left > 0:
        p.x-=10
        p.angle=90
    if keyboard.up and p.top > 0:
        p.y-=10
        p.angle=0
    if keyboard.down and p.bottom < HEIGHT:
        p.y+=10
        p.angle=0
def update():
    global score # tells pyhton that we want to change the value of the global variable score
    p_move()
    if p.colliderect(c):
        score+=1
        c.pos=(randint(0,WIDTH),randint(0,HEIGHT))
        sounds.s1.play()
    print(p.x,p.y,p.angle)

pgzrun.go()