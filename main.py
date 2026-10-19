class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
@namespace
class SpriteKind:
    Coin = SpriteKind.create()
    Flower = SpriteKind.create()
    Coin10 = SpriteKind.create()
    Coin100 = SpriteKind.create()
    Bee = SpriteKind.create()
    Catacter = SpriteKind.create()
    Apple_Food = SpriteKind.create()
    doggyemeraldcoin = SpriteKind.create()
    GoldenApple_Food = SpriteKind.create()
    Imperial_Catacater = SpriteKind.create()
    Head_Scientist_Catacter = SpriteKind.create()
    teleporter_sender = SpriteKind.create()
    telepoter_reciever = SpriteKind.create()
    flowing_lava = SpriteKind.create()
    still_lava = SpriteKind.create()
def Start_Level():
    global Coin2, Flower2, Catacter_Sprite, Coin10Var, Coin1002, Apple, Golden_Apple, Imperial_Catacter_Sprite, Head_Scintist_Catacter_Sprite, teleport_portal, teleport_portal_2
    if current_level == 0:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
    elif current_level == 1:
        tiles.set_current_tilemap(tilemap("""
            level_2
        """))
        Health_Bar.value = 110
        Health_Bar.max = 110
    elif current_level == 2:
        tiles.set_current_tilemap(tilemap("""
            level_3
        """))
        Health_Bar.value = 120
        Health_Bar.max = 120
    elif current_level == 3:
        tiles.set_current_tilemap(tilemap("""
            level_4true
        """))
        Health_Bar.value = 130
        Health_Bar.max = 130
    elif current_level == 4:
        tiles.set_current_tilemap(tilemap("""
            level_5
        """))
        Health_Bar.value = 140
        Health_Bar.max = 140
    elif current_level == 5:
        tiles.set_current_tilemap(tilemap("""
            level_6
        """))
        Health_Bar.value = 150
        Health_Bar.max = 150
    elif current_level == 6:
        tiles.set_current_tilemap(tilemap("""
            level_7
        """))
        Health_Bar.value = 160
        Health_Bar.max = 160
    elif current_level == 7:
        tiles.set_current_tilemap(tilemap("""
            level_8
        """))
        Health_Bar.value = 170
        Health_Bar.max = 170
    elif current_level == 8:
        tiles.set_current_tilemap(tilemap("""
            level27
        """))
        Health_Bar.value = 180
        Health_Bar.max = 180
    elif current_level == 9:
        tiles.set_current_tilemap(tilemap("""
            level_9
        """))
        Health_Bar.value = 190
        Health_Bar.max = 190
    elif False:
        pass
    else:
        game.game_over(True)
        game.set_game_over_message(True, "Remember you can go to the Offical Site For Records")
    tiles.place_on_random_tile(Doggy, assets.tile("""
        Spawn_Doggy
    """))
    for value in tiles.get_tiles_by_type(assets.tile("""
        Spawn_Doggy
    """)):
        tiles.set_tile_at(value, assets.tile("""
            transparency16
        """))
    scene.camera_follow_sprite(Doggy)
    for value2 in sprites.all_of_kind(SpriteKind.Bee):
        sprites.destroy(value2)
    for value3 in sprites.all_of_kind(SpriteKind.Catacter):
        sprites.destroy(value3)
    for value4 in sprites.all_of_kind(SpriteKind.Coin):
        sprites.destroy(value4)
    for value5 in sprites.all_of_kind(SpriteKind.Coin10):
        sprites.destroy(value5)
    for value6 in sprites.all_of_kind(SpriteKind.Coin100):
        sprites.destroy(value6)
    for value7 in sprites.all_of_kind(SpriteKind.Flower):
        sprites.destroy(value7)
    for value8 in tiles.get_tiles_by_type(assets.tile("""
        Coin_Collectable
    """)):
        Coin2 = sprites.create(assets.image("""
            Coin_Actual
        """), SpriteKind.Coin)
        animation.run_image_animation(Coin2,
            assets.animation("""
                Coin_Animation
            """),
            500,
            True)
        tiles.place_on_tile(Coin2, value8)
        tiles.set_tile_at(value8, assets.tile("""
            transparency16
        """))
    for value9 in tiles.get_tiles_by_type(assets.tile("""
        Flower_Placeholder
    """)):
        Flower2 = sprites.create(assets.image("""
            Flower_1
        """), SpriteKind.Flower)
        tiles.place_on_tile(Flower2, value9)
        tiles.set_tile_at(value9, assets.tile("""
            transparency16
        """))
    for value10 in tiles.get_tiles_by_type(assets.tile("""
        Catacter_Tile
    """)):
        Catacter_Sprite = sprites.create(assets.image("""
            Catacter
        """), SpriteKind.Catacter)
        tiles.place_on_tile(Catacter_Sprite, value10)
        tiles.set_tile_at(value10, assets.tile("""
            transparency16
        """))
    for value11 in tiles.get_tiles_by_type(assets.tile("""
        10coin
    """)):
        Coin10Var = sprites.create(assets.image("""
            Coin_10
        """), SpriteKind.Coin10)
        tiles.place_on_tile(Coin10Var, value11)
        tiles.set_tile_at(value11, assets.tile("""
            transparency16
        """))
    for value12 in tiles.get_tiles_by_type(assets.tile("""
        Coin100
    """)):
        Coin1002 = sprites.create(assets.image("""
            Coin_100
        """), SpriteKind.Coin100)
        tiles.place_on_tile(Coin1002, value12)
        tiles.set_tile_at(value12, assets.tile("""
            transparency16
        """))
    for value13 in tiles.get_tiles_by_type(assets.tile("""
        apple_foodtile
    """)):
        Apple = sprites.create(assets.image("""
            apple_food
        """), SpriteKind.Apple_Food)
        tiles.place_on_tile(Apple, value13)
        tiles.set_tile_at(value13, assets.tile("""
            transparency16
        """))
    for value14 in tiles.get_tiles_by_type(assets.tile("""
        GOLDEN_APPLE_FOOD
    """)):
        Golden_Apple = sprites.create(assets.image("""
                goldenapple_food
            """),
            SpriteKind.GoldenApple_Food)
        tiles.place_on_tile(Golden_Apple, value14)
        tiles.set_tile_at(value14, assets.tile("""
            transparency16
        """))
    for value15 in tiles.get_tiles_by_type(assets.tile("""
        Imperial_Catacater_Spawn
    """)):
        Imperial_Catacter_Sprite = sprites.create(assets.image("""
                Imperial_Catacter_Sprite
            """),
            SpriteKind.Imperial_Catacater)
        tiles.place_on_tile(Imperial_Catacter_Sprite, value15)
        tiles.set_tile_at(value15, assets.tile("""
            transparency16
        """))
    for value16 in tiles.get_tiles_by_type(assets.tile("""
        head_scientist_catacter
    """)):
        Head_Scintist_Catacter_Sprite = sprites.create(assets.image("""
                Head_Scientist_Catacter_Sprite
            """),
            SpriteKind.Head_Scientist_Catacter)
        tiles.place_on_tile(Head_Scintist_Catacter_Sprite, value16)
        tiles.set_tile_at(value16, assets.tile("""
            transparency16
        """))
    for value17 in tiles.get_tiles_by_type(assets.tile("""
        teleport_tile_sender
    """)):
        teleport_portal = sprites.create(assets.image("""
                teleport_portal
            """),
            SpriteKind.teleporter_sender)
        tiles.place_on_tile(teleport_portal, value17)
        tiles.set_tile_at(value17, assets.tile("""
            transparency16
        """))
    for value18 in tiles.get_tiles_by_type(assets.tile("""
        teleporter_tile_receiver
    """)):
        teleport_portal_2 = sprites.create(assets.image("""
                teleport_portal_2
            """),
            SpriteKind.telepoter_reciever)
        tiles.place_on_tile(teleport_portal_2, value18)
        tiles.set_tile_at(value18, assets.tile("""
            transparency16
        """))

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.Coin, on_on_overlap)

def on_b_pressed():
    global sonic_bark
    sonic_bark = sprites.create_projectile_from_sprite(assets.image("""
        sonic_bark
    """), Doggy, 100, 0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(otherSprite2)
    Head_Scintist_Catacter_Sprite.set_position(Doggy.x + 0, Doggy.y - 0)
    if Doggy.y < otherSprite2.y:
        info.change_score_by(100)
    else:
        Health_Bar.value += -50
sprites.on_overlap(SpriteKind.player,
    SpriteKind.Head_Scientist_Catacter,
    on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    info.change_score_by(100)
    sprites.destroy(otherSprite3)
sprites.on_overlap(SpriteKind.player, SpriteKind.Coin100, on_on_overlap3)

def on_overlap_tile(sprite4, location):
    global current_level
    current_level += 1
    sprites.destroy_all_sprites_of_kind(SpriteKind.Apple_Food)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Bee)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Catacter)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Imperial_Catacater)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Head_Scientist_Catacter)
    sprites.destroy_all_sprites_of_kind(SpriteKind.teleporter_sender)
    sprites.destroy_all_sprites_of_kind(SpriteKind.telepoter_reciever)
    sprites.destroy_all_sprites_of_kind(SpriteKind.flowing_lava)
    sprites.destroy_all_sprites_of_kind(SpriteKind.still_lava)
    sprites.destroy_all_sprites_of_kind(SpriteKind.GoldenApple_Food)
    Start_Level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile)

def on_a_pressed():
    if Doggy.vy == 0:
        Doggy.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap4(sprite5, otherSprite4):
    Health_Bar.value += 10
    sprites.destroy(otherSprite4)
sprites.on_overlap(SpriteKind.player, SpriteKind.Apple_Food, on_on_overlap4)

def on_overlap_tile2(sprite6, location2):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        lava_still
    """),
    on_overlap_tile2)

def on_on_overlap5(sprite7, otherSprite5):
    sprites.destroy(sprite7)
    info.change_score_by(3)
sprites.on_overlap(SpriteKind.Catacter, SpriteKind.projectile, on_on_overlap5)

def on_overlap_tile3(sprite8, location3):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        lava_flowing
    """),
    on_overlap_tile3)

def on_on_overlap6(sprite9, otherSprite6):
    info.change_score_by(10)
    sprites.destroy(sprite9)
sprites.on_overlap(SpriteKind.Imperial_Catacater,
    SpriteKind.projectile,
    on_on_overlap6)

def on_overlap_tile4(sprite10, location4):
    global Coin2, Flower2, Catacter_Sprite, Coin10Var, Imperial_Catacter_Sprite, Coin1002, Apple, Head_Scintist_Catacter_Sprite, teleport_portal, teleport_portal_2, Golden_Apple
    if current_secret_level == 0:
        tiles.set_current_tilemap(tilemap("""
            level_1_secret
        """))
    elif current_secret_level == 1:
        tiles.set_current_tilemap(tilemap("""
            level_3_secret
        """))
    elif current_secret_level == 2:
        tiles.set_current_tilemap(tilemap("""
            level_3_secret
        """))
    elif current_secret_level == 3:
        tiles.set_current_tilemap(tilemap("""
            secret_level_4
        """))
    elif current_secret_level == 4:
        tiles.set_current_tilemap(tilemap("""
            secret_level_5
        """))
    elif current_secret_level == 5:
        tiles.set_current_tilemap(tilemap("""
            secret_level_0
        """))
    elif current_secret_level == 6:
        tiles.set_current_tilemap(tilemap("""
            secret_level_6
        """))
    elif current_secret_level == 7:
        tiles.set_current_tilemap(tilemap("""
            scam_secret_level
        """))
    else:
        pass
    tiles.place_on_random_tile(Doggy, assets.tile("""
        Spawn_Doggy
    """))
    for value142 in tiles.get_tiles_by_type(assets.tile("""
        Spawn_Doggy
    """)):
        tiles.set_tile_at(value142, assets.tile("""
            transparency16
        """))
    scene.camera_follow_sprite(Doggy)
    for value152 in sprites.all_of_kind(SpriteKind.Bee):
        sprites.destroy(value152)
    for value162 in sprites.all_of_kind(SpriteKind.Catacter):
        sprites.destroy(value162)
    for value172 in sprites.all_of_kind(SpriteKind.Coin):
        sprites.destroy(value172)
    for value182 in sprites.all_of_kind(SpriteKind.Coin10):
        sprites.destroy(value182)
    for value19 in sprites.all_of_kind(SpriteKind.Coin100):
        sprites.destroy(value19)
    for value20 in sprites.all_of_kind(SpriteKind.Flower):
        sprites.destroy(value20)
    for value21 in tiles.get_tiles_by_type(assets.tile("""
        Coin_Collectable
    """)):
        Coin2 = sprites.create(assets.image("""
            Coin_Actual
        """), SpriteKind.Coin)
        animation.run_image_animation(Coin2,
            assets.animation("""
                Coin_Animation
            """),
            500,
            True)
        tiles.place_on_tile(Coin2, value21)
        tiles.set_tile_at(value21, assets.tile("""
            transparency16
        """))
    for value22 in tiles.get_tiles_by_type(assets.tile("""
        Flower_Placeholder
    """)):
        Flower2 = sprites.create(assets.image("""
            Flower_1
        """), SpriteKind.Flower)
        tiles.place_on_tile(Flower2, value22)
        tiles.set_tile_at(value22, assets.tile("""
            transparency16
        """))
    for value23 in tiles.get_tiles_by_type(assets.tile("""
        Catacter_Tile
    """)):
        Catacter_Sprite = sprites.create(assets.image("""
            Catacter
        """), SpriteKind.Catacter)
        tiles.place_on_tile(Catacter_Sprite, value23)
        tiles.set_tile_at(value23, assets.tile("""
            transparency16
        """))
    for value24 in tiles.get_tiles_by_type(assets.tile("""
        10coin
    """)):
        Coin10Var = sprites.create(assets.image("""
            Coin_10
        """), SpriteKind.Coin10)
        tiles.place_on_tile(Coin10Var, value24)
        tiles.set_tile_at(value24, assets.tile("""
            transparency16
        """))
    for value25 in tiles.get_tiles_by_type(assets.tile("""
        Imperial_Catacater_Spawn
    """)):
        Imperial_Catacter_Sprite = sprites.create(assets.image("""
                Imperial_Catacter_Sprite
            """),
            SpriteKind.Imperial_Catacater)
        tiles.place_on_tile(Imperial_Catacter_Sprite, value25)
        tiles.set_tile_at(value25, assets.tile("""
            transparency16
        """))
    for value252 in tiles.get_tiles_by_type(assets.tile("""
        Coin100
    """)):
        Coin1002 = sprites.create(assets.image("""
            Coin_100
        """), SpriteKind.Coin100)
        tiles.place_on_tile(Coin1002, value252)
        tiles.set_tile_at(value252, assets.tile("""
            transparency16
        """))
    for value26 in tiles.get_tiles_by_type(assets.tile("""
        apple_foodtile
    """)):
        Apple = sprites.create(assets.image("""
            apple_food
        """), SpriteKind.Apple_Food)
        tiles.place_on_tile(Apple, value26)
        tiles.set_tile_at(value26, assets.tile("""
            transparency16
        """))
    for value27 in tiles.get_tiles_by_type(assets.tile("""
        head_scientist_catacter
    """)):
        Head_Scintist_Catacter_Sprite = sprites.create(assets.image("""
                Head_Scientist_Catacter_Sprite
            """),
            SpriteKind.Head_Scientist_Catacter)
        tiles.place_on_tile(Head_Scintist_Catacter_Sprite, value27)
        tiles.set_tile_at(value27, assets.tile("""
            transparency16
        """))
    for value28 in tiles.get_tiles_by_type(assets.tile("""
        teleport_tile_sender
    """)):
        teleport_portal = sprites.create(assets.image("""
                teleport_portal
            """),
            SpriteKind.teleporter_sender)
        tiles.place_on_tile(teleport_portal, value28)
        tiles.set_tile_at(value28, assets.tile("""
            transparency16
        """))
    for value29 in tiles.get_tiles_by_type(assets.tile("""
        teleporter_tile_receiver
    """)):
        teleport_portal_2 = sprites.create(assets.image("""
                teleport_portal_2
            """),
            SpriteKind.telepoter_reciever)
        tiles.place_on_tile(teleport_portal_2, value29)
        tiles.set_tile_at(value29, assets.tile("""
            transparency16
        """))
    for value30 in tiles.get_tiles_by_type(assets.tile("""
        GOLDEN_APPLE_FOOD
    """)):
        Golden_Apple = sprites.create(assets.image("""
                goldenapple_food
            """),
            SpriteKind.GoldenApple_Food)
        tiles.place_on_tile(Golden_Apple, value30)
        tiles.set_tile_at(value30, assets.tile("""
            transparency16
        """))
    sprites.destroy_all_sprites_of_kind(SpriteKind.Apple_Food)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Bee)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Catacter)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Imperial_Catacater)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Head_Scientist_Catacter)
    sprites.destroy_all_sprites_of_kind(SpriteKind.teleporter_sender)
    sprites.destroy_all_sprites_of_kind(SpriteKind.telepoter_reciever)
    sprites.destroy_all_sprites_of_kind(SpriteKind.flowing_lava)
    sprites.destroy_all_sprites_of_kind(SpriteKind.still_lava)
    sprites.destroy_all_sprites_of_kind(SpriteKind.GoldenApple_Food)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        secret_level_flag
    """),
    on_overlap_tile4)

def on_on_overlap7(sprite11, otherSprite7):
    info.change_score_by(10)
    sprites.destroy(otherSprite7)
sprites.on_overlap(SpriteKind.player, SpriteKind.Coin10, on_on_overlap7)

def on_on_overlap8(sprite12, otherSprite8):
    bee_health.value += -25
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.Bee, SpriteKind.projectile, on_on_overlap8)

def on_on_overlap9(sprite13, otherSprite9):
    global Bee2, bee_health
    sprites.destroy(otherSprite9)
    Bee2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Bee)
    bee_health = statusbars.create(20, 4, StatusBarKind.enemy_health)
    bee_health.value = 50
    bee_health.attach_to_sprite(Bee2)
    animation.run_image_animation(Bee2,
        assets.animation("""
            Bee_EnemyAnamation
        """),
        100,
        True)
    Bee2.set_position(Doggy.x + 80, Doggy.y - 80)
    Bee2.follow(Doggy)
sprites.on_overlap(SpriteKind.player, SpriteKind.Flower, on_on_overlap9)

def on_on_overlap10(sprite14, otherSprite10):
    sprites.destroy(otherSprite10)
    Imperial_Catacter_Sprite.set_position(Doggy.x + 0, Doggy.y - 0)
    if Doggy.y < otherSprite10.y:
        info.change_score_by(15)
    else:
        Health_Bar.value += -20
sprites.on_overlap(SpriteKind.player,
    SpriteKind.Imperial_Catacater,
    on_on_overlap10)

def on_on_overlap11(sprite15, otherSprite11):
    Doggy.set_position(teleport_portal_2.x, teleport_portal_2.y)
    sprites.destroy(otherSprite11)
sprites.on_overlap(SpriteKind.player,
    SpriteKind.teleporter_sender,
    on_on_overlap11)

def on_on_overlap12(sprite16, otherSprite12):
    Health_Bar.value += 50
    sprites.destroy(otherSprite12)
    scaling.scale_by_pixels(Doggy, 5, ScaleDirection.HORIZONTALLY, ScaleAnchor.MIDDLE)
    scaling.scale_by_pixels(Doggy, 5, ScaleDirection.VERTICALLY, ScaleAnchor.MIDDLE)
sprites.on_overlap(SpriteKind.player,
    SpriteKind.GoldenApple_Food,
    on_on_overlap12)

def on_on_overlap13(sprite17, otherSprite13):
    sprites.destroy(sprite17)
    info.change_score_by(25)
sprites.on_overlap(SpriteKind.Head_Scientist_Catacter,
    SpriteKind.projectile,
    on_on_overlap13)

def on_on_overlap14(sprite18, otherSprite14):
    sprites.destroy(otherSprite14)
    Catacter_Sprite.set_position(Doggy.x + 0, Doggy.y - 0)
    if Doggy.y < otherSprite14.y:
        info.change_score_by(5)
    else:
        Health_Bar.value += -10
sprites.on_overlap(SpriteKind.player, SpriteKind.Catacter, on_on_overlap14)

def on_on_overlap15(sprite19, otherSprite15):
    bee_health.value += -45
    if Doggy.y < otherSprite15.y:
        info.change_score_by(3)
    else:
        Health_Bar.value += -5
    if bee_health.value == 0:
        sprites.destroy(otherSprite15)
sprites.on_overlap(SpriteKind.player, SpriteKind.Bee, on_on_overlap15)

Bee2: Sprite = None
bee_health: StatusBarSprite = None
current_secret_level = 0
sonic_bark: Sprite = None
teleport_portal_2: Sprite = None
teleport_portal: Sprite = None
Head_Scintist_Catacter_Sprite: Sprite = None
Imperial_Catacter_Sprite: Sprite = None
Golden_Apple: Sprite = None
Apple: Sprite = None
Coin1002: Sprite = None
Coin10Var: Sprite = None
Flower2: Sprite = None
Coin2: Sprite = None
Catacter_Sprite: Sprite = None
Health_Bar: StatusBarSprite = None
Doggy: Sprite = None
current_level = 0
game.set_dialog_frame(assets.image("""
    bruh_man_chat_bubble
"""))
game.show_long_text("DOGGY! GET BACK HERE!", DialogLayout.FULL)
current_level = 0
Doggy = sprites.create(assets.image("""
    Doggy
"""), SpriteKind.player)
Health_Bar = statusbars.create(20, 4, StatusBarKind.health)
Health_Bar.value = 100
info.set_life(3)
controller.move_sprite(Doggy, 100, 0)
Doggy.set_bounce_on_wall(False)
Start_Level()
Catacter_Sprite.follow(Doggy)

def on_on_update():
    Doggy.set_image(assets.image("""
        Doggy
    """))
    if Doggy.vy < 0:
        Doggy.set_image(assets.image("""
            Doggy_Jump
        """))
    elif Doggy.vy > 0:
        Doggy.set_image(assets.image("""
            Doggy_Fall
        """))
    else:
        pass
    if (Doggy.is_hitting_tile(CollisionDirection.LEFT) or Doggy.is_hitting_tile(CollisionDirection.RIGHT)) and Doggy.vy >= 0:
        Doggy.vy = 0
        Doggy.ay = 0
        Doggy.set_image(assets.image("""
            Doggy_Climb
        """))
    else:
        Doggy.ay = 350
    if Doggy.vx < 0 or Doggy.is_hitting_tile(CollisionDirection.LEFT):
        Doggy.image.flip_x()
        Doggy.set_image(Doggy.image)
game.on_update(on_on_update)

def on_forever():
    music.play(music.create_song(hex("""
            0078000408020600001c00010a006400f4016400000400000000000000000000000000050000040c0000000400012a04000800012701001c000f05001202c102c20100040500280000006400280003140006020004120000000400012504000800012408000c00012205001c000f0a006400f4010a00000400000000000000000000000000000000020c000000040001200c001000011e06001c00010a006400f4016400000400000000000000000000000000000000020c0020002400012924002800012908001c000e050046006603320000040a002d00000064001400013200020100021c000c001000012a14001800041d2024272000240002242524002800012409010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80006000c000d000108
        """)),
        music.PlaybackMode.UNTIL_DONE)
    if current_level == 0:
        scene.set_background_image(assets.image("""
            Sky_1
        """))
    elif current_level == 1:
        scene.set_background_image(assets.image("""
            Sky_2
        """))
    elif current_level == 2:
        scene.set_background_image(assets.image("""
            Sky_3
        """))
    elif current_level == 3:
        scene.set_background_image(assets.image("""
            Sky_4
        """))
    elif current_level == 4:
        scene.set_background_image(assets.image("""
            Sky_5
        """))
    elif current_level == 5:
        scene.set_background_image(assets.image("""
            Sky_1
        """))
    elif current_level == 6:
        scene.set_background_image(assets.image("""
            Sky_1
        """))
    elif current_level == 7:
        scene.set_background_image(assets.image("""
            Sky_1
        """))
    elif current_level == 8:
        scene.set_background_image(assets.image("""
            Background_Level_9
        """))
    else:
        scene.set_background_image(assets.image("""
            Backround_Level_8
        """))
forever(on_forever)

def on_forever2():
    music.play(music.create_song(assets.song("""
            Doggy_World_Music
        """)),
        music.PlaybackMode.UNTIL_DONE)
    if current_secret_level == 0:
        scene.set_background_image(img("""
            ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
        """))
forever(on_forever2)

def on_forever3():
    if info.life() == 0:
        game.game_over(False)
        game.set_game_over_effect(False, effects.melt)
        game.set_game_over_message(False, "GAME OVER!")
forever(on_forever3)

def on_forever4():
    Health_Bar.attach_to_sprite(Doggy)
    if Health_Bar.value == 0:
        info.change_life_by(-1)
        if info.life() == 0:
            game.game_over(False)
            game.set_game_over_message(False, "GAME OVER!")
forever(on_forever4)

def on_forever5():
    global current_secret_level
    current_secret_level = current_level
forever(on_forever5)
