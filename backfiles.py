import settings
player=None
def xmovier(bX):
    return bX - player.bX + settings.SIZE[0] / 2
def ymovier(bY):
    return bY - player.bY + settings.SIZE[1] / 2