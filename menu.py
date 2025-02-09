import pygame

from settings import *


class MenuOption (pygame.font.Font):
    def __init__(self, text, function, position=(0, 0), font=None, font_size=40, font_color=WHITE):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.function = function
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, True, font_color)
        self.rect = self.label.get_rect(center=position)
        self.position = position
        self.is_selected = False

    def set_position(self, x, y):
        self.position = (x, y)
        self.rect = self.label.get_rect(center=self.position)

    def highlight(self, color=YELLOW):
        self.font_color = color
        self.label = self.render(self.text, True, self.font_color)
        self.is_selected = True

    def unhighlight(self):
        self.font_color = WHITE
        self.label = self.render(self.text, True, self.font_color)
        self.is_selected = False

    def check_for_mouse_selection(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.highlight()
        else:
            self.unhighlight()


def draw_gradient_background(screen, colors, width, height):
    for i in range(height):
        color = [
            colors[0][c] + (colors[1][c] - colors[0][c]) * i // height
            for c in range(3)
        ]
        pygame.draw.line(screen, color, (0, i), (width, i))


class Menu:
    def __init__(self, screen, functions):
        self.is_active = True
        self.screen = screen
        self.scr_width, self.scr_height = self.screen.get_size()
        self.options = []
        self.current_option = None
        self.functions = functions

        for index, option in enumerate(functions.keys()):
            menu_option = MenuOption(option, functions[option])
            width, height = menu_option.rect.size
            total_height = len(functions) * height
            pos_x = self.scr_width // 2
            pos_y = (self.scr_height // 2 - total_height // 2) + index * (height + 20)
            menu_option.set_position(pos_x, pos_y)
            self.options.append(menu_option)

    def draw(self):
        draw_gradient_background(self.screen, [(255, 0, 0), (0, 0, 255)], self.scr_width, self.scr_height)

        for option in self.options:
            option.check_for_mouse_selection(pygame.mouse.get_pos())
            if self.current_option is not None:
                self.options[self.current_option].highlight()

            shadow_offset = 3
            shadow_color = (50, 50, 50)
            shadow_label = option.render(option.text, True, shadow_color)
            shadow_rect = shadow_label.get_rect(center=option.position)
            self.screen.blit(shadow_label, (shadow_rect.x + shadow_offset, shadow_rect.y + shadow_offset))

            self.screen.blit(option.label, option.rect)

            if option.is_selected:
                pygame.draw.rect(self.screen, YELLOW, option.rect.inflate(20, 10), 2, border_radius=8)
