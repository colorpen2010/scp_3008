import pygame,entity,inventories,player

bmoveX=200
bmoveY=200
player=player.Player()
inventory=inventories.Inventory_system(False)
water=entity.Entity(160,200,player,'sprites/props/usable/ВОДА.png')
box1=entity.Entity(240, 200, player, 'sprites/props/коробка.png')