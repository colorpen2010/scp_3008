import pygame,entity,inventories,player

bmoveX=200
bmoveY=200
player=player.Player()
inventory=inventories.Inventory_system(False)
water=entity.Entity(bmoveX-40,bmoveY,player,'sprites/props/usable/ВОДА.png')
box1=entity.Entity(bmoveX + 40, bmoveY, player, 'sprites/props/коробка.png')