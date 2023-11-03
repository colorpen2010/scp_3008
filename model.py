import pygame,furniture

bmoveX=200
bmoveY=200
player2=furniture.Furniture(bmoveX,bmoveY,None,'sprites/player/игрок.png')
player2.player=player2
box1=furniture.Furniture(bmoveX+40,bmoveY,player2,'sprites/props/коробка.png')