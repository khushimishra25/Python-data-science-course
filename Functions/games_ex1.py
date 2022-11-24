import pgzrun

HEIGHT=300
WIDTH=800

p=Actor('ironman')
c=Actor('cookie_img',(100,100))

def draw():
    screen.clear()      #screen.fill('white')   to change the color of the background
    p.draw()
    c.draw()
    #print('drawing')

def update():
    #print('updating')
    p.x+=1
    p.angle=-10
    if p.x>WIDTH:       #if p.x<0: agar player left side se bahar jaye to
        p.x=0           p.x=WIDTH
    print(p.x,p.y)

pgzrun.go()