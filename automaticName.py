import pyautogui as pg
import time
time.sleep(2)

def paintOpen():
    pg.hotkey('win', 's')
    pg.write('paint')
    time.sleep(1)
    pg.hotkey('enter')
    time.sleep(1)

def wordT():
    pg.dragRel(100, 0)
    pg.dragRel(0, 20)
    pg.dragRel(-40, 0)
    pg.dragRel(0, 100)
    pg.dragRel(-20, 0)
    pg.dragRel(0, -100)
    pg.dragRel(-40, 0)
    pg.dragRel(0, -20)
    global t
    t = pg.position()

def wordA():
    pg.click(pg.moveRel(120, 0))
    pg.dragRel(20, 0)
    pg.dragRel(40, 120)
    pg.dragRel(-20, 0)
    pg.dragRel(-20, -60)
    pg.dragRel(-20, 0)
    pg.dragRel(-20, 60)
    pg.dragRel(-20, 0)
    pg.dragRel(40, -120)

    pg.click(pg.moveRel(5, 20))
    pg.dragRel(10, 0)
    pg.dragRel(5, 20)
    pg.dragRel(-20, 0)
    pg.dragRel(5, -20)
    global a
    a = pg.position()

def wordN():
    pg.click(pg.moveRel(60, -20))
    pg.dragRel(0, 120)
    pg.dragRel(20, 0)
    pg.dragRel(0, -100)
    pg.dragRel(40, 100)
    pg.dragRel(40, 0)
    pg.dragRel(0, -120)
    pg.dragRel(-20, 0)
    pg.dragRel(0, 100)
    pg.dragRel(-40, -100)
    pg.dragRel(-40, 0)
    global n
    n = pg.position()

def wordU():
    pg.click(pg.moveRel(110, 0))
    pg.dragRel(0, 120)
    pg.dragRel(80, 0)
    pg.dragRel(0, -120)
    pg.dragRel(-20, 0)
    pg.dragRel(0, 100)
    pg.dragRel(-40, 0)
    pg.dragRel(0, -100)
    pg.dragRel(-20, 0)
    global u
    u = pg.position()

def wordJ():
    pg.click(pg.moveRel(120, 0))
    pg.dragRel(40, 0)
    pg.dragRel(0, 20)
    pg.dragRel(-10, 0)
    pg.dragRel(0, 80)
    pg.dragRel(-20, 20)
    pg.dragRel(-20, 0)
    pg.dragRel(-20, -20)
    pg.dragRel(0, -20)
    pg.dragRel(20, 0)
    pg.dragRel(0, 10)
    pg.dragRel(5, 10)
    pg.dragRel(10, 0)
    pg.dragRel(5, -10)
    pg.dragRel(0, -70)
    pg.dragRel(-10, 0)
    pg.dragRel(0, -20)
    global j
    j = pg.position()

def outline():
    paintOpen()
    pg.alert(title = 'position', text = 'move the cursor on a empty position, from where you want to start the process')
    global start
    start = pg.position()
    pg.click(pg.moveTo(start))   # move to the start point
    pg.hotkey('ctrl', 'a')
    pg.hotkey('del')
    pg.alert(title = 'writing brush', text = 'move the cursor on writing brush or pen')
    global brush
    brush = pg.position()
    pg.click(pg.moveTo(brush))   # writing brush
    pg.alert(title = 'black colour', text = 'move the cursor on black colour')
    global black
    black = pg.position()
    pg.click(pg.moveTo(black))   # black color
    pg.click(pg.moveTo(start))   # move to the start point
    wordT()
    wordA()
    wordN()
    wordU()
    wordJ()

def coloring():
    # paint brush
    pg.alert(title = 'painting brush', text = 'move the cursor on painting brush')
    global paint
    paint = pg.position()
    pg.click(pg.moveTo(paint))
    # gray color
    pg.alert(title = 'gray colour', text = 'move the cursor on gray colour')
    global gray
    gray = pg.position()
    pg.click(pg.moveTo(gray))

    pg.click(pg.moveTo(t[0]+51, t[1]+12))   # T k andr
    pg.click(pg.moveTo(a[0]+6, a[1]-9))   # A k andr
    pg.click(pg.moveTo(n[0]+20, n[1]+10))   # N k andr
    pg.click(pg.moveTo(u[0]+10, u[1]+10))    # U k andr
    pg.click(pg.moveTo(j[0]+20, j[1]+10))    # J k andr
    
    # blue color
    pg.alert(title = 'blue colour', text = 'move the cursor on blue colour')
    global blue
    blue = pg.position()
    pg.click(pg.moveTo(blue))

    pg.click(pg.moveTo(start[0]-10, start[1]-15))   # move just before the start point
    pg.click(pg.moveTo(a[0]+6, a[1]+10))   # A k small k andr
    dltmsg = pg.confirm(text='do you want to delete this whole', title='', buttons=['Yes', 'No'])
    if(dltmsg.title() == 'Yes'):
        pg.click(pg.moveTo(start[0]-10, start[1]-15))
        pg.hotkey('ctrl', 'a')
        pg.hotkey('del')
    
    pg.click(pg.moveTo(brush))   # writing brush
    pg.click(pg.moveTo(black))   # black colour

    pg.alert(title = 'close paint', text = 'move the cursor on close icon, situated at upper right corner(red color)')
    global close
    close = pg.position()
    
    closemsg  = pg.confirm(text='do you want to close the paint', title='', buttons=['Yes', 'No'])
    if(closemsg.title() == 'Yes'):
        pg.click(pg.moveTo(close))   # close the window
        global dSave
        dSave = pg.alert(title = '', text = "move the cursor on Don't Save")
        dSave = pg.position()
        pg.click(pg.moveTo(dSave))   # Don't save

def tanuj():
    pg.alert(title = 'Always Remembered in future', text = "Don't use cursor to click 'OK', plz only press the enter \n Move the cursor only when I told you")
    time.sleep(2)
    outline()
    coloring()

tanuj()
