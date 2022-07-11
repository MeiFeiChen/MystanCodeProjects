"""
File: my_drawing.py
Name:Mei-Fei Chen
----------------------
To draw a rowlet.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
label = GLabel('？？？？')


def main():
    """
    Title: 我是誰???? 木木梟
    雖然自從改叫寶可夢之後就再也沒看過寶可夢了, 但被網路上木木梟的圖片被萌到, 根本是萌系神奇寶貝!
    """
    background = GRect(window.width, window.height)
    background.filled = True
    background.fill_color = 'skyblue'
    window.add(background)
    label.font = '-40'
    window.add(label, x=(window.width - label.width) / 2, y=70)
    black_rowlet()
    onmouseclicked(rowlet)


def black_rowlet():
    foot('black')
    upper_body('black')
    head(140, 130, 'black')
    head(225, 130, 'black')
    eyes(175, 175, 'black')
    eyes(275, 175, 'black')
    spark(186, 190, 'black')
    spark(286, 190, 'black')
    mouse('black', 'black')
    lower_body('black')
    wing('black')
    neck('black', 'black')


def rowlet(event):
    global label
    window.remove(label)
    label_rowlet = GLabel('木木梟')
    label_rowlet.font = '-40'
    window.add(label_rowlet, x=(window.width-label_rowlet.width)/2, y=70)
    foot('sandybrown')
    upper_body('bisque')
    head(140, 130, 'ivory')
    head(225, 130, 'ivory')
    eyes(175, 175, 'dimgrey')
    eyes(275, 175, 'dimgrey')
    spark(186, 190, 'floralwhite')
    spark(286, 190, 'floralwhite')
    mouse('sandybrown', 'oldlace')
    lower_body('floralwhite')
    wing('bisque')
    neck('mediumaquamarine', 'darksage')


def upper_body(color):
    oval = GOval(275, 295, x=(window.width-275)/2, y=(window.height-295)/2)
    oval.filled = True
    oval.fill_color = color
    oval.color = color
    window.add(oval)


def head(x, y, color):
    face = GOval(120, 130, x=x, y=y)
    face.filled = True
    face.fill_color = color
    face.color = color
    window.add(face)


def eyes(x, y, color):
    eye = GOval(30, 45, x=x, y=y)
    eye.filled = True
    eye.fill_color = color
    eye.color = color
    window.add(eye)


def spark(x, y, color):
    sp = GOval(7, 13, x=x, y=y)
    sp.filled = True
    sp.fill_color = color
    sp.color = color
    window.add(sp)


def mouse(backcolor, color):
    back = GOval(40, 80, x=221, y=157)
    back.filled = True
    back.fill_color = backcolor
    back.color = backcolor
    upper = GArc(42, 100, -20, 220, x=220, y=157)
    upper.filled = True
    upper.fill_color = color
    upper.color = color
    lower = GOval(40, 40, x=221, y=183)
    lower.filled = True
    lower.fill_color = color
    lower.color = color
    window.add(back)
    window.add(upper)
    window.add(lower)


def neck(color, veincolor):
    left = GPolygon()
    left.add_vertex((201, 273))
    left.add_vertex((175, 290))
    left.add_vertex((201, 307))
    left.filled = True
    left.fill_color = color
    left.color = color
    left_ball = GOval(60, 44, x=191, y=268)
    left_ball.filled = True
    left_ball.fill_color = color
    left_ball.color = color
    left_vein = GRect(20, 3, x=221, y=290)
    left_vein.filled = True
    left_vein.fill_color = veincolor
    left_vein.color = veincolor
    right_ball = GOval(60, 44, x=242, y=268)
    right_ball.filled = True
    right_ball.fill_color = color
    right_ball.color = color
    right = GPolygon()
    right.add_vertex((292, 273))
    right.add_vertex((318, 290))
    right.add_vertex((292, 307))
    right.filled = True
    right.fill_color = color
    right.color = color
    right_vein = GRect(20, 3, x=251, y=290)
    right_vein.filled = True
    right_vein.fill_color = veincolor
    right_vein.color = veincolor
    window.add(left)
    window.add(right)
    window.add(left_ball)
    window.add(right_ball)
    window.add(left_vein)
    window.add(right_vein)


def lower_body(color):
    upper = GArc(130, 80, 0, 180, x=184, y=300)
    upper.filled = True
    upper.fill_color = color
    upper.color = color
    left = GOval(118, 105, x=168, y=298)
    left.filled = True
    left.fill_color = color
    left.color = color
    right = GOval(118, 105, x=218, y=298)
    right.filled = True
    right.fill_color = color
    right.color = color
    window.add(left)
    window.add(right)
    window.add(upper)


def wing(color):
    left = GArc(35, 230, 175, 180, x=174, y=220)
    left.filled = True
    left.fill_color = color
    left.color = color
    left2 = GArc(38, 280, 175, 180, x=150, y=220)
    left2.filled = True
    left2.fill_color = color
    left2.color = color
    right = GArc(35, 230, 175, 180, x=290, y=220)
    right.filled = True
    right.fill_color = color
    right.color = color
    right2 = GArc(38, 280, 175, 180, x=314, y=220)
    right2.filled = True
    right2.fill_color = color
    right2.color = color
    window.add(left2)
    window.add(left)
    window.add(right)
    window.add(right2)


def foot(color):
    # 左腳
    left = GPolygon()
    left.add_vertex((240, 380))
    left.add_vertex((270, 390))
    left.add_vertex((230, 415))
    left.add_vertex((190, 410))
    left.filled = True
    left.fill_color = color
    left.color = color
    # 左1指甲
    left_nail1 = GArc(60, 35, 40, 180, x=185, y=400)
    left_nail1.filled = True
    left_nail1.fill_color = color
    left_nail1.color = color
    # 左2指甲
    left_nail2 = GArc(40, 50, 34, 180, x=206, y=400)
    left_nail2.filled = True
    left_nail2.fill_color = color
    left_nail2.color = color
    # 右腳
    right = GPolygon()
    right.add_vertex((window.width-240, 380))
    right.add_vertex((window.width-270, 390))
    right.add_vertex((window.width-230, 415))
    right.add_vertex((window.width-190, 410))
    right.filled = True
    right.fill_color = color
    right.color = color
    # 右1指甲
    right_nail1 = GArc(60, 35, -40, 180, x=window.width-185-55, y=400)
    right_nail1.filled = True
    right_nail1.fill_color = color
    right_nail1.color = color
    # 右2指甲
    right_nail2 = GArc(40, 50, -34, 180, x=window.width-206-36, y=400)
    right_nail2.filled = True
    right_nail2.fill_color = color
    right_nail2.color = color

    window.add(left_nail1)
    window.add(left_nail2)
    window.add(right_nail1)
    window.add(right_nail2)
    window.add(left)
    window.add(right)


if __name__ == '__main__':
    main()
