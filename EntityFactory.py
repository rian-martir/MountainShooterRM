from Const import ASSET_PLAYER, ASSET_ENEMY_1
# Supondo que você crie classes para Player e Enemy
# from Player import Player

class EntityFactory:
    @staticmethod
    def get_entity(entity_type):
        if entity_type == 'Player':
            # return Player(ASSET_PLAYER, (10, 10))
            pass
        if entity_type == 'Enemy1':
            # return Enemy(ASSET_ENEMY_1, (500, 100))
            pass
