"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics
from campy.graphics.gobjects import GLabel
import random

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts
SCORES = 0  # scores
BUFF_MOVE = 3  # the velocity of buff drop
WIN_LABEL = GLabel('You win!')    # win label
LOSE_LABEL = GLabel('You lose!')  # lose label

live_label = GLabel(f'lives: {NUM_LIVES}')
score_label = GLabel(f'score: {SCORES}')


def main():
    graphics = BreakoutGraphics()
    live_label.font = '-30'
    score_label.font = '-30'
    graphics.window.add(live_label, x=0, y=live_label.height)
    graphics.window.add(score_label, x=0, y=graphics.window.height)
    lives = NUM_LIVES
    score = SCORES
    buff_lst = []

    # Add the animation loop here!
    while True:

        graphics.ball.move(graphics.dx, graphics.dy)
        graphics.hit_window()

        if graphics.corner() is not None:
            x, y, obj = graphics.corner()
            if obj != live_label:
                if obj == graphics.paddle:
                    graphics.hit_paddle(y)
                elif obj.height == graphics.brick_height and obj.width == graphics.brick_width:
                    graphics.hit_brick(obj, x, y)
                    score += 1
                    score_label.text = 'score: ' + str(score)
                    if random.random() < 0.5:
                        buff = graphics.get_buff()
                        if type(buff) == GLabel:
                            buff_lst.append(buff)
                            graphics.window.add(buff, x=obj.x, y=obj.y + buff.height)

        if graphics.ball.y + graphics.ball.height > graphics.window.height + graphics.ball.height * 2:
            lives -= 1
            live_label.text = 'lives: ' + str(lives)
            if lives > 0:
                graphics.reset_ball()
            else:
                graphics.window.add(LOSE_LABEL, x=(graphics.window.width-LOSE_LABEL.width)/2,
                                    y=(graphics.window.height+LOSE_LABEL.height)/2)
                break

        if score == graphics.brick_num:
            graphics.window.add(WIN_LABEL, x=(graphics.window.width - WIN_LABEL.width) / 2,
                                y=(graphics.window.height + WIN_LABEL.height)/2)
            break

        for buff in buff_lst:
            if buff.y > graphics.window.height + buff.height:
                continue
            buff.move(0, BUFF_MOVE)
            graphics.buff_hit_paddle(buff)

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
