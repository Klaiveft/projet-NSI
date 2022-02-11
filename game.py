import pygame
import pytmx
import pyscroll
from player import Player

class Game:

    def __init__(self):

        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Labyrinthe")

        #charge la carte
        tmx_data = pytmx.util_pygame.load_pygame('MAP 1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        #charge le joueur
        player_position = tmx_data.get_object_by_name("spawn_1")
        self.player = Player(player_position.x, player_position.y)

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 1)
        self.group.add(self.player)

        entree_1 = tmx_data.get_layer_by_name("entrer_1")
        sefl.entree_1_rect = pygame.Rect(entree_1.x, entree_1.y, entree_1.width, entree_1.height)


    def handle_input(self):
        press = pygame.key.get_pressed()



        if press[pygame.K_UP]:
            self.player.mouv_up()
            self.player.change_annimation('up')

        elif press[pygame.K_DOWN]:
            self.player.mouv_down()
            self.player.change_annimation('down')

        elif press[pygame.K_LEFT]:
            self.player.mouv_left()
            self.player.change_annimation('left')

        elif press[pygame.K_RIGHT]:
            self.player.mouv_right()
            self.player.change_annimation('right')

    def switch_map(self):
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Labyrinthe")

        #charge la carte
        tmx_data = pytmx.util_pygame.load_pygame('MAP 2.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        #charge le joueur
        player_position = tmx_data.get_object_by_name("spawn_2")
        self.player = Player(player_position.x, player_position.y)

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 1)
        self.group.add(self.player)

        entree_1 = tmx_data.get_layer_by_name("entrer_1")
        sefl.entree_1_rect = pygame.Rect(entree_1.x, entree_1.y, entree_1.width, entree_1.height)


    def update(self):
        self.group.update()

        if self.player.feet.colliderect(self.entree_1.rect):
            self.switch_map()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.mouv_back()


    def song(self):
        self.song = pygame.mixer.Sound("offshore.ogg")
        return self.song.play(6)

    def run(self):

        clock = pygame.time.Clock()
        self.song()
        running = True
        while running:


            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()