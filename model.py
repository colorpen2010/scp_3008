import pygame,entity,inventories

bmoveX=200
bmoveY=200
player=entity.Entity(bmoveX, bmoveY, None, 'sprites/player/игрок.png')
player.player=player
inventory=inventories.Inventory_system(False)
box1=entity.Entity(bmoveX + 40, bmoveY, player, 'sprites/props/коробка.png')