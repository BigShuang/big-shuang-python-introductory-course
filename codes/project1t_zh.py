## Quick Chat Commands from Command & Conquer: Red Alert 3
## http://nyerguds.arsaneus-design.com/manuals/Red%20Alert%203/RA3_manual_english.pdf
## https://t.bilibili.com/99841003?type=2


QUIT_MENU = "<退出>"
RETURN_MENU = "<返回>"

MENU_L1 = [
    "要求（组队专用）",  # request
    "响应（组队专用）",  # response
    "战术（组队专用）",  # directive
    "全体信息",  # global
]

MENU_L2 = [
    [
        "保卫我的基地！", "撤退", "分兵", "夺取主要目标", "夺取奖励目标",
        "救命！", "侧翼攻击", "偷袭", "离开运输工具"
    ],
    [
        "同意", "否决", "敌人来袭", "发展陆军", "发展空军",
        "发展海军", "发展攻城", "再说一次？"
    ],
    [
        "生产", "快攻", "科技", "游击", "龟缩",
        "扩展", "进驻", "占领", "守卫"
    ],
    [
        "护卫我的基地！", "GL，HF", "大笑", "嘲弄", "恭喜",
        "请求再战", "邀请"
    ]
]


MENU_DICT = {
    "request": {},
    "response": {},
    "directive": {

    },
    "global": {},
}

MENU_L3 = [
    [ # request

    ],
    [ # response

    ],
    [ # directive

    ],
    [ # global

    ],
]

REQUEST_MENUS = [
    {
        "a": [],
        "e": [],
        "s": [],
    },
    {
        "a": [],
        "e": [],
        "s": [],
    },
]
RESPONSE_MENUS = []

DIRECTIVE_MENUS = [
    {  # "生产",
        "a": ["建造更多的军队，你会这么做吧？", "把钱花在刀刃上！"],
        "e": ["训练战斗部队，马上！", "钱在那里是叫你花的！"],
        "s": ["建造更多的部队，快点！", "花光这些钱吧，同志！"],
    },
    {  # "快攻"
        "a": ["", ""],
        "e": [],
        "s": [],
    },
    {  # "科技"
        "a": [],
        "e": [],
        "s": [],
    },
    {  # "游击
        "a": [],
        "e": [],
        "s": [],
    },
    {  # 龟缩
        "a": [],
        "e": [],
        "s": [],
    },
    {  # 扩展
        "a": [],
        "e": [],
        "s": [],
    },
    {  # 进驻
        "a": [],
        "e": [],
        "s": [],
    },
    {  # 占领
        "a": ["占领他们的建筑！", "派出工程师，让我们夺取那些建筑！"],
        "e": [],
        "s": [],
    },
    {  # 守卫
        "a": [],
        "e": [],
        "s": [],
    },
]

GLOBAL_MENUS = []