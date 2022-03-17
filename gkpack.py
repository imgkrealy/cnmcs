packName = "聆听万物资源包dome"#在此修改附加包的名字(游戏内显示)
#allDict为未收录的语言库(例如其他组件的生物)
#eTypehartDict为攻击生物的语言库
#eTypeapDict为玩家靠近生物的语言库
#blockDestroyDict为破坏方块的语言库
#blockPlaceDict为放置方块的语言库
#所有语言库均可自行扩展(namespace:id)

allDict = {
    ["",""]
}
eTypehartDict = {
    "bat":[#蝙蝠

    ],
    "chicken":[#鸡

    ],
    "cod":[#鳕鱼

    ],
    "cow":[#牛

    ],
    "donkey":[#驴

    ],
    "frog":[#青蛙

    ],
    "glow_squid":[#发光鱿鱼

    ],
    "horse":[#马

    ],
    "mooshroom":[#哞菇

    ],
    "mule":[#骡

    ],
    "parrot":[#鹦鹉

    ],
    "pig":[#猪

    ],
    "rabbit":[#兔子

    ],
    "salmon":[#鲑鱼

    ],
    "sheep":[#绵羊

    ],
    "skeleton_horse":[#骷髅马

    ],
    "squid":[#鱿鱼

    ],
    "strider":[#炽足兽

    ],
    "tadpole":[#蝌蚪

    ],
    "tropicalfish":[#热带鱼

    ],
    "turtle":[#海龟

    ],
    "villager_v2":[#村民

    ],
    "wandering_trader":[#流浪商人

    ],
    "pufferfish":[#河豚

    ],
    "goat":[#山羊

    ],
    "axolotl":[#美西螈

    ],
    "cat":[#猫

    ],
    "ocelot":[#豹猫

    ],
    "snow_golem":[#雪傀儡

    ],
    "bee":[#蜜蜂

    ],
    "dolphin":[#海豚

    ],
    "fox":[#狐狸

    ],
    "iron_golem":[#铁傀儡

    ],
    "llama":[#羊驼

    ],
    "wolf":[#狼

    ],
    "panda":[#熊猫

    ],
    "polar_bear":[#北极熊

    ],
    "blaze":[#烈焰人

    ],
    "creeper":[#苦力怕

    ],
    "drowned":[#溺尸

    ],
    "elder_guardian":[#远古守卫者

    ],
    "endermite":[#末影螨

    ],
    "evocation_illager":[#唤魔者

    ],
    "ghast":[#恶魂

    ],
    "guardian":[#守卫者

    ],
    "hoglin":[#疣猪兽

    ],
    "husk":[#尸壳

    ],
    "magma_cube":[#岩浆怪

    ],
    "phantom":[#幻翼

    ],
    "pillager":[#劫掠者

    ],
    "ravager":[#劫掠兽

    ],
    "shulker":[#潜影贝

    ],
    "silverfish":[#蠹虫

    ],
    "skeleton":[#骷髅

    ],
    "slime":[#史莱姆

    ],
    "stray":[#流浪者

    ],
    "vex":[#恼鬼

    ],
    "vindicator":[#卫道士

    ],
    "warden":[#warden(暂时不确定)

    ],
    "witch":[#女巫

    ],
    "wither_skeleton":[#凋零骷髅

    ],
    "zoglin":[#僵尸疣猪兽

    ],
    "zombie":[#僵尸

    ],
    "zombie_villager_v2":[#僵尸村民

    ],
    "piglin_brute":[#猪灵蛮兵

    ],
    "enderman":[#末影人

    ],
    "piglin":[#猪灵

    ],
    "spider":[#蜘蛛

    ],
    "cave_spider":[#洞穴蜘蛛

    ],
    "zombie_pigman":[#僵尸猪灵

    ],
    "ender_dragon":[#末影龙

    ],
    "wither":[#凋零

    ]
}
eTypeapDict = {
    "bat":[#蝙蝠

    ],
    "chicken":[#鸡

    ],
    "cod":[#鳕鱼

    ],
    "cow":[#牛

    ],
    "donkey":[#驴

    ],
    "frog":[#青蛙

    ],
    "glow_squid":[#发光鱿鱼

    ],
    "horse":[#马

    ],
    "mooshroom":[#哞菇

    ],
    "mule":[#骡

    ],
    "parrot":[#鹦鹉

    ],
    "pig":[#猪

    ],
    "rabbit":[#兔子

    ],
    "salmon":[#鲑鱼

    ],
    "sheep":[#绵羊

    ],
    "skeleton_horse":[#骷髅马

    ],
    "squid":[#鱿鱼

    ],
    "strider":[#炽足兽

    ],
    "tadpole":[#蝌蚪

    ],
    "tropicalfish":[#热带鱼

    ],
    "turtle":[#海龟

    ],
    "villager_v2":[#村民

    ],
    "wandering_trader":[#流浪商人

    ],
    "pufferfish":[#河豚

    ],
    "goat":[#山羊

    ],
    "axolotl":[#美西螈

    ],
    "cat":[#猫

    ],
    "ocelot":[#豹猫

    ],
    "snow_golem":[#雪傀儡

    ],
    "bee":[#蜜蜂

    ],
    "dolphin":[#海豚

    ],
    "fox":[#狐狸

    ],
    "iron_golem":[#铁傀儡

    ],
    "llama":[#羊驼

    ],
    "wolf":[#狼

    ],
    "panda":[#熊猫

    ],
    "polar_bear":[#北极熊

    ],
    "blaze":[#烈焰人

    ],
    "creeper":[#苦力怕

    ],
    "drowned":[#溺尸

    ],
    "elder_guardian":[#远古守卫者

    ],
    "endermite":[#末影螨

    ],
    "evocation_illager":[#唤魔者

    ],
    "ghast":[#恶魂

    ],
    "guardian":[#守卫者

    ],
    "hoglin":[#疣猪兽

    ],
    "husk":[#尸壳

    ],
    "magma_cube":[#岩浆怪

    ],
    "phantom":[#幻翼

    ],
    "pillager":[#劫掠者

    ],
    "ravager":[#劫掠兽

    ],
    "shulker":[#潜影贝

    ],
    "silverfish":[#蠹虫

    ],
    "skeleton":[#骷髅

    ],
    "slime":[#史莱姆

    ],
    "stray":[#流浪者

    ],
    "vex":[#恼鬼

    ],
    "vindicator":[#卫道士

    ],
    "warden":[#warden(暂时不确定)

    ],
    "witch":[#女巫

    ],
    "wither_skeleton":[#凋零骷髅

    ],
    "zoglin":[#僵尸疣猪兽

    ],
    "zombie":[#僵尸

    ],
    "zombie_villager_v2":[#僵尸村民

    ],
    "piglin_brute":[#猪灵蛮兵

    ],
    "enderman":[#末影人

    ],
    "piglin":[#猪灵

    ],
    "spider":[#蜘蛛

    ],
    "cave_spider":[#洞穴蜘蛛

    ],
    "zombie_pigman":[#僵尸猪灵

    ],
    "ender_dragon":[#末影龙

    ],
    "wither":[#凋零

    ]

}

#方块语言库可扩展原版方块id,原版方块不需要命名空间
blockDestroyDict = {
    "grass":[#草方块

    ],
}
blockPlaceDict = {
    "grass":[#草方块

    ],
}