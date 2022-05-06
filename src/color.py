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
        self.top = top
        self.bottom = bottom
# Example: ColorCombination("WHITE", "SKYBLUE") -> top == "WHITE", bottom == "SKYBLUE"
# TODO: Implement getter


combinations = [
    ColorCombination("WHITE", "SKYBLUE")
]
"""
list for store color combination 
"""
# TODO: Add Color Combination Data


color_code_map = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0)
}
"""
dictionary for store RGB color code
"""
# TODO: Add Color Code Map


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
    pass
# Example: get_color_code("RED") will return (255, 0, 0)
# TODO: Implement Function: Get color code from color_code_map
