from ball import *
from player import *

class Gameworld:
    def __init__(self):
        self.balls = []
        self.player = Player()
        self.initialize_balls()
        self.game_over = False

    def initialize_balls(self):
        # hardcoded initial balls
        self.balls.append(Ball(100, 200, 3, (2, -3), RIGHT))
        self.balls.append(Ball(300, 150, 2, (-2, 2), LEFT))

    def check_for_collisions(self):
        for ball_index, ball in enumerate(self.balls):
            ball_rect = ball.image.get_rect(left=ball.x, top=ball.y)
            weapon_rect = self.player.weapon.image.get_rect(left=self.player.weapon.x, top=self.player.weapon.y)
            player_rect = self.player.image.get_rect(left=self.player.x, top=self.player.y)
            # if ball_rect.colliderect(player_rect):
            #     self.player.lives -= 1
            #     # if self.player.lives:
            #     #     self.load_level(self.level)
            #     # else:
            #     if self.player.lives == 0:
            #         self.game_over = True
            if ball_rect.colliderect(player_rect) and not self.player.invincible:
                self.player.lives -= 1
                self.player.invincible = True
                self.player.invincible_timer = 60
                print("Lost a life.")

                if self.player.lives == 0:
                    self.game_over = True

            if ball_rect.colliderect(weapon_rect) and self.player.weapon.is_active:
                self.player.weapon.is_active = False
                self.split_ball(ball_index)
                return

    def split_ball(self, ball_index):
        ball = self.balls[ball_index]

        if ball.size == 2:
            del self.balls[ball_index]
        else:
            self.balls.append(Ball(ball.x - 25, ball.y - 10, ball.size - 1, (1, -5), LEFT))
            self.balls.append(Ball(ball.x + 25, ball.y - 10, ball.size - 1, (-1, -5), RIGHT))
            del self.balls[ball_index]

    def update(self):
        for ball in self.balls:
            ball.update()
        # if self.player.weapon.is_active:
        self.check_for_collisions()
        self.player.update()
