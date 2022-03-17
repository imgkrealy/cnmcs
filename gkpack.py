packName = "聆听万物资源包dome"#在此修改附加包的名字(游戏内显示)
id = ""#内容仅限小写英文字母,长度须小于8,建议使用 自己标识符+某些字母

#allDict为未收录的语言库(例如其他组件的生物)
#eTypehartDict为攻击生物的语言库
#eTypeapDict为玩家靠近生物的语言库
#blockDestroyDict为破坏方块的语言库
#blockPlaceDict为放置方块的语言库
#所有语言库均可自行扩展(namespace:id)

#一句话不可以超过30个汉字，推荐小于25个
allDict = {
    [
        "gq的组件开发者不多,但地图开发者非常多,即使组件数量远大于地图",
        ""
    ]
}
eTypehartDict = {
    "bat":[#蝙蝠

    ],
    "chicken":[#鸡

    ],
    "cod":[#鳕鱼

    ],
    "cow":[#牛
        "晚餐就应该吃羊肉"
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
#优先添加生存常用方块
blockDestroyDict = {
    "grass":[#草方块

    ],
    "dirt":[#泥土

    ],
    "stone":[#石头

    ],
    "cobblestone":[#圆石

    ],
    "log":[#原木(不包括log2)

    ],
    "coal_ore":[#煤矿石

    ],
    "iron_ore":[#铁矿石

    ],
    "gold_ore":[#金矿石

    ],
    "diamond_ore":[#钻石矿石

    ],
    "raw_iron_block":[#粗铁块

    ],
    "raw_gold_block":[#粗金块

    ],
    "raw_copper_block":[#粗铜块

    ],
    "redstone_block":[#红石块

    ],
    "obsidian":[#黑曜石

    ],
    "blackblock":[#黑石

    ],
    "wool":[#羊毛

    ],
    "chest":[#箱子

    ],
    "bookbookshelf":[#书架

    ],
    "crafting_table":[#工作台

    ],
    "barrel":[#桶

    ],
    "furnace":[#熔炉

    ],
    "blast_furnace":[#高炉

    ],
    "smoker":[#烟熏炉

    ],
    "cartography_table":[#制图台

    ],
    "fletching_table":[#制箭台

    ],
    "smithing_table":[#锻造台

    ],
    "loom":[#织布机

    ],
    "quartz_block":[#石英块

    ],
    "quartz_ore":[#石英矿石

    ],
    "coal_block":[#煤炭块

    ],
    "iron_block":[#铁块

    ],
    "gold_block":[#金块

    ],
    "diamond_block":[#钻石块

    ],
    "glass":[#玻璃块

    ],
    "sand":[#沙子

    ],
    "slime":[#黏液块

    ],
    "snow":[#雪块

    ],
    "dispenser":[#发射器

    ],
    "dropper":[#投掷器

    ],
    "end_stone":[#末地石

    ],
    "mob_spawner":[#刷怪笼

    ],
    "ender_chest":[#末影箱

    ],
    "sponge":[#海绵

    ],
    "soul_sand":[#灵魂沙

    ],
    "framland":[#耕地

    ],
    "stonecutter_block":[#切石机

    ],
    "bed":[#床

    ],
    "hay_block":[#干草块

    ],
    "shulker":[#潜影盒

    ],
    "anvil":[#铁砧

    ],
    "tnt":[#TNT

    ],
    "bedrock":[#基岩

    ],
    "torch":[#火把

    ],
    "glowstone":[#萤石

    ],
    "cactus":[#仙人掌

    ]   
}
blockPlaceDict = {
    "grass":[#草方块

    ]
}
