import pgzrun

WIDTH = 1000
HEIGHT = 500

scr=0

def gamescr(bgcolor,title,info):
    screen.fill(bgcolor)
    screen.draw.text(title,center=(WIDTH/2, HEIGHT/2), fontsize=100, color='white', align='center')
    screen.draw.text(info,center=(WIDTH/2, HEIGHT/2+100), fontsize=50, color='white', align='center')

def draw():
    if scr==0:
        gamescr('black','Amazing game','Press space to start')
        #screen.blit("hearts",(0,0))      for background
    elif scr==1:
        gamescr('green','Game is running','Press esc to end')
    elif scr==2:
        gamescr('red','Game Over','Press space to restart')
        

def update():
    global scr
    if keyboard.space and scr==0:
        scr=1
    if keyboard.escape and scr==1 :
        scr=2
    if keyboard.space and scr==2:
        scr=0


pgzrun.go()