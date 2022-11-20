import pygame,sys
import numpy as np

pygame.init()

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
        self.display_juego.fill((127, 127, 127))
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
