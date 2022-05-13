class ColorCombination:
    """
    class for represent color combination
    """

    def __init__(self, top: str, bottom: str):
        """
        constructor
        :param top: color of top
        :param bottom: color of bottom
        """
        self.__top = top  # "__name" means private attribute/method
        self.__bottom = bottom

    @property  # "@property" decorator meas getter
    def top(self):
        return self.__top

    @property
    def bottom(self):
        return self.__bottom

    # if you need setter, use decorator like this
    """
    @top.setter
    def top(self, top):
        self.__top = top

    @bottom.setter
    def bottom(self, bottom):
        self.__bottom = bottom
    """

    def __eq__(self, other):  # 다른 인스턴스 값과 같은지 비교
        return self.top == other.bottom and self.bottom == other.bottom


# Example: ColorCombination("WHITE", "SKYBLUE") -> top == "WHITE", bottom == "SKYBLUE"


"""
LIGHTBLUE = 연청 / DARKBLUE = 진청
data reference
        https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kkulkkuls&logNo=221587846538
        https://m.blog.naver.com/ktaitai1/221936224085
"""
combinations = [
    ColorCombination("WHITE", "DARKBLUE"),
    ColorCombination("WHITE", "LIGHTBLUE"),
    ColorCombination("WHITE", "BEIGE"),
    ColorCombination("WHITE", "KHAKI"),
    ColorCombination("WHITE", "CHARCOAL"),
    ColorCombination("WHITE", "BLACK"),
    ColorCombination("NAVY", "DARKBLUE"),
    ColorCombination("NAVY", "LIGHTBLUE"),
    ColorCombination("NAVY", "BEIGE"),
    ColorCombination("NAVY", "KHAKI"),
    ColorCombination("NAVY", "CHARCOAL"),
    ColorCombination("NAVY", "BLACK"),
    ColorCombination("PINK", "DARKBLUE"),
    ColorCombination("PINK", "LIGHTBLUE"),
    ColorCombination("PINK", "BEIGE"),
    ColorCombination("PINK", "KHAKI"),
    ColorCombination("PINK", "CHARCOAL"),
    ColorCombination("PINK", "BLACK"),
    ColorCombination("YELLOW", "DARKBLUE"),
    ColorCombination("YELLOW", "LIGHTBLUE"),
    ColorCombination("YELLOW", "BEIGE"),
    ColorCombination("YELLOW", "KHAKI"),
    ColorCombination("YELLOW", "CHARCOAL"),
    ColorCombination("YELLOW", "BLACK"),
    ColorCombination("BLUE", "DARKBLUE"),
    ColorCombination("BLUE", "LIGHTBLUE"),
    ColorCombination("BLUE", "BEIGE"),
    ColorCombination("BLUE", "KHAKI"),
    ColorCombination("BLUE", "CHARCOAL"),
    ColorCombination("BLUE", "BLACK"),
    ColorCombination("GREEN", "DARKBLUE"),
    ColorCombination("GREEN", "LIGHTBLUE"),
    ColorCombination("GREEN", "BEIGE"),
    ColorCombination("GREEN", "KHAKI"),
    ColorCombination("GREEN", "CHARCOAL"),
    ColorCombination("GREEN", "BLACK"),
    ColorCombination("RED", "BLACK"),
    ColorCombination("RED", "DARKBLUE"),
    ColorCombination("MAROON", "KHAKI"),
    ColorCombination("PURPLE", "KHAKI"),
    ColorCombination("TEAL", "KHAKI"),
    ColorCombination("GRAY", "KHAKI"),
    ColorCombination("MAROON", "BLACK"),
    ColorCombination("LIGHTORANGE", "BLACK"),
    ColorCombination("PURPLE", "BLACK"),
    ColorCombination("LIGHTPINK", "BLACK"),
    ColorCombination("LIGHTGRAY", "BLACK"),
    ColorCombination("LIGHTYELLOW", "BLACK"),
    ColorCombination("TURQUOISEGREEN", "BLACK"),
    ColorCombination("NAVYBLUE", "CRAEM"),
    ColorCombination("MAROON", "CRAEM"),
    ColorCombination("PINK", "CRAEM"),
    ColorCombination("SEAGREEN", "CRAEM"),
    ColorCombination("BLACK", "CRAEM"),
    ColorCombination("SPRINGBLOOM", "GRAY"),
    ColorCombination("PURPLE", "GRAY"),
    ColorCombination("AQUA", "GRAY"),
    ColorCombination("LIGHTPINK", "GRAY"),
    ColorCombination("CHERRY", "GRAY"),
    ColorCombination("BLUE", "GRAY"),
    ColorCombination("GREEN", "GRAY"),
    ColorCombination("RED", "GRAY"),
    ColorCombination("BLACK", "GRAY"),
    ColorCombination("WHITE", "GRAY"),
    ColorCombination("YELLOW", "NAVY"),
    ColorCombination("PEACH", "NAVY"),
    ColorCombination("PINK", "NAVY"),
    ColorCombination("LIGHTGREEN", "NAVY"),
    ColorCombination("PURPLE", "NAVY"),
    ColorCombination("ROYALBLUE", "NAVY"),
    ColorCombination("BROWN", "NAVY"),
    ColorCombination("MAGENTA", "NAVY"),
    ColorCombination("AQUA", "NAVY"),
    ColorCombination("CREAM", "NAVY"),
    ColorCombination("KHAKI", "NAVY"),
    ColorCombination("GRAY", "NAVY"),
    ColorCombination("MAROON", "NAVY"),
    ColorCombination("RUSTORANGE", "NAVY"),
    ColorCombination("CRIMSON", "NAVY"),
    ColorCombination("SUNNYYELLOW", "NAVY"),
    ColorCombination("WHITE", "NAVY"),
    ColorCombination("RED", "NAVY"),
    ColorCombination("BLACK", "NAVY"),
]
"""
list for store color combination 
"""


def check_letters():
    for com in combinations:
        com.top = com.top.replace(" ", "").upper()
        com.bottom = com.bottom.replace(" ", "").upper()


# 비교방법 1 - top 비교 -> bottom 비교
def is_repeated():
    n = 0
    for c in combinations[1:]:
        if combinations[n].top == c.top:  # top 먼저 비교 -> 같으면 하의도 같으면 T, 다르면 F
            re = combinations[n].bottom == c.bottom
            if re is True:
                print(combinations[n], c)
            return not re  # return false

        n += 1


def check_repeated():
    if not is_repeated():
        print("there is a repeated data")
    else:
        print("complete data")


check_letters()
check_repeated()


# 비교2 __eq__메서드 이용
def compare_data():
    n = 0
    for c in combinations[1:]:
        if c.__eq__(combinations[n]):
            print(c.top, c.bottom, combinations[n].top, combinations[n].bottom)
            print("same data occur!")
            break
        n += 1


compare_data()

# 두 개다 동일한 결과 나오는 것 확인

# ColorfulOnes_MatchTip = { maincolor: [outfit pairings with] }
ColorfulOnes_MatchTip = {
    "PINK": ["LIGHTBLUE", 'NAVY', 'GRAY', 'WHITE', 'BLACK'],
    "RED": ["LIGHTBLUE", 'NAVY', 'GRAY', 'WHITE', 'BLACK'],
    "ORANGE": ["LIGHTBLUE", 'NAVY', 'GREEN', 'WHITE', 'BLACK'],
    'BEIGE': ["NAVY", 'PURPLE', 'BROWN', 'WHITE', 'BLACK'],
    'YELLOW': ["GREEN", 'NAVY', 'WHITE', 'BLACK'],
    'GREEN': ["ORANGE", "PURPLE", "WHITE", "BLACK"],
    'LIGHTBLUE': ["PINK", 'RED', 'ORANGE', 'WHITE', 'BLACK'],
    'DARKBLUE': ["PINK", 'RED', 'YELLOW', 'GRAY', 'WHITE', 'BLACK'],
    'PURPLE': ["ORANGE", 'GRAY', 'GREEN', 'WHITE', 'BLACK'],
    'BROWN': ['BEIGE', 'WHITE', 'BLACK'],
    'GREY': ["PINK", 'RED', 'NAVY', 'PURPLE']
}


color_code_map = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "NAVY": (0, 0, 128),
    "PINK": (255, 192, 203),
    "YELLOW": (255, 255, 0),
    "MAROON": (128, 0, 0),
    "PURPLE": (128, 0, 128),
    "LIGHTPINK": (255, 182, 193),
    "TEAL": (0, 128, 128),
    "GRAY": (128, 128, 128),
    "LIGHTGRAY": (211, 211, 211),
    "LIGHTYELLOW": (255, 255, 224),
    "SEAGREEN": (46, 139, 87),
    "AQUA": (0, 255, 255),
    "LIGHTGREEN": (144, 238, 144),
    "ROYALBLUE": (65, 105, 225),
    "BROWN": (165, 42, 42),
    "MAGENTA": (255, 0, 255),
    "KHAKI": (240, 230, 140),
    "CRIMSON": (220, 20, 60),
    "BEIGE": (245, 245, 220),
    "LIGHTBLUE": (173, 216, 230),
    "DARKBLUE": (0, 0, 139),
    "CHERRY": (222, 49, 99),
    "PEACH": (255, 229, 180),
    "CREAM": (255, 253, 208),
    "CHARCOAL": (54, 69, 79),
    "TURQUOISEGREEN": (160, 214, 180),
    "RUSTORANGE": (196, 85, 8),
    "LIGHTORANGE": (254, 216, 177),
    "SUNNYYELLOW": (255, 249, 23),
    "NAVYBLUE": (45, 35, 99),
    "SPRINGBLOOM": (228, 125, 167),
}
"""
dictionary for store RGB color code
    https://www.rapidtables.com/web/color/RGB_Color.html
    http://www.workwithcolor.com/color-chart-full-01.htm
    https://color-register.org/color/
    https://www.color-name.com/navy-blue.color
    https://www.colorxs.com/color/springtime-bloom-2079-40
"""


def get_combi(where: str, color: str) -> str:
    """
    get color combination from combinations
    :param where: location. value is "TOP" or "BOTTOM"
    :param color: color of cloth
    :return: where="TOP" will return color of bottom. where="BOTTOM" will return color of top.
    """
    pass
# Example: get_combi("TOP", "WHITE") will return "SKYBLUE"
# TODO: Implement Function: Get "ColorCombination" Instance from "combinations" List


def get_color_code(color) -> tuple:
    """
    get color code
    :param color: color name (dictionary key of color_code_map)
    :return: tuple for color code
    """
    return color_code_map[color]
# Example: get_color_code("RED") will return (255, 0, 0)
# print(get_color_code("RED")) # test get_color_code_map
