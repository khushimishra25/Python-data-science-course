import pgzrun

HEIGHT=300
WIDTH=800

p=Actor('ironman')
c=Actor('cookie_img',(100,100))

def draw():
    screen.clear()      #screen.fill('white')   to change the color of the background
    p.draw()
    c.draw()

pgzrun.go()