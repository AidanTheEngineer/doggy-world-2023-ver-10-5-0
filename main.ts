namespace SpriteKind {
    export const Coin = SpriteKind.create()
    export const Flower = SpriteKind.create()
    export const Coin10 = SpriteKind.create()
    export const Coin100 = SpriteKind.create()
    export const Bee = SpriteKind.create()
    export const Catacter = SpriteKind.create()
    export const Apple_Food = SpriteKind.create()
    export const doggyemeraldcoin = SpriteKind.create()
    export const GoldenApple_Food = SpriteKind.create()
    export const Imperial_Catacater = SpriteKind.create()
    export const Head_Scientist_Catacter = SpriteKind.create()
    export const teleporter_sender = SpriteKind.create()
    export const telepoter_reciever = SpriteKind.create()
    export const flowing_lava = SpriteKind.create()
    export const still_lava = SpriteKind.create()
    export const Caution_Sign = SpriteKind.create()
    export const Water = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite4, location) {
    Doggy.ax = 0
    Doggy.ay = 0
    current_level += 1
    sprites.destroyAllSpritesOfKind(SpriteKind.Apple_Food)
    sprites.destroyAllSpritesOfKind(SpriteKind.Bee)
    sprites.destroyAllSpritesOfKind(SpriteKind.Catacter)
    sprites.destroyAllSpritesOfKind(SpriteKind.Imperial_Catacater)
    sprites.destroyAllSpritesOfKind(SpriteKind.Head_Scientist_Catacter)
    sprites.destroyAllSpritesOfKind(SpriteKind.teleporter_sender)
    sprites.destroyAllSpritesOfKind(SpriteKind.telepoter_reciever)
    sprites.destroyAllSpritesOfKind(SpriteKind.flowing_lava)
    sprites.destroyAllSpritesOfKind(SpriteKind.still_lava)
    sprites.destroyAllSpritesOfKind(SpriteKind.GoldenApple_Food)
    sprites.destroyAllSpritesOfKind(SpriteKind.Caution_Sign)
    sprites.destroyAllSpritesOfKind(SpriteKind.Water)
    Start_Level()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`lava_still`, function (sprite6, location2) {
    info.changeLifeBy(-1)
})
function Start_Level () {
    if (current_level == 1) {
        tiles.setCurrentTilemap(tilemap`level1`)
    } else if (current_level == 2) {
        game.splash("Level 2 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level_2`)
        Health_Bar.value = 110
        Health_Bar.max = 110
    } else if (current_level == 3) {
        game.splash("Level 3 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level_3`)
        Health_Bar.value = 120
        Health_Bar.max = 120
    } else if (current_level == 4) {
        game.splash("Level 4 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level_4true`)
        Health_Bar.value = 130
        Health_Bar.max = 130
    } else if (current_level == 5) {
        game.splash("Level 5 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level_5`)
        Health_Bar.value = 140
        Health_Bar.max = 140
    } else if (current_level == 6) {
        game.splash("Level 6 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level_6`)
        Health_Bar.value = 150
        Health_Bar.max = 150
    } else if (current_level == 7) {
        game.splash("Level 7 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level_7`)
        Health_Bar.value = 160
        Health_Bar.max = 160
    } else if (current_level == 8) {
        game.splash("Level 8 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level_8`)
        Health_Bar.value = 170
        Health_Bar.max = 170
    } else if (current_level == 9) {
        game.splash("Level 9 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level27`)
        Health_Bar.value = 180
        Health_Bar.max = 180
    } else if (current_level == 10) {
        game.splash("Level 10 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level_9`)
        Health_Bar.value = 190
        Health_Bar.max = 190
    } else if (current_level == 11) {
        game.splash("Level 11 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level_10`)
        Health_Bar.value = 200
        Health_Bar.max = 200
    } else if (current_level == 12) {
        game.splash("Level 12 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level_0`)
        Health_Bar.value = 210
        Health_Bar.max = 210
    } else if (current_level == 13) {
        game.splash("Level 13 Unlocked!")
        tiles.setCurrentTilemap(tilemap`level49`)
        Health_Bar.value = 210
        Health_Bar.max = 210
    } else {
        game.gameOver(true)
        game.setGameOverMessage(true, "ROOF! ROOF! GOOD JOB!")
        game.setGameOverMessage(true, "Remember you can go to the Offical Site For Records")
    }
    tiles.placeOnRandomTile(Doggy, assets.tile`Spawn_Doggy`)
    for (let value of tiles.getTilesByType(assets.tile`Spawn_Doggy`)) {
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
    scene.cameraFollowSprite(Doggy)
    for (let value2 of sprites.allOfKind(SpriteKind.Bee)) {
        sprites.destroy(value2)
    }
    for (let value3 of sprites.allOfKind(SpriteKind.Catacter)) {
        sprites.destroy(value3)
    }
    for (let value4 of sprites.allOfKind(SpriteKind.Coin)) {
        sprites.destroy(value4)
    }
    for (let value5 of sprites.allOfKind(SpriteKind.Coin10)) {
        sprites.destroy(value5)
    }
    for (let value6 of sprites.allOfKind(SpriteKind.Coin100)) {
        sprites.destroy(value6)
    }
    for (let value7 of sprites.allOfKind(SpriteKind.Flower)) {
        sprites.destroy(value7)
    }
    for (let value8 of tiles.getTilesByType(assets.tile`Coin_Collectable`)) {
        Coin2 = sprites.create(assets.image`Coin_Actual`, SpriteKind.Coin)
        animation.runImageAnimation(
        Coin2,
        assets.animation`Coin_Animation`,
        500,
        true
        )
        tiles.placeOnTile(Coin2, value8)
        tiles.setTileAt(value8, assets.tile`transparency16`)
    }
    for (let value9 of tiles.getTilesByType(assets.tile`Flower_Placeholder`)) {
        Flower2 = sprites.create(assets.image`Flower_1`, SpriteKind.Flower)
        tiles.placeOnTile(Flower2, value9)
        tiles.setTileAt(value9, assets.tile`transparency16`)
    }
    for (let value10 of tiles.getTilesByType(assets.tile`Catacter_Tile`)) {
        Catacter_Sprite = sprites.create(assets.image`Catacter`, SpriteKind.Catacter)
        tiles.placeOnTile(Catacter_Sprite, value10)
        tiles.setTileAt(value10, assets.tile`transparency16`)
    }
    for (let value11 of tiles.getTilesByType(assets.tile`10coin`)) {
        Coin10Var = sprites.create(assets.image`Coin_10`, SpriteKind.Coin10)
        tiles.placeOnTile(Coin10Var, value11)
        tiles.setTileAt(value11, assets.tile`transparency16`)
    }
    for (let value12 of tiles.getTilesByType(assets.tile`Coin100`)) {
        Coin1002 = sprites.create(assets.image`Coin_100`, SpriteKind.Coin100)
        tiles.placeOnTile(Coin1002, value12)
        tiles.setTileAt(value12, assets.tile`transparency16`)
    }
    for (let value13 of tiles.getTilesByType(assets.tile`apple_foodtile`)) {
        Apple = sprites.create(assets.image`apple_food`, SpriteKind.Apple_Food)
        tiles.placeOnTile(Apple, value13)
        tiles.setTileAt(value13, assets.tile`transparency16`)
    }
    for (let value14 of tiles.getTilesByType(assets.tile`GOLDEN_APPLE_FOOD`)) {
        Golden_Apple = sprites.create(assets.image`goldenapple_food`, SpriteKind.GoldenApple_Food)
        tiles.placeOnTile(Golden_Apple, value14)
        tiles.setTileAt(value14, assets.tile`transparency16`)
    }
    for (let value15 of tiles.getTilesByType(assets.tile`Imperial_Catacater_Spawn`)) {
        Imperial_Catacter_Sprite = sprites.create(assets.image`Imperial_Catacter_Sprite`, SpriteKind.Imperial_Catacater)
        tiles.placeOnTile(Imperial_Catacter_Sprite, value15)
        tiles.setTileAt(value15, assets.tile`transparency16`)
    }
    for (let value16 of tiles.getTilesByType(assets.tile`head_scientist_catacter`)) {
        Head_Scintist_Catacter_Sprite = sprites.create(assets.image`Head_Scientist_Catacter_Sprite`, SpriteKind.Head_Scientist_Catacter)
        tiles.placeOnTile(Head_Scintist_Catacter_Sprite, value16)
        tiles.setTileAt(value16, assets.tile`transparency16`)
    }
    for (let value17 of tiles.getTilesByType(assets.tile`teleport_tile_sender`)) {
        teleport_portal = sprites.create(assets.image`teleport_portal`, SpriteKind.teleporter_sender)
        tiles.placeOnTile(teleport_portal, value17)
        tiles.setTileAt(value17, assets.tile`transparency16`)
    }
    for (let value18 of tiles.getTilesByType(assets.tile`teleporter_tile_receiver`)) {
        teleport_portal_2 = sprites.create(assets.image`teleport_portal_2`, SpriteKind.telepoter_reciever)
        tiles.placeOnTile(teleport_portal_2, value18)
        tiles.setTileAt(value18, assets.tile`transparency16`)
    }
    for (let value of tiles.getTilesByType(assets.tile`CAUTION_BLOCK`)) {
        CAUTION_SIGN = sprites.create(assets.image`Caution_Sign_Sprite`, SpriteKind.Caution_Sign)
        tiles.placeOnTile(CAUTION_SIGN, value)
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
    for (let value of tiles.getTilesByType(assets.tile`water`)) {
        Water = sprites.create(assets.image`water_normal`, SpriteKind.Water)
        tiles.placeOnTile(Water, value)
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Coin, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    sprites.destroy(otherSprite)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    sonic_bark = sprites.createProjectileFromSprite(assets.image`sonic_bark`, Doggy, 100, 0)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Doggy.vy == 0) {
        Doggy.vy = -150
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.teleporter_sender, function (sprite15, otherSprite11) {
    Doggy.setPosition(teleport_portal_2.x, teleport_portal_2.y)
    sprites.destroy(otherSprite11)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Bee, function (sprite19, otherSprite15) {
    bee_health.value += -45
    if (Doggy.y < otherSprite15.y) {
        info.changeScoreBy(3)
    } else {
        Health_Bar.value += -5
    }
    if (bee_health.value == 0) {
        sprites.destroy(otherSprite15)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`secret_level_flag`, function (sprite10, location4) {
    if (current_secret_level == 0) {
        tiles.setCurrentTilemap(tilemap`level_1_secret`)
    } else if (current_secret_level == 1) {
        tiles.setCurrentTilemap(tilemap`level_3_secret`)
    } else if (current_secret_level == 2) {
        tiles.setCurrentTilemap(tilemap`level_3_secret`)
    } else if (current_secret_level == 3) {
        tiles.setCurrentTilemap(tilemap`secret_level_4`)
    } else if (current_secret_level == 4) {
        tiles.setCurrentTilemap(tilemap`secret_level_5`)
    } else if (current_secret_level == 5) {
        tiles.setCurrentTilemap(tilemap`secret_level_0`)
    } else if (current_secret_level == 6) {
        tiles.setCurrentTilemap(tilemap`secret_level_6`)
    } else if (current_secret_level == 7) {
        tiles.setCurrentTilemap(tilemap`scam_secret_level`)
    } else {
    	
    }
    tiles.placeOnRandomTile(Doggy, assets.tile`Spawn_Doggy`)
    for (let value142 of tiles.getTilesByType(assets.tile`Spawn_Doggy`)) {
        tiles.setTileAt(value142, assets.tile`transparency16`)
    }
    scene.cameraFollowSprite(Doggy)
    for (let value152 of sprites.allOfKind(SpriteKind.Bee)) {
        sprites.destroy(value152)
    }
    for (let value162 of sprites.allOfKind(SpriteKind.Catacter)) {
        sprites.destroy(value162)
    }
    for (let value172 of sprites.allOfKind(SpriteKind.Coin)) {
        sprites.destroy(value172)
    }
    for (let value182 of sprites.allOfKind(SpriteKind.Coin10)) {
        sprites.destroy(value182)
    }
    for (let value19 of sprites.allOfKind(SpriteKind.Coin100)) {
        sprites.destroy(value19)
    }
    for (let value20 of sprites.allOfKind(SpriteKind.Flower)) {
        sprites.destroy(value20)
    }
    for (let value21 of tiles.getTilesByType(assets.tile`Coin_Collectable`)) {
        Coin2 = sprites.create(assets.image`Coin_Actual`, SpriteKind.Coin)
        animation.runImageAnimation(
        Coin2,
        assets.animation`Coin_Animation`,
        500,
        true
        )
        tiles.placeOnTile(Coin2, value21)
        tiles.setTileAt(value21, assets.tile`transparency16`)
    }
    for (let value22 of tiles.getTilesByType(assets.tile`Flower_Placeholder`)) {
        Flower2 = sprites.create(assets.image`Flower_1`, SpriteKind.Flower)
        tiles.placeOnTile(Flower2, value22)
        tiles.setTileAt(value22, assets.tile`transparency16`)
    }
    for (let value23 of tiles.getTilesByType(assets.tile`Catacter_Tile`)) {
        Catacter_Sprite = sprites.create(assets.image`Catacter`, SpriteKind.Catacter)
        tiles.placeOnTile(Catacter_Sprite, value23)
        tiles.setTileAt(value23, assets.tile`transparency16`)
    }
    for (let value24 of tiles.getTilesByType(assets.tile`10coin`)) {
        Coin10Var = sprites.create(assets.image`Coin_10`, SpriteKind.Coin10)
        tiles.placeOnTile(Coin10Var, value24)
        tiles.setTileAt(value24, assets.tile`transparency16`)
    }
    for (let value25 of tiles.getTilesByType(assets.tile`Imperial_Catacater_Spawn`)) {
        Imperial_Catacter_Sprite = sprites.create(assets.image`Imperial_Catacter_Sprite`, SpriteKind.Imperial_Catacater)
        tiles.placeOnTile(Imperial_Catacter_Sprite, value25)
        tiles.setTileAt(value25, assets.tile`transparency16`)
    }
    for (let value252 of tiles.getTilesByType(assets.tile`Coin100`)) {
        Coin1002 = sprites.create(assets.image`Coin_100`, SpriteKind.Coin100)
        tiles.placeOnTile(Coin1002, value252)
        tiles.setTileAt(value252, assets.tile`transparency16`)
    }
    for (let value26 of tiles.getTilesByType(assets.tile`apple_foodtile`)) {
        Apple = sprites.create(assets.image`apple_food`, SpriteKind.Apple_Food)
        tiles.placeOnTile(Apple, value26)
        tiles.setTileAt(value26, assets.tile`transparency16`)
    }
    for (let value27 of tiles.getTilesByType(assets.tile`head_scientist_catacter`)) {
        Head_Scintist_Catacter_Sprite = sprites.create(assets.image`Head_Scientist_Catacter_Sprite`, SpriteKind.Head_Scientist_Catacter)
        tiles.placeOnTile(Head_Scintist_Catacter_Sprite, value27)
        tiles.setTileAt(value27, assets.tile`transparency16`)
    }
    for (let value28 of tiles.getTilesByType(assets.tile`teleport_tile_sender`)) {
        teleport_portal = sprites.create(assets.image`teleport_portal`, SpriteKind.teleporter_sender)
        tiles.placeOnTile(teleport_portal, value28)
        tiles.setTileAt(value28, assets.tile`transparency16`)
    }
    for (let value29 of tiles.getTilesByType(assets.tile`teleporter_tile_receiver`)) {
        teleport_portal_2 = sprites.create(assets.image`teleport_portal_2`, SpriteKind.telepoter_reciever)
        tiles.placeOnTile(teleport_portal_2, value29)
        tiles.setTileAt(value29, assets.tile`transparency16`)
    }
    for (let value30 of tiles.getTilesByType(assets.tile`GOLDEN_APPLE_FOOD`)) {
        Golden_Apple = sprites.create(assets.image`goldenapple_food`, SpriteKind.GoldenApple_Food)
        tiles.placeOnTile(Golden_Apple, value30)
        tiles.setTileAt(value30, assets.tile`transparency16`)
    }
    for (let value of tiles.getTilesByType(assets.tile`CAUTION_BLOCK`)) {
        CAUTION_SIGN = sprites.create(assets.image`Caution_Sign_Sprite`, SpriteKind.Player)
        tiles.placeOnTile(CAUTION_SIGN, value)
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
    for (let value of tiles.getTilesByType(assets.tile`water`)) {
        Water = sprites.create(assets.image`water_normal`, SpriteKind.Water)
        tiles.placeOnTile(Water, value)
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
    sprites.destroyAllSpritesOfKind(SpriteKind.Apple_Food)
    sprites.destroyAllSpritesOfKind(SpriteKind.Bee)
    sprites.destroyAllSpritesOfKind(SpriteKind.Catacter)
    sprites.destroyAllSpritesOfKind(SpriteKind.Imperial_Catacater)
    sprites.destroyAllSpritesOfKind(SpriteKind.Head_Scientist_Catacter)
    sprites.destroyAllSpritesOfKind(SpriteKind.teleporter_sender)
    sprites.destroyAllSpritesOfKind(SpriteKind.telepoter_reciever)
    sprites.destroyAllSpritesOfKind(SpriteKind.flowing_lava)
    sprites.destroyAllSpritesOfKind(SpriteKind.still_lava)
    sprites.destroyAllSpritesOfKind(SpriteKind.GoldenApple_Food)
    sprites.destroyAllSpritesOfKind(SpriteKind.Caution_Sign)
    sprites.destroyAllSpritesOfKind(SpriteKind.Water)
})
sprites.onOverlap(SpriteKind.Catacter, SpriteKind.Projectile, function (sprite7, otherSprite5) {
    sprites.destroy(sprite7)
    info.changeScoreBy(3)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Apple_Food, function (sprite, otherSprite) {
    Health_Bar.value += 10
    sprites.destroy(otherSprite)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Imperial_Catacater, function (sprite14, otherSprite10) {
    sprites.destroy(otherSprite10)
    Imperial_Catacter_Sprite.setPosition(Doggy.x + 0, Doggy.y - 0)
    if (Doggy.y < otherSprite10.y) {
        info.changeScoreBy(15)
    } else {
        Health_Bar.value += -20
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Coin10, function (sprite11, otherSprite7) {
    info.changeScoreBy(10)
    sprites.destroy(otherSprite7)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Caution_Sign, function (sprite, otherSprite) {
    game.splash("CAUTION!")
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Catacter, function (sprite18, otherSprite14) {
    sprites.destroy(otherSprite14)
    Catacter_Sprite.setPosition(Doggy.x + 0, Doggy.y - 0)
    if (Doggy.y < otherSprite14.y) {
        info.changeScoreBy(5)
    } else {
        Health_Bar.value += -10
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`lava_flowing`, function (sprite8, location3) {
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Bee, SpriteKind.Projectile, function (sprite12, otherSprite8) {
    bee_health.value += -25
    info.changeScoreBy(0)
})
sprites.onOverlap(SpriteKind.Head_Scientist_Catacter, SpriteKind.Projectile, function (sprite17, otherSprite13) {
    sprites.destroy(sprite17)
    info.changeScoreBy(25)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Head_Scientist_Catacter, function (sprite2, otherSprite2) {
    sprites.destroy(otherSprite2)
    Head_Scintist_Catacter_Sprite.setPosition(Doggy.x + 0, Doggy.y - 0)
    if (Doggy.y < otherSprite2.y) {
        info.changeScoreBy(100)
    } else {
        Health_Bar.value += -50
    }
})
sprites.onOverlap(SpriteKind.Imperial_Catacater, SpriteKind.Projectile, function (sprite9, otherSprite6) {
    info.changeScoreBy(10)
    sprites.destroy(sprite9)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Coin100, function (sprite3, otherSprite3) {
    info.changeScoreBy(100)
    sprites.destroy(otherSprite3)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.teleporter_sender, function (sprite15, otherSprite11) {
    Doggy.setPosition(teleport_portal_2.x, teleport_portal_2.y)
    sprites.destroy(otherSprite11)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.GoldenApple_Food, function (sprite16, otherSprite12) {
    Health_Bar.value += 50
    sprites.destroy(otherSprite12)
    scaling.scaleByPixels(Doggy, 5, ScaleDirection.Horizontally, ScaleAnchor.Middle)
    scaling.scaleByPixels(Doggy, 5, ScaleDirection.Vertically, ScaleAnchor.Middle)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Apple_Food, function (sprite5, otherSprite4) {
    Health_Bar.value += 10
    sprites.destroy(otherSprite4)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Flower, function (sprite13, otherSprite9) {
    sprites.destroy(otherSprite9)
    Bee2 = sprites.create(img`
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
        `, SpriteKind.Bee)
    bee_health = statusbars.create(20, 4, StatusBarKind.EnemyHealth)
    bee_health.value = 50
    bee_health.attachToSprite(Bee2)
    animation.runImageAnimation(
    Bee2,
    assets.animation`Bee_EnemyAnamation`,
    100,
    true
    )
    Bee2.setPosition(Doggy.x + 80, Doggy.y - 80)
    Bee2.follow(Doggy)
})
let Bee2: Sprite = null
let current_secret_level = 0
let bee_health: StatusBarSprite = null
let sonic_bark: Sprite = null
let Water: Sprite = null
let CAUTION_SIGN: Sprite = null
let teleport_portal_2: Sprite = null
let teleport_portal: Sprite = null
let Head_Scintist_Catacter_Sprite: Sprite = null
let Imperial_Catacter_Sprite: Sprite = null
let Golden_Apple: Sprite = null
let Apple: Sprite = null
let Coin1002: Sprite = null
let Coin10Var: Sprite = null
let Flower2: Sprite = null
let Coin2: Sprite = null
let Catacter_Sprite: Sprite = null
let Health_Bar: StatusBarSprite = null
let Doggy: Sprite = null
let current_level = 0
class ActionKind {
    static Walking: number
    private ___Walking_is_set: boolean
    private ___Walking: number
    get Walking(): number {
        return this.___Walking_is_set ? this.___Walking : ActionKind.Walking
    }
    set Walking(value: number) {
        this.___Walking_is_set = true
        this.___Walking = value
    }
    
    static Idle: number
    private ___Idle_is_set: boolean
    private ___Idle: number
    get Idle(): number {
        return this.___Idle_is_set ? this.___Idle : ActionKind.Idle
    }
    set Idle(value: number) {
        this.___Idle_is_set = true
        this.___Idle = value
    }
    
    static Jumping: number
    private ___Jumping_is_set: boolean
    private ___Jumping: number
    get Jumping(): number {
        return this.___Jumping_is_set ? this.___Jumping : ActionKind.Jumping
    }
    set Jumping(value: number) {
        this.___Jumping_is_set = true
        this.___Jumping = value
    }
    
    public static __initActionKind() {
        ActionKind.Walking = 0
        ActionKind.Idle = 1
        ActionKind.Jumping = 2
    }
    
}
ActionKind.__initActionKind()
game.setDialogFrame(assets.image`bruh_man_chat_bubble`)
game.showLongText("DOGGY! GET BACK HERE!", DialogLayout.Full)
current_level = 1
Doggy = sprites.create(assets.image`Doggy`, SpriteKind.Player)
Health_Bar = statusbars.create(20, 4, StatusBarKind.Health)
Health_Bar.value = 100
info.setLife(3)
controller.moveSprite(Doggy, 100, 0)
Doggy.setBounceOnWall(false)
Start_Level()
Catacter_Sprite.follow(Doggy)
game.onUpdate(function () {
    Doggy.setImage(assets.image`Doggy`)
    if (Doggy.vy < 0) {
        Doggy.setImage(assets.image`Doggy_Jump`)
    } else if (Doggy.vy > 0) {
        Doggy.setImage(assets.image`Doggy_Fall`)
    } else {
    	
    }
    if ((Doggy.isHittingTile(CollisionDirection.Left) || Doggy.isHittingTile(CollisionDirection.Right)) && Doggy.vy >= 0) {
        Doggy.vy = 0
        Doggy.ay = 0
        Doggy.setImage(assets.image`Doggy_Climb`)
    } else {
        Doggy.ay = 350
    }
    if (Doggy.vx < 0 || Doggy.isHittingTile(CollisionDirection.Left)) {
        Doggy.image.flipX()
        Doggy.setImage(Doggy.image)
    }
})
forever(function () {
    if (current_level == 1) {
        scene.setBackgroundImage(assets.image`Sky_1`)
    } else if (current_level == 2) {
        scene.setBackgroundImage(assets.image`Sky_2`)
    } else if (current_level == 3) {
        scene.setBackgroundImage(assets.image`Sky_3`)
    } else if (false) {
        scene.setBackgroundImage(assets.image`Sky_4`)
    } else if (current_level == 4) {
        scene.setBackgroundImage(assets.image`Sky_5`)
    } else if (current_level == 5) {
        scene.setBackgroundImage(assets.image`Sky_1`)
    } else if (current_level == 6) {
        scene.setBackgroundImage(assets.image`Sky_1`)
    } else if (current_level == 7) {
        scene.setBackgroundImage(assets.image`Sky_1`)
    } else if (current_level == 8) {
        scene.setBackgroundImage(assets.image`Background_Level_9`)
    } else if (current_level == 9) {
        scene.setBackgroundImage(assets.image`Backround_Level_8`)
    } else {
        scene.setBackgroundImage(assets.image`backround_10`)
    }
})
forever(function () {
    if (current_level == 1) {
        music.play(music.createSong(assets.song`Doggy World OST - WELCOME TO DOGGY WORLD`), music.PlaybackMode.UntilDone)
    }
    if (current_level == 2) {
        music.play(music.createSong(assets.song`Doggy World OST - TIDAL WAVES`), music.PlaybackMode.UntilDone)
    }
    if (current_level == 3) {
        music.play(music.createSong(assets.song`Doggy World OST - TOWER EXTREME`), music.PlaybackMode.UntilDone)
    }
    if (current_level == 4) {
        music.play(music.createSong(assets.song`Doggy World OST - Escape From Sanctuary`), music.PlaybackMode.UntilDone)
    }
    if (current_level == 5) {
        music.play(music.createSong(assets.song`Doggy World OST - WELCOME TO DOGGY WORLD0`), music.PlaybackMode.UntilDone)
    }
    if (current_level == 6) {
        music.play(music.createSong(assets.song`Doggy World OST - CATACTER TOWER`), music.PlaybackMode.UntilDone)
    }
})
forever(function () {
    if (info.life() == 0) {
        game.gameOver(false)
        game.setGameOverEffect(false, effects.melt)
        game.setGameOverMessage(false, "GAME OVER!")
    }
})
forever(function () {
    Health_Bar.attachToSprite(Doggy)
    if (Health_Bar.value == 0) {
        info.changeLifeBy(-1)
        if (info.life() == 0) {
            game.gameOver(false)
            game.setGameOverMessage(false, "GAME OVER!")
        }
    }
})
forever(function () {
    current_secret_level = current_level
})
