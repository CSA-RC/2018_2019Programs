# Jacob Meadows
# Computer Programming, 6th Period
# 15 December 2018
"""
First-OpenGL-Project.py

My first PyGame project.

Copyright (C) 2018 Jacob Meadows

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import os
import pygame
import OpenGL.GL as GL
import OpenGL.GLU as GLU
import OpenGL.GLUT as GLUT
import numpy
import time
import string


class App:
    def __init__(self):
        pygame.init()
        pygame.display.init()
        pygame.mixer.init()
        pygame.font.init()

        os.environ["SDL_VIDEO_WINDOW_POS"] = "100, 100"
        pygame.display.set_caption("Diablo: The RPG")
        self.screen = pygame.display.set_mode((1280, 720), pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.key.set_repeat(500, 20)
        self.clock = pygame.time.Clock()

        self.screen_objects = {
            "Texts": dict(),
            "TextInputs": dict(),
            "Buttons": dict()
        }
        self.screen_rectangles = list()
        self.world_objects = dict()
        self.system_variables = dict()

        self.main_menu()
        self.optional_init()

        delta_x = 0
        delta_y = 0
        delta_z = 0
        rotation_x = 0
        rotation_y = 0

        while True:
            keys = pygame.key.get_pressed()
            mods = pygame.key.get_mods()
            mouse_pos = pygame.mouse.get_pos()

            screen_objects = dict()
            for object_name, screen_object in [
                *self.screen_objects["Buttons"].items(), *self.screen_objects["TextInputs"].items()
            ]:
                if screen_object.active_state:
                    screen_objects.update({object_name: screen_object})

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not pygame.event.get_grab() and self.world_objects != dict():
                        pygame.mouse.set_visible(False)
                        pygame.event.set_grab(True)
                    for button in self.screen_objects["Buttons"].values():
                        if button.active_state:
                            if button.focus_state:
                                button.activate(button)
                                break
                    for text_input in self.screen_objects["TextInputs"].values():
                        if text_input.active_state:
                            if text_input.rect.collidepoint(*event.pos):
                                text_input.focus_state = True
                            else:
                                text_input.focus_state = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB and not mods & pygame.KMOD_LSHIFT:
                        if screen_objects:
                            if True not in [screen_object.focus_state for screen_object in screen_objects.values()]:
                                [screen_object for screen_object in screen_objects.values() if screen_object.rect.y ==
                                 min([screen_object.rect.y for screen_object in screen_objects.values()]) and
                                 screen_object.rect.x ==
                                 min([screen_object.rect.x for screen_object in screen_objects.values()
                                      if screen_object.rect.y ==
                                      min([screen_object.rect.y for screen_object in screen_objects.values()])])
                                 ][0] \
                                    .focus_state = True
                            elif True in [screen_object.focus_state for screen_object in screen_objects.values()]:
                                focused_object = [screen_object for screen_object in screen_objects.values()
                                                  if screen_object.focus_state][0]
                                lower_objects = [screen_object for screen_object in screen_objects.values()
                                                 if screen_object.rect.y > focused_object.rect.y]
                                next_lower_object = [lower_object for lower_object in lower_objects
                                                     if lower_object.rect.y ==
                                                     min([lower_object.rect.y for lower_object in lower_objects])]
                                side_objects = [screen_object for screen_object in screen_objects.values()
                                                if screen_object.rect.y == focused_object.rect.y
                                                and screen_object.rect.x > focused_object.rect.x
                                                and screen_object != focused_object]
                                next_side_object = [side_object for side_object in side_objects
                                                    if side_object.rect.x ==
                                                    min([side_object.rect.x for side_object in side_objects])]
                                new_object = next_side_object[0] if next_side_object else [
                                    next_lower_object[0] if next_lower_object
                                    else [screen_object for screen_object in screen_objects.values()
                                          if screen_object.rect.y ==
                                          min([screen_object.rect.y for screen_object in screen_objects.values()]) and
                                          screen_object.rect.x ==
                                          min([screen_object.rect.x for screen_object in screen_objects.values()
                                               if screen_object.rect.y ==
                                               min([screen_object.rect.y for screen_object
                                                    in screen_objects.values()])])
                                          ][0]][0]
                                new_object.focus_state = True
                                focused_object.focus_state = False
                    elif event.key == pygame.K_TAB and mods & pygame.KMOD_LSHIFT:
                        if screen_objects:
                            if True not in [screen_object.focus_state for screen_object in screen_objects.values()]:
                                [screen_object for screen_object in screen_objects.values() if screen_object.rect.y ==
                                 max([screen_object.rect.y for screen_object in screen_objects.values()]) and
                                 screen_object.rect.x ==
                                 max([screen_object.rect.x for screen_object in screen_objects.values()
                                      if screen_object.rect.y ==
                                      max([screen_object.rect.y for screen_object in screen_objects.values()])])
                                 ][0] \
                                    .focus_state = True
                            elif True in [screen_object.focus_state for screen_object in screen_objects.values()]:
                                focused_object = [screen_object for screen_object in screen_objects.values()
                                                  if screen_object.focus_state][0]
                                higher_objects = [screen_object for screen_object in screen_objects.values()
                                                  if screen_object.rect.y < focused_object.rect.y]
                                next_higher_object = [lower_object for lower_object in higher_objects
                                                      if lower_object.rect.y ==
                                                      max([lower_object.rect.y for lower_object in higher_objects])]
                                side_objects = [screen_object for screen_object in screen_objects.values()
                                                if screen_object.rect.y == focused_object.rect.y
                                                and screen_object.rect.x < focused_object.rect.x
                                                and screen_object != focused_object]
                                next_side_object = [side_object for side_object in side_objects
                                                    if side_object.rect.x ==
                                                    max([side_object.rect.x for side_object in side_objects])]
                                new_object = next_side_object[0] if next_side_object else [
                                    next_higher_object[0] if next_higher_object
                                    else [screen_object for screen_object in screen_objects.values()
                                          if screen_object.rect.y ==
                                          max([screen_object.rect.y for screen_object in screen_objects.values()]) and
                                          screen_object.rect.x ==
                                          max([screen_object.rect.x for screen_object in screen_objects.values()
                                               if screen_object.rect.y ==
                                               max([screen_object.rect.y for screen_object
                                                    in screen_objects.values()])])
                                          ][0]][0]
                                new_object.focus_state = True
                                focused_object.focus_state = False
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        for button in self.screen_objects["Buttons"].values():
                            if button.active_state:
                                if button.focus_state:
                                    button.activate(button)
                                    break
                    elif event.key == pygame.K_ESCAPE:
                        pygame.mouse.set_visible(True)
                        pygame.event.set_grab(False)
                    for text_input in self.screen_objects["TextInputs"].values():
                        if text_input.active_state:
                            text_input.input(event, mods)
                elif event.type == pygame.MOUSEMOTION:
                    for button in self.screen_objects["Buttons"].values():
                        if button.active_state:
                            button.focus(event.pos)

            if self.world_objects != dict():
                if keys[pygame.K_w]:
                    delta_z += .1
                if keys[pygame.K_s]:
                    delta_z -= .1
                if keys[pygame.K_a]:
                    delta_x += .1
                if keys[pygame.K_d]:
                    delta_x -= .1
                if keys[pygame.K_SPACE]:
                    delta_y -= .1
                if delta_y < 0:
                    delta_y += .025
            if pygame.event.get_grab():
                rotation_x += (pygame.mouse.get_pos()[0] - self.screen.get_width() / 2) * .01
                rotation_y += (pygame.mouse.get_pos()[1] - self.screen.get_height() / 2) * .01
                pygame.mouse.set_pos(self.screen.get_width() / 2, self.screen.get_height() / 2)

            self.optional_update()
            self.bbox_highlight(keys, mods)
            if True in [screen_object.focus_state for screen_object in screen_objects.values()]:
                for button in self.screen_objects["Buttons"].values():
                    if button.active_state:
                        if button.focus_state:
                            button.focus(button.rect.center)
                        else:
                            button.focus(mouse_pos)

            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

            GL.glViewport(0, 0, self.screen.get_width(), self.screen.get_height())
            GL.glMatrixMode(GL.GL_PROJECTION)
            GL.glLoadIdentity()
            GL.glMatrixMode(GL.GL_MODELVIEW)
            GL.glLoadIdentity()

            GLU.gluPerspective(90, self.screen.get_width() / self.screen.get_height(), 0.1, 50.0)
            if "player" in self.world_objects:
                for vertex in range(len(self.world_objects["player"].vertices)):
                    self.world_objects["player"].vertices[vertex][0] = \
                        self.world_objects["player"].original_vertices[vertex][0] - delta_x
                    self.world_objects["player"].vertices[vertex][1] = \
                        self.world_objects["player"].original_vertices[vertex][1] - delta_y
                    self.world_objects["player"].vertices[vertex][2] = \
                        self.world_objects["player"].original_vertices[vertex][2] - delta_z
                object_x = numpy.mean([vertex[0] for vertex in self.world_objects["player"].vertices])
                object_y = numpy.mean([vertex[1] for vertex in self.world_objects["player"].vertices])
                object_z = numpy.mean([vertex[2] for vertex in self.world_objects["player"].vertices])
                eyex = object_x + 2.5 * numpy.cos(rotation_y) * numpy.sin(rotation_x)
                eyey = object_y + 2.5 * numpy.sin(rotation_y) * numpy.sin(rotation_x)
                eyez = object_z + 2.5 * numpy.cos(rotation_x)
                GLU.gluLookAt(eyex, eyey, eyez, object_x, object_y, object_z, 0, 1, 0)

            for world_object in self.world_objects.values():
                world_object.render()

            GL.glViewport(0, 0, self.screen.get_width(), self.screen.get_height())
            GL.glMatrixMode(GL.GL_PROJECTION)
            GL.glLoadIdentity()
            GL.glOrtho(0.0, self.screen.get_width(), 0.0, self.screen.get_height(), 0.0, 1.0)
            GL.glMatrixMode(GL.GL_MODELVIEW)
            GL.glLoadIdentity()

            for screen_object_dict in self.screen_objects.values():
                for screen_object in screen_object_dict.values():
                    screen_object.text_update()
                    screen_object.render()

            pygame.display.flip()

            self.clock.tick()

    def main_menu(self):
        for screen_object_dict in self.screen_objects.values():
            screen_object_dict.clear()
        self.screen_objects["Texts"]["title"] = Text(
            rect=(10, 10, 380, 60), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 50, True),
            text="Diablo: The RPG"
        )
        self.screen_objects["Texts"]["subtitle"] = Text(
            rect=(20, 80, 515, 30), bg_color=(0, 0, 0), fg_color=(10, 10, 10),
            font=("Times New Roman", 30, False, True), text="Based on Diablo III lore and information."
        )
        self.screen_objects["Texts"]["version"] = Text(
            rect=(20, 670, 130, 30), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            text="Version: 0.0.1"
        )
        self.screen_objects["Buttons"]["new_game"] = Button(
            rect=(20, 150, 160, 40), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 30, True),
            text="New Game", command=self.character_sheet, focus_command=self.button_menu, justify="center"
        )
        self.screen_objects["Buttons"]["load_game"] = Button(
            rect=(20, 200, 160, 40), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 30, True),
            text="Load Game", command=self.load_menu, focus_command=self.button_menu, justify="center"
        )
        self.screen_objects["Buttons"]["options"] = Button(
            rect=(20, 250, 160, 40), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 30, True),
            text="Options", command=self.options_menu, focus_command=self.button_menu, justify="center"
        )
        self.screen_objects["Buttons"]["exit"] = Button(
            rect=(20, 300, 160, 40), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 30, True),
            text="Exit", command=lambda:
            self.selection_choice(
                given_text="Are you sure you want to exit?", yes_command=lambda: [pygame.quit(), quit()]
            ),
            focus_command=self.button_menu, justify="center"
        )

    def character_sheet(self):
        try:
            class_info_txt = open("class_info.txt", "r")
            class_info = class_info_txt.read().split("\n")
            self.system_variables["class_info_dict"] = dict()
            for line in class_info:
                class_name, class_information = line.split(":  ")
                class_description, class_stats = class_information.split("(SP)")
                self.system_variables["class_info_dict"].update(
                    {class_name: ["\n".join(class_description.split("(NL)")), class_stats]}
                )
        except FileNotFoundError:
            pass
        for screen_object_dict in self.screen_objects.values():
            screen_object_dict.clear()
        self.system_variables["chosen_class"] = ""
        self.screen_objects["Texts"]["character_sheet"] = Text(
            rect=(10, 10, 360, 60), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 50, True),
            text="Character Sheet"
        )
        self.screen_objects["Texts"]["name"] = Text(
            rect=(30, 80, 90, 40), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 30, True),
            text="Name:"
        )
        self.screen_objects["TextInputs"]["name"] = TextInput(
            rect=(130, 80, 500, 40), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 30, True),
            limit=20
        )

        self.screen_objects["Texts"]["class"] = Text(
            rect=(30, 130, 90, 40), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 30, True),
            text="Class:"
        )
        object_height = 180
        for class_name in self.system_variables["class_info_dict"]:
            self.screen_objects["Buttons"][class_name.lower()] = Button(
                rect=(50, object_height, 140, 30), bg_color=(0, 0, 0), fg_color=(0, 255, 0),
                font=("Times New Roman", 20, True), text=class_name, command=self.class_update,
                focus_command=self.class_focus, justify="center"
            )
            object_height += 40

        self.screen_objects["Texts"]["description"] = Text(
            rect=(200, 130, 165, 40), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 30, True),
            text="Description:"
        )
        self.screen_objects["Texts"]["full_description"] = Text(
            rect=(200, 180, 430, 460), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 18, True),
            width=1
        )
        for class_name in self.system_variables["class_info_dict"]:
            self.screen_objects["Texts"]["full_description"].text_update(
                self.system_variables["class_info_dict"][class_name][0]
            )
        self.screen_objects["Texts"]["full_description"].text_update("")

        self.screen_objects["Texts"]["statistics"] = Text(
            rect=(640, 130, 135, 40), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 30, True),
            text="Statistics:"
        )
        self.screen_objects["Texts"]["attack"] = Text(
            rect=(640, 180, 280, 55), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            width=1, text="Attack: 0\nAll damage increased by: 0.00%"
        )
        self.screen_objects["Texts"]["precision"] = Text(
            rect=(640, 245, 280, 55), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            width=1, text="Precision: 0\nChange to critical hit: 0.00%"
        )
        self.screen_objects["Texts"]["defense"] = Text(
            rect=(640, 310, 280, 55), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            width=1, text="Defense: 0\nAll damage reduced by: 0.00%"
        )
        self.screen_objects["Texts"]["vitality"] = Text(
            rect=(640, 375, 280, 55), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            width=1, text="Vitality: 0\nLife: 0"
        )
        for class_name in self.system_variables["class_info_dict"]:
            for stat in self.system_variables["class_info_dict"][class_name][1].split(", "):
                stat_name, stat_int = stat.split(": ")
                stat_info = self.screen_objects['Texts'][stat_name.lower()].text.split('\n')[1]
                self.screen_objects["Texts"][stat_name.lower()].text_update(
                    f"{stat}\n{stat_info.split(': ')[0]}: {float(stat_int) / 2}%"
                )
                self.screen_objects["Texts"][stat_name.lower()].text_update(
                    f"{stat_name}: 0\n{stat_info.split(': ')[0]}: 0.00%"
                )

        self.screen_objects["Buttons"]["back"] = Button(
            rect=(20, 660, 100, 40), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 30, True),
            text="Back", command=self.main_menu, focus_command=self.button_highlight, justify="center"
        )
        self.screen_objects["Buttons"]["start"] = Button(
            rect=(130, 660, 100, 40), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 30, True),
            text="Start", command=lambda:
            self.selection_choice(given_text="Are you sure you want to start?", yes_command=self.main_sequence),
            focus_command=self.button_highlight, justify="center"
        )

    def main_sequence(self):
        self.system_variables["inputted_name"] = self.screen_objects["TextInputs"]["name"].text
        for screen_object_dict in self.screen_objects.values():
            screen_object_dict.clear()
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)

        self.screen_objects["Texts"]["name"] = Text(
            rect=(20, 610, 100, 90), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            text=f"{self.system_variables['inputted_name']}", width=1, justify="center"
        )
        self.screen_objects["Texts"]["health"] = Text(
            rect=(120, 610, 1000, 30), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            text="Health:", width=1
        )
        self.screen_objects["Texts"]["health_bar"] = Text(rect=(195, 615, 915, 20), bg_color=(255, 0, 0), text=None)
        self.screen_objects["Texts"]["magic"] = Text(
            rect=(120, 640, 1000, 30), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            text="Magic:", width=1
        )
        self.screen_objects["Texts"]["magic_bar"] = Text(rect=(195, 645, 915, 20), bg_color=(0, 0, 255), text=None)
        self.screen_objects["Texts"]["level"] = Text(
            rect=(120, 670, 1000, 30), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            text="Level:", width=1
        )
        self.screen_objects["Texts"]["level_bar"] = Text(rect=(195, 675, 915, 20), bg_color=(255, 255, 0), text=None)

        self.world_objects["player"] = Quad(
            vertices=[
                [0.25, -0.5, -1], [0.25, 0.5, -1], [-0.25, 0.5, -1], [-0.25, -0.5, -1],
                [0.25, -0.5, -1.5], [0.25, 0.5, -1.5], [-0.25, -0.5, -1.5], [-0.25, 0.5, -1.5]
            ],
            edges=(
                (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)
            )
        )
        self.world_objects["initial_position"] = Quad(
            vertices=[
                [0.25, -0.5, -1], [0.25, 0.5, -1], [-0.25, 0.5, -1], [-0.25, -0.5, -1],
                [0.25, -0.5, -1.5], [0.25, 0.5, -1.5], [-0.25, -0.5, -1.5], [-0.25, 0.5, -1.5]
            ],
            edges=(
                (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)
            )
        )

    def load_menu(self):
        pass

    def options_menu(self):
        pass

    def optional_init(self):
        self.system_variables["init_time"] = time.localtime()
        init_time = self.system_variables['init_time']
        self.system_variables["time_text"] = True
        self.screen_objects["Texts"]["time"] = Text(
            rect=(1160, 650, 100, 50), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            text=f"{('0' * (len(str(init_time.tm_hour)) % 2)) + str(init_time.tm_hour)}:"
                 f"{('0' * (len(str(init_time.tm_min)) % 2)) + str(init_time.tm_min)}:"
                 f"{('0' * (len(str(init_time.tm_sec)) % 2)) + str(init_time.tm_sec)}\n"
                 f"{init_time.tm_mday}/{init_time.tm_mon}/{init_time.tm_year}", justify="center", width=1
        )

        self.system_variables["init_fps"] = int(self.clock.get_fps())
        init_fps = self.system_variables['init_fps']
        self.system_variables["fps_text"] = True
        self.screen_objects["Texts"]["fps"] = Text(
            rect=(1170, 20, 90, 30), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            text=f"FPS: {init_fps}", width=1
        )

    def optional_update(self):
        if "time" in self.screen_objects["Texts"]:
            self.system_variables["current_time"] = time.localtime()
            current_time = self.system_variables["current_time"]
            self.screen_objects["Texts"]["time"].text_update(
                f"{('0' * (len(str(current_time.tm_hour)) % 2)) + str(current_time.tm_hour)}:"
                f"{('0' * (len(str(current_time.tm_min)) % 2)) + str(current_time.tm_min)}:"
                f"{('0' * (len(str(current_time.tm_sec)) % 2)) + str(current_time.tm_sec)}\n"
                f"{current_time.tm_mday}/{current_time.tm_mon}/{current_time.tm_year}"
            )
        else:
            if self.system_variables["time_text"]:
                current_time = self.system_variables['current_time']
                self.screen_objects["Texts"]["time"] = Text(
                    rect=(1160, 650, 100, 50), bg_color=(0, 0, 0), fg_color=(0, 255, 0),
                    font=("Times New Roman", 20, True),
                    text=f"{('0' * (len(str(current_time.tm_hour)) % 2)) + str(current_time.tm_hour)}:"
                    f"{('0' * (len(str(current_time.tm_min)) % 2)) + str(current_time.tm_min)}:"
                    f"{('0' * (len(str(current_time.tm_sec)) % 2)) + str(current_time.tm_sec)}\n"
                    f"{current_time.tm_mday}/{current_time.tm_mon}/{current_time.tm_year}", justify="center",
                    width=1
                )

        if "fps" in self.screen_objects["Texts"]:
            self.system_variables["current_fps"] = int(self.clock.get_fps())
            current_fps = self.system_variables["current_fps"]
            self.screen_objects["Texts"]["fps"].text_update(f"FPS: {current_fps}")
        else:
            if self.system_variables["fps_text"]:
                current_fps = self.system_variables['current_fps']
                self.screen_objects["Texts"]["fps"] = Text(
                    rect=(1170, 20, 90, 30), bg_color=(0, 0, 0), fg_color=(0, 255, 0),
                    font=("Times New Roman", 20, True),
                    text=f"FPS: {current_fps}",
                    width=1
                )

    def class_focus(self, given_object, pos):
        if given_object.focus_state and self.screen_objects["Texts"]["full_description"].text != \
                self.system_variables["class_info_dict"][given_object.text][0]:
            self.screen_objects["Texts"]["full_description"].text_update(
                self.system_variables["class_info_dict"][given_object.text][0]
            )
            for stat in self.system_variables["class_info_dict"][given_object.text][1].split(", "):
                stat_name, stat_int = stat.split(": ")
                stat_info = self.screen_objects['Texts'][stat_name.lower()].text.split('\n')[1]
                self.screen_objects["Texts"][stat_name.lower()].text_update(
                    f"{stat}\n{stat_info.split(': ')[0]}: {float(stat_int) / 2}%"
                )
        if True not in [self.screen_objects["Buttons"][class_name.lower()].focus_state
                        for class_name in self.system_variables["class_info_dict"]] and \
                self.system_variables["chosen_class"] in self.system_variables["class_info_dict"] and \
                self.screen_objects["Texts"]["full_description"].text != \
                self.system_variables["class_info_dict"][self.system_variables["chosen_class"]][0]:
            if self.system_variables["class_info_dict"][self.system_variables["chosen_class"]][0] != given_object.text:
                given_object.bg_color = (0, 255, 0)
            self.screen_objects["Texts"]["full_description"].text_update(
                self.system_variables["class_info_dict"][self.system_variables["chosen_class"]][0]
            )
            for stat in self.system_variables["class_info_dict"][self.system_variables["chosen_class"]][1].split(", "):
                stat_name, stat_int = stat.split(": ")
                stat_info = self.screen_objects['Texts'][stat_name.lower()].text.split('\n')[1]
                self.screen_objects["Texts"][stat_name.lower()].text_update(
                    f"{stat}\n{stat_info.split(': ')[0]}: {float(stat_int) / 2}%"
                )
        self.button_highlight(given_object, pos)

    def class_update(self, given_object):
        self.system_variables["chosen_class"] = given_object.text
        if (0, 0, 0) in [self.screen_objects["Buttons"][class_name.lower()].fg_color
                         for class_name in self.system_variables["class_info_dict"]]:
            for class_name in self.system_variables["class_info_dict"]:
                self.screen_objects["Buttons"][class_name.lower()].fg_color = \
                    self.screen_objects["Buttons"][class_name.lower()].original_fg_color
                self.screen_objects["Buttons"][class_name.lower()].original_bg_color = (0, 0, 0)
        given_object.fg_color = (0, 0, 0)
        given_object.original_bg_color = (0, 255, 0)

    def selection_choice(self, given_text="", yes_command=None, no_command=None):
        for screen_object in [*self.screen_objects["Buttons"].values(), *self.screen_objects["TextInputs"].values()]:
            screen_object.active_state = False
            screen_object.focus_state = False
        for screen_dict in self.screen_objects.values():
            for screen_object in screen_dict.values():
                if screen_object.fg_color == (0, 255, 0):
                    screen_object.fg_color = (0, 100, 0)
        self.screen_objects["Texts"]["selection"] = Text(
            rect=(540, 345, 200, 50), bg_color=(0, 0, 0), fg_color=(0, 255, 0), text=given_text,
            font=("Times New Roman", 20, True), justify="center", width=1
        )
        self.screen_objects["Buttons"]["yes"] = Button(
            rect=(595, 400, 40, 30), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            text="Yes", command=yes_command, focus_command=self.button_highlight, justify="center"
        )
        self.screen_objects["Buttons"]["no"] = Button(
            rect=(645, 400, 40, 30), bg_color=(0, 0, 0), fg_color=(0, 255, 0), font=("Times New Roman", 20, True),
            text="No", command=lambda: [
                no_command() if no_command is not None else None,
                [setattr(screen_object_, "active_state", True) for screen_object_ in
                 [*self.screen_objects["Buttons"].values(), *self.screen_objects["TextInputs"].values()]],
                [setattr(screen_object_, "fg_color", screen_object_.original_fg_color)
                 for screen_dicts in self.screen_objects.values()
                 for screen_object_ in screen_dicts.values()],
                self.screen_objects["Buttons"].pop("yes"),
                self.screen_objects["Buttons"].pop("no"),
                self.screen_objects["Texts"].pop("selection")
            ], focus_command=self.button_highlight, justify="center"
        )

    def bbox_highlight(self, keys, mods):
        if keys[pygame.K_c] and mods & pygame.KMOD_CTRL and mods & pygame.KMOD_LSHIFT:
            for screen_object_dict in self.screen_objects.values():
                for screen_object in screen_object_dict.values():
                    screen_object.bg_color = (0, 100, 0)
        else:
            for screen_object_dict in self.screen_objects.values():
                for screen_object in screen_object_dict.values():
                    screen_object.bg_color = screen_object.original_bg_color

    @staticmethod
    def button_menu(given_object, pos):
        if given_object.rect.collidepoint(*pos):
            given_object.focus_state = True
        else:
            given_object.focus_state = False
        if given_object.rect.width < given_object.original_rect.width * 1.1 and given_object.focus_state:
            given_object.rect.width *= 1.025
        elif given_object.rect.width > given_object.original_rect.width and not given_object.focus_state:
            given_object.rect.width *= .975
        if given_object.rect.width < given_object.original_rect.width and not given_object.focus_state:
            given_object.rect.width = given_object.original_rect.width

    @staticmethod
    def button_highlight(given_object, pos):
        if given_object.rect.collidepoint(*pos):
            given_object.focus_state = True
            given_object.bg_color = (0, 100, 0)
        else:
            given_object.focus_state = False
            given_object.bg_color = given_object.original_bg_color


class MenuObject:
    def __init__(self, rect=(0, 0, 100, 100), bg_color=(0, 0, 0), fg_color=(0, 0, 0), text="",
                 font=("Times New Roman", 20, False, False), justify="left", width=0):
        self.font = pygame.font.SysFont(*font)
        self.original_rect = pygame.rect.Rect(rect)
        self.rect = pygame.rect.Rect(rect)
        self.original_bg_color = bg_color
        self.bg_color = bg_color
        self.original_fg_color = fg_color
        self.fg_color = fg_color
        self.text = text
        self.text_rect = self.rect[:]
        self.cached_text = dict()
        self.formatted_text = list()
        self.justify = justify
        self.width = width
        self.text_update()

    def render(self):
        self.text_rect = self.rect[:]
        GL.glBegin(GL.GL_QUADS)
        GL.glColor3fv((self.bg_color[0] / 255, self.bg_color[1] / 255, self.bg_color[2] / 255))
        GL.glVertex2f(self.rect[0], 720 - self.rect[1])
        GL.glVertex2f(self.rect[0] + self.rect[2], 720 - self.rect[1])
        GL.glVertex2f(self.rect[0] + self.rect[2], 720 - (self.rect[1] + self.rect[3]))
        GL.glVertex2f(self.rect[0], 720 - (self.rect[1] + self.rect[3]))
        GL.glEnd()
        if self.width > 0:
            GL.glBegin(GL.GL_LINES)
            GL.glColor3fv((self.fg_color[0] / 255, self.fg_color[1] / 255, self.fg_color[2] / 255))
            GL.glVertex2f(self.rect[0], 720 - self.rect[1])
            GL.glVertex2f(self.rect[0] + self.rect[2], 720 - self.rect[1])
            GL.glVertex2f(self.rect[0] + self.rect[2], 720 - self.rect[1])
            GL.glVertex2f(self.rect[0] + self.rect[2], 720 - (self.rect[1] + self.rect[3]))
            GL.glVertex2f(self.rect[0] + self.rect[2], 720 - (self.rect[1] + self.rect[3]))
            GL.glVertex2f(self.rect[0], 720 - (self.rect[1] + self.rect[3]))
            GL.glVertex2f(self.rect[0], 720 - (self.rect[1] + self.rect[3]))
            GL.glVertex2f(self.rect[0], 720 - self.rect[1])
            GL.glEnd()
        if self.justify == "left":
            self.text_rect[0] += 5
        self.text_rect[1] += 2
        for text_line in range(len(self.formatted_text)):
            text_x = 0
            if self.justify == "center":
                text_x = (self.rect.width - self.formatted_text[text_line].get_width()) / 2
            self.text_rect[0] += text_x
            textdata = pygame.image.tostring(self.formatted_text[text_line], "RGBA", True)
            GL.glRasterPos2d(self.text_rect[0], 720 - (self.text_rect[1] + self.formatted_text[text_line].get_height()))
            GL.glDrawPixels(self.formatted_text[text_line].get_width(), self.formatted_text[text_line].get_height(),
                            GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, textdata)
            self.text_rect[0] += self.formatted_text[text_line].get_width()
            if len(self.formatted_text) > text_line + 1:
                self.text_rect[1] += self.formatted_text[text_line].get_height()
                self.text_rect[0] -= text_x + self.formatted_text[text_line].get_width()

    def text_update(self, text=None):
        if text is not None:
            self.text = text
        if self.text is not None:
            if f"{self.text}{self.fg_color}{self.bg_color}" not in self.cached_text:
                self.formatted_text = self.text.split("\n")
                text_line = 0
                while len(self.formatted_text) > text_line:
                    text_size = self.font.size(self.formatted_text[text_line])
                    new_line = " ".join(self.formatted_text[text_line].split()[:-1])
                    while text_size[0] >= self.rect.width - 5:
                        new_line = " ".join(new_line.split()[:-1])
                        text_size = self.font.size(new_line)
                    if new_line != " ".join(self.formatted_text[text_line].split()[:-1]):
                        self.formatted_text.insert(text_line + 1, self.formatted_text[text_line][len(new_line) + 1:])
                        self.formatted_text[text_line] = self.font.render(
                            new_line, True, self.fg_color, self.bg_color + (255,)
                        )
                    else:
                        self.formatted_text[text_line] = self.font.render(
                            self.formatted_text[text_line], True, self.fg_color, self.bg_color + (255,)
                        )
                    text_line += 1
                self.cached_text[f"{self.text}{self.fg_color}{self.bg_color}"] = self.formatted_text[:]
            elif f"{self.text}{self.fg_color}{self.bg_color}" in self.cached_text:
                self.formatted_text = self.cached_text[f"{self.text}{self.fg_color}{self.bg_color}"][:]


class Text(MenuObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Button(MenuObject):
    def __init__(self, command=None, focus_command=None, width=1, **kwargs):
        super().__init__(width=width, **kwargs)
        self.command = command
        self.focus_state_command = focus_command
        self.focus_state = False
        self.active_state = True

    def activate(self, given_object):
        if self.command is not None:
            try:
                self.command(given_object)
            except TypeError:
                self.command()

    def focus(self, pos):
        if self.focus_state_command is not None:
            self.focus_state_command(self, pos)


class TextInput(MenuObject):
    def __init__(self, limit=0, width=1, **kwargs):
        super().__init__(width=width, **kwargs)
        self.limit = limit
        self.focus_state = False
        self.repeater_state = 0
        self.key_dict = {
            "`": "~", "1": "!", "2": "@", "3": "#", "4": "$", "5": "%", "6": "^", "7": "&", "8": "*", "9": "(",
            "0": ")", "-": "_", "=": "+", "[": "{", "]": "}", ";": ":", "'": '"', "\\": "|", ",": "<", ".": ">",
            "/": "?"
        }
        self.active_state = True

    def render(self):
        super().render()
        if self.focus_state:
            if self.repeater_state <= 60:
                repeater = self.font.render("|", True, self.fg_color, self.bg_color + (255,))
                textdata = pygame.image.tostring(repeater, "RGBA", True)
                GL.glRasterPos2d(self.text_rect[0], 720 - (self.text_rect[1] + repeater.get_height()))
                GL.glDrawPixels(repeater.get_width(), repeater.get_height(), GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, textdata)
                self.repeater_state += 1
            elif self.repeater_state <= 120:
                self.repeater_state += 1
            else:
                self.repeater_state = 0
        else:
            self.repeater_state = 0

    def input(self, event, mods):
        if self.focus_state:
            key_name = pygame.key.name(event.key)
            if len(self.text) < self.limit or self.limit == 0:
                if key_name in string.ascii_letters:
                    if not mods & pygame.KMOD_LSHIFT:
                        self.text_update(self.text + key_name)
                    elif mods & pygame.KMOD_LSHIFT:
                        self.text_update(self.text + key_name.upper())
                elif key_name in self.key_dict:
                    if not mods & pygame.KMOD_LSHIFT:
                        self.text_update(self.text + key_name)
                    elif mods & pygame.KMOD_LSHIFT:
                        self.text_update(self.text + self.key_dict[key_name])
                elif key_name == "space":
                    self.text_update(self.text + " ")
            if key_name == "backspace":
                self.text_update(self.text[:-1])


class Quad:
    def __init__(self, vertices, edges):
        self.original_vertices = vertices[:]
        for vertex in range(len(self.original_vertices)):
            self.original_vertices[vertex] = tuple(self.original_vertices[vertex])
        self.original_vertices = tuple(self.original_vertices)
        self.vertices = vertices
        self.original_edges = edges
        self.edges = edges

    def render(self):
        GL.glBegin(GL.GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                GL.glVertex3fv(self.vertices[vertex])
        GL.glEnd()


if __name__ == '__main__':
    try:
        import ctypes
        screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
    except ModuleNotFoundError:
        screensize = (1280, 720)
    App()
