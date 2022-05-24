# coding=utf8

from flask import Flask, request, jsonify

from color import get_combi, get_color_code, combinations, color_code_map

"""
ref  https://velog.io/@jewon119/01.Flask-%EA%B8%B0%EC%B4%88-REST-API-%EA%B5%AC%ED%98%84
"""
app = Flask(__name__, static_url_path="", static_folder="web/static")


def make_2len_hex(hex_code):
    if len(hex_code) == 1:
        return "0" + hex_code
    return hex_code


def rgb_to_hex(r, g, b):
    hex_r = format(r, "x")
    hex_g = format(g, "x")
    hex_b = format(b, "x")

    hex_r = make_2len_hex(hex_r)
    hex_g = make_2len_hex(hex_g)
    hex_b = make_2len_hex(hex_b)

    return hex_r + hex_g + hex_b


@app.route("/")
def index_page():
    with open("./web/static/index.html", encoding="utf8", mode="r") as idx_file:
        return idx_file.read()


@app.route("/color")
def color_page():
    with open("./web/static/color.html", encoding="utf8", mode="r") as idx_file:
        return idx_file.read()


@app.route("/api/color/combi")
def color_combi():
    color = request.args.get("color")
    loc = request.args.get("loc")

    combi = get_combi(loc, color)  # 상의 또는 하의 어울리는 color -> list로 리턴
    combi_set = set()
    for c in combi:
        combi_set.add(c)

    combi_list = []

    for c in combi_set:
        combi_list.append(c)

    color_set = set()
    color_set.add(color)

    for c in combi_list:
        color_set.add(c)

    color_code_obj_list = []

    for c in color_set:
        code = get_color_code(c)
        color_code_obj_list.append({"name": c, "code": rgb_to_hex(code[0], code[1], code[2])})

    combi_db = {
        "pickedColor": color,
        "pickedLoc": loc,
        "colors": combi_list,
        "colorCode": color_code_obj_list,
    }
    return jsonify(combi_db)


@app.route("/api/color/list")
def color_list():
    list_db = []
    for c in combinations:
        list_db.append({"top": c.top, "bottom": c.bottom})

    color_code_db = []
    key_list = color_code_map.keys()

    for key in key_list:
        color_code = color_code_map[key]
        temp = {"name": key, "code": rgb_to_hex(color_code[0], color_code[1], color_code[2])}
        color_code_db.append(temp)

    combi_data = {
        "list": list_db,
        "colorCode": color_code_db,
    }
    return jsonify(combi_data)


def page_not_found():
    return "04_ERROR_PAGE_WILL_BE_RETURN"


# TODO: Implement 404 Error Page


app.register_error_handler(404, page_not_found)

if __name__ == "__main__":
    app.run()
