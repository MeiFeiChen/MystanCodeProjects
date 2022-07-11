"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 5  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 2  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball
FRAME_RATE = 1000 / 120  # 120 frames per second
PADDLE_BUFF = 5


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout2'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle = GRect(self.paddle_width, self.paddle_height)
        self.paddle_offset = paddle_offset
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2,
                        y=window_height - self.paddle_offset - self.paddle.height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.reset_ball()

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.start_click)
        onmousemoved(self.paddle_position)

        # Draw bricks
        brick_y = brick_offset
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_num = brick_rows * brick_cols

        for row in range(brick_rows):
            brick_x = 0
            for col in range(brick_cols):
                brick = GRect(brick_width, brick_height, x=brick_x, y=brick_y)
                brick.filled = True
                if row < brick_rows / 5:
                    brick.fill_color = 'Red'
                    brick.color = 'Red'
                elif row < brick_rows / 5 * 2:
                    brick.fill_color = 'Orange'
                    brick.color = 'Orange'
                elif row < brick_rows / 5 * 3:
                    brick.fill_color = 'Yellow'
                    brick.color = 'Yellow'
                elif row < brick_rows / 5 * 4:
                    brick.fill_color = 'Green'
                    brick.color = 'Green'
                else:
                    brick.fill_color = 'Blue'
                    brick.color = 'Blue'
                self.window.add(brick)

                brick_x += (brick_spacing + brick_width)
            brick_y += brick_spacing + brick_height

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy

    def hit_window(self):
        """
        Updates dx and dy depending on whether or not the ball hit the wall.
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def corner(self):
        """
        :return: whether or not object in the four corners of the ball is None.
        if object in all of the corners are None, return None.
        if object in any corner is not None, return the x,y of the corner and the object.
        """
        corner = [[x, y] for x in [self.ball.x + self.ball.width, self.ball.x]
                  for y in [self.ball.y, self.ball.y + self.ball.height]]
        for x, y in corner:
            obj = self.window.get_object_at(x, y)
            if obj is not None:
                return x, y, obj

    def hit_paddle(self, y):
        """
        updates dy if the ball hits the paddle.
        """
        if y == self.ball.y + self.ball.height:
            self.__dy = -abs(self.__dy)

    def hit_brick(self, obj, x, y):
        """
        Updates dx and dy depending on whether or not the ball hit the brick and then remove the brick.
        :param obj: brick
        :param x: ball.x
        :param y: ball.y
        """
        if (x == self.ball.x and obj.x + obj.width - abs(self.__dx) < x <= obj.x + obj.width) or \
                (x == self.ball.x + self.ball.width and obj.x <= x < obj.x + abs(self.__dx)):
            self.__dx = -self.__dx
        if (y == self.ball.y and obj.y + obj.height - abs(self.__dy) < y <= obj.y + obj.height) or \
                (y == self.ball.y + self.ball.height and obj.y <= y < obj.y + abs(self.__dy)):
            self.__dy = -self.__dy
        self.window.remove(obj)

    @staticmethod
    def get_buff():
        paddle_lengthen = GLabel('<-->')
        paddle_lengthen.font = '-20'
        paddle_shorten = GLabel('-><-')
        paddle_shorten.font = '-20'
        buff = [paddle_lengthen, paddle_shorten]
        return random.choice(buff)

    def buff_hit_paddle(self, buff):
        """
        if buff hit the paddle, shorten or lengthen the paddle.
        """
        buff_corner = [[x, buff.y] for x in [buff.x, buff.x + buff.width]]
        for x, y in buff_corner:
            obj = self.window.get_object_at(x, y)
            if obj == self.paddle:  # if the buff hit the paddle
                buff.y += self.window.height - self.paddle.height   # to make the buff out of the window
                new_x = self.paddle.x   # new_paddle_x
                new_y = self.paddle.y   # new_paddle_y
                self.window.remove(self.paddle)
                if buff.text == '<-->':     # lengthen the paddle
                    self.paddle_width += PADDLE_BUFF
                    new_x -= PADDLE_BUFF / 2
                elif buff.text == '-><-':   # shorten the paddle
                    self.paddle_width -= PADDLE_BUFF
                    new_x += PADDLE_BUFF / 2
                self.paddle = GRect(self.paddle_width, self.paddle_height, x=new_x, y=new_y)
                self.paddle.filled = True
                self.window.add(self.paddle)
                break

    def reset_ball(self):
        """
        sets the ball fixed in the original position.
        """
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        self.__dx = 0
        self.__dy = 0

    def start_click(self, event):
        """
        sets ball velocity after clicked.
        sets ball x velocity to random negative or positive number.
        sets ball y velocity to random positive number.
        :param event: mouse clicked event
        """
        if 0 <= event.x < self.window.width and 0 <= event.y < self.window.height:
            if self.__dy == 0:
                self.__dx = random.randint(1, MAX_X_SPEED)
                self.__dy = INITIAL_Y_SPEED
                if random.random() > 0.5:
                    self.__dx = -self.__dx

    def paddle_position(self, event):
        """
        sets the paddle position in the middle of the mouse.
        :param event: mouse moved event
        """
        if event.x >= self.window.width - self.paddle.width / 2:
            paddle_x = self.window.width - self.paddle.width
        elif event.x <= self.paddle.width / 2:
            paddle_x = 0
        else:
            paddle_x = event.x - self.paddle.width / 2
        self.window.add(self.paddle, x=paddle_x, y=self.window.height - self.paddle_offset)
