import pgzrun

HEIGHT=600
WIDTH=1200

p=Actor('ironman',center=(WIDTH//2,HEIGHT//2))

title="IRON-MAN GAME"

def draw():
    screen.fill('white')
    screen.draw.text(title,(10,10),fontsize=30,color='black',center=(WIDTH//2,30),align='center',shadow=(1,1),scolor="red")
    p.draw()

def p_move():
    '''fuction to move player'''
    if keyboard.left:
        p.x-=3
        p.angle=-10
    elif keyboard.right:
        p.x+=3
        p.angle=-10
    elif keyboard.up:
        p.y-=3
    elif keyboard.down:
        p.y+=3
    else:
        p.angle=0

def handle_boundary():
    if p.x>WIDTH:
        p.x=0
    if p.x<0:
        p.x=WIDTH
    if p.y>HEIGHT:
        p.y=0
    if p.y<0:
        p.y=HEIGHT

    

def update():
    p_move()
    print(p.x,p.y,p.angle)

pgzrun.go()