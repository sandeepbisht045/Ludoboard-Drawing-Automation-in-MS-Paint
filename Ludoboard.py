import pyautogui
import subprocess
import time
subprocess.Popen(r"C:\Windows\system32\mspaint.exe")
time.sleep(5)

def common_color():
    pyautogui.click(85,35)
    time.sleep(2)
    pyautogui.click(960,82)
    a=130
    pyautogui.moveTo(325,330)
    while(a>=0):
        pyautogui.drag(a,0)
        pyautogui.drag(0, a)
        pyautogui.drag(-a, 0)
        pyautogui.drag(0, -a)
        a=a-3
# -------------------------------------------------------------------------------
def color1():
    x=240
    y=43
    while(y>=0):
        pyautogui.drag(x,0)
        pyautogui.drag(0, y)
        pyautogui.drag(-x, 0)
        pyautogui.drag(0, -y)
        x=x-1
        y=y-1

def color2():
    x=43
    y=240
    while(x>=0):
        pyautogui.drag(x,0)
        pyautogui.drag(0, y)
        pyautogui.drag(-x, 0)
        pyautogui.drag(0, -y)
        x=x-1
        y=y-1
# ----------------------------------------------------------------------------------------
pyautogui.moveTo(85,90)
def box():
    fill=240
    while(fill>=0):

        pyautogui.drag(fill,0)
        pyautogui.drag(0,fill)


        pyautogui.drag(-fill,0)

        pyautogui.drag(0,-fill)
        fill = fill - 2
    # ---------------------------------------------------------------
def sq():
    def square():
        x=40
        # while(x>=0):
        pyautogui.drag(x,0)
        pyautogui.drag(0,x)
        pyautogui.drag(-x,0)
        pyautogui.drag(0,-x)
        # x=x-3
    square()
    pyautogui.move(70,0)
    square()
    pyautogui.move(0,70)
    square()
    pyautogui.move(-70,0)
    square()


# --------------------------------------------------------------------------------------------------------------------------------------
def tabla(Y,Z,W,V):
    rows = Y
    column = Z
    width = W
    height =V
    k = width / column

    # tells the current positon pf cursor which is stored in u,v
    u, v = pyautogui.position()
    a = 0
    # this while loop will create the rows required

    while (a < rows):

        pyautogui.drag(width, 0)
        pyautogui.drag(0, height)
        pyautogui.drag(-width, 0)
        pyautogui.drag(0, -height)
        x, y = pyautogui.position()
        pyautogui.moveTo(x, y + height)

        a = a + 1

    m = 0
    f = 0
    # this while loop will create the columns required
    while (m < column):
        pyautogui.moveTo(u + f, v)

        pyautogui.drag(0, (rows * height))
        f = f + k
        m = m + 1
        # --------------------------------------------------------------------------------------
pyautogui.click(83,35)
time.sleep(2)
pyautogui.leftClick(831, 60)
pyautogui.moveTo(85,90)
box()

pyautogui.moveTo(85,330)
color1()
pyautogui.moveTo(325,90)
color2()
pyautogui.move(43,0)
color2()

pyautogui.click(83,35)
time.sleep(2)
pyautogui.click(937,60)

pyautogui.moveTo(455,90)
box()
pyautogui.moveTo(411,90)
color2()
pyautogui.moveTo(455,330)
color1()
pyautogui.move(0,43)
color1()

pyautogui.click(83,35)
time.sleep(2)
pyautogui.click(893, 62)
pyautogui.moveTo(455,460)
box()

pyautogui.moveTo(455,416)
color1()
pyautogui.moveTo(411,460)
color2()
pyautogui.move(-43,0)
color2()

pyautogui.click(83,35)
time.sleep(2)
pyautogui.click(872, 61)
pyautogui.moveTo(85,460)
box()

pyautogui.moveTo(325,460)
color2()
pyautogui.move(-240,-43)
color1()
pyautogui.move(0,-43)
color1()
# ----------------------------------------------------------
common_color()
# --------------------------------------------------------------------
pyautogui.click(83,35)
time.sleep(2)
pyautogui.click(762,59)

pyautogui.moveTo(85,460)
pyautogui.drag(0,-130)
pyautogui.drag(610,0)
pyautogui.drag(0,370)
pyautogui.drag(-370,0)
pyautogui.drag(0,-610)
tabla(6,3,130,40)
pyautogui.moveTo(325,460)
tabla(6,3,130,40)
pyautogui.moveTo(85,330)
tabla(3,6,240,43.333)
pyautogui.moveTo(455,330)
tabla(3,6,240,43.333)
# ------------------------------------------------------------------------------------
pyautogui.moveTo(455,330)
pyautogui.drag(-130,130)
pyautogui.moveTo(325,330)
pyautogui.drag(130,130)
# ------------------------------------------------------------


pyautogui.move(60,60)
sq()
pyautogui.moveTo(85,460)
pyautogui.move(60,60)
sq()


pyautogui.moveTo(85,90)
pyautogui.move(60,60)
sq()


pyautogui.moveTo(455,90)
pyautogui.move(60,60)
sq()

pyautogui.moveTo(85,90)
pyautogui.drag(610,0)
pyautogui.drag(0,610)
pyautogui.drag(-610,0)
pyautogui.drag(0,-610)
# ----------------------------------------------------
def start_point(x,y):
    pyautogui.drag(x,y)
    pyautogui.move(-x,0)
    pyautogui.drag(x,-y)

pyautogui.moveTo(325,620)
start_point(43,40)
pyautogui.moveTo(165,416)
start_point(40,43)
pyautogui.moveTo(125,330)
start_point(40,43)
pyautogui.moveTo(325,170)
start_point(43,40)
pyautogui.moveTo(411,130)
start_point(43,40)
pyautogui.moveTo(575,330)
start_point(40,43)
pyautogui.moveTo(615,416)
start_point(40,43)
pyautogui.moveTo(411,580)
start_point(43,40)
