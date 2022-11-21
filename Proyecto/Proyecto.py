import pygame,sys
import numpy as np

pygame.init()

negro  = (0,0,0)
blanco = (255,255,255)
gris   = (127,127,127)

class Game(object):

    def __init__(self, ancho_juego, alto_juego):
        pygame.display.set_caption('Serpiente')
        self.ancho_juego = ancho_juego
        self.alto_juego = alto_juego
        self.display_juego = pygame.display.set_mode((ancho_juego, alto_juego+100))

        self.colision = False
        self.score = 0
        self.font = pygame.font.SysFont('Arial', 25)

    def display_ui(self, record):
        self.display_juego.fill(blanco)
        score_txt = self.font.render('Puntos: ', True, (255, 255, 255))
        score_num = self.font.render(str(self.score), True, (255, 255, 255))
        record_txt = self.font.render('Record: ', True, (255, 255, 255))
        record_num = self.font.render(str(record), True, (255, 255, 255))

        pygame.draw.rect(self.display_juego, (0, 0, 0), (0, self.alto_juego, self.alto_juego, 100))

        self.display_juego.blit(score_txt, (45, 480))
        self.display_juego.blit(score_num, (170, 480))
        self.display_juego.blit(record_txt, (270, 480))
        self.display_juego.blit(record_num, (350, 480))

    def obtener_record(self, score, record):
        return score if score >= record else record

imagenes = pygame.sprite.Group()
efectos  = pygame.sprite.Group()

class personaje(object):

    def __init__(self):
        self.x = 100
        self.y = 100
        self.posicion = []
        self.posicion.append([self.x, self. y])
        self.n_manzanas = 1
        self.comida = False
        self.imagen = pygame.image.load('bssets/fantasma rojo.png')
        self.cambio_x = 20
        self.cambio_y = 0
        self.direccion = [1, 0]

    def refrescar_posicion(self, x, y):
        if self.posicion[-1][0] != x or self.posicion[-1][0] != y:
            if self.n_manzanas > 1:
                for i in range(self.n_manzanas - 1):
                    self.posicion[i][0], self.posicion[i][1] = self.posicion[i + 1]

            self.posicion[-1][0] = x
            self.posicion[-1][1] = y

    def hacer_movimiento(self, x, y, game, food):
        array_m = [self.cambio_x, self.cambio_y]

        if self.comida:
            self.posicion.append([self.x, self.y])
            self.comida = False
            self.n_manzanas += 1

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT and self.direccion != [1, 0]:
                    array_m = [-20, 0]
                    self.direccion = [-1, 0]
                elif e.key == pygame.K_RIGHT and self.direccion != [-1, 0]:
                    array_m = [20, 0]
                    self.direccion = [1, 0]
                elif e.key == pygame.K_UP and self.direccion != [0, -1]:
                    array_m = [0, -20]
                    self.direccion = [0, 1]
                elif e.key == pygame.K_DOWN and self.direccion != [0, 1]:
                    array_m = [0, 20]
                    self.direccion = [0, -1]

        self.cambio_x, self.cambio_y = array_m
        self.x = x + self.cambio_x
        self.y = y + self.cambio_y

        if self.x < 0 or self.x > game.ancho_juego-20 \
                or self.y < 0 or self.y > game.alto_juego-20 \
                or [self.x, self.y] in self.posicion:
            game.colision = True

        food.comer(self, game)
        self.refrescar_posicion(self.x, self.y)

    def display_jugador(self, x, y, game):
        self.posicion[-1][0] = x
        self.posicion[-1][1] = y

        if game.colision == False:
            for i in range(self.n_manzanas):
                x_temp, y_temp = self.posicion[len(self.posicion) -1 -i]
                game.display_juego.blit(self.imagen, (x_temp, y_temp))

    def disparar(Self):
        arma= arma()
        imagenes.add(arma)
        efectos.add(arma)


class Laser(pygame.sprite.Sprite):
    def  __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bssets/puntosadisparar.png")
        self.image.set_colorkey(gris)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class pacmans(object):

    def __init__(self):
        self.x_food = 200
        self.y_food = 200
        self.image = pygame.image.load('bssets/pacman.png').convert()

    def comida_coor(self, game, player):
        x_rand = np.random.choice(list(range(0, game.ancho_juego, 20)))
        self.x_food = x_rand
        y_rand = np.random.choice(list(range(0, game.alto_juego, 20)))
        self.y_food = y_rand

    def display_comida(self, x, y, game):
        game.display_juego.blit(self.image, (x, y))

    def comer(self, player, game):
        if player.x == self.x_food and player.y == self.y_food:
            self.comida_coor(game, player)
            player.comida = True
            game.score += 1




running = True
def run():
    pygame.init()
    record = 0
    clock = pygame.time.Clock()
    
    while True:
        game = Game(420, 420)
        player = personaje()
        punto = pacmans()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.disparar()

        imagenes.update()


        game.display_ui(record)
        player.display_jugador(player.x, player.y, game)
        punto.display_comida(punto.x_food, punto.y_food, game)
        pygame.display.update()

        while not game.colision:
            player.hacer_movimiento(player.x, player.y, game, punto)
            record = game.obtener_record(game.score, record)
            game.display_ui(record)
            player.display_jugador(player.x, player.y, game)
            punto.display_comida(punto.x_food, punto.y_food, game)
            pygame.display.update()
            clock.tick(10)

if __name__ == '__main__':
    run()
