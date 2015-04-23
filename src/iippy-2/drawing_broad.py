#模仿Chaonet的代码






import simplegui
import math

# 定义各种变量，全局和局部变量

WIDTH = 800
HEIGHT = 600
canvas_color = "Black"
pos = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 7
Polygons = "Round"





# 通过canvas_color预备画板颜色，以便事件调用（一堆handler）；
#声明全局变量，并更改
# def red():
#canvas_color ="Red" (是错误声明，只声明了局部变量，作用域只在def 语块而已，)


def red():
    global canvas_color
    canvas_color = "Red"

def yellow():
    global canvas_color
    canvas_color = "Yellow"

def green():
    global canvas_color
    canvas_color = "Green"

def blue():
    global canvas_color
    canvas_color = "Blue"

def black():
    global canvas_color
    canvas_color = "Black"


# 鼠标点击事件，先声明全局变量，再修改为局部变量



def mouse_click(pos):
    global pos 
    pos = list(pos)


#预备多种形状，以便事件调用


def Triangular():
    global Polygons
    Polygons = "Triangular"

def Square():
    global Polygons
    Polygons = "Square"

def Round():
    global Polygons
    Polygons = "Round"
# Handler to draw on canvas
#列条件不同条件下画哪钟图像; 官方视频教程没有加列if elif 和else条件，单使用 canvas.draw_polygon(), canvas.draw_circle()

def draw(canvas):
    if Polygons == "Triangular": #三角形，三条边
        canvas.draw_polygon([(pos[0], pos[1]-25), (pos[0]-25, pos[1]+25), (pos[0]+25,pos[1]+25)], 
                                             5, 
                                             "White", canvas_color
                                             )

    elif Polygons == "Square":#四边形，四条边
        canvas.draw_polygon([(pos[0]-25, pos[1]-25), (pos[0]-25, pos[1]+25), (pos[0]+25, pos[1]+25), (pos[0]+25, pos[1]-25)], 
                                             5, 
                                             "White", canvas_color
                                             )

    elif Polygons == "Round":
        canvas.draw_circle(pos, BALL_RADIUS, 
                                        1, 
                                        "White", canvas_color
                                        )

# 设置框架对应生成按钮，并回调事件

frame = simplegui.create_frame("Home", 800, 600)
frame.set_canvas_background('White')
frame.add_button('Triangular', Triangular, 80)
frame.add_button('Square', Square, 80)
frame.add_button('Round', Round, 80)
frame.add_button("Red", red, 60)
frame.add_button("Yellow", yellow, 60)
frame.add_button("Green", green, 60)
frame.add_button("Blue", blue, 60)
frame.add_button("Black", black, 60)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_click)
# Start the frame animation

frame.start()

