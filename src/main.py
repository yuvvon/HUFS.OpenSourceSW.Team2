
from flask import Flask, request, jsonify
from color import get_combi, get_color_code,combinations,color_code_map

"""
ref  https://velog.io/@jewon119/01.Flask-%EA%B8%B0%EC%B4%88-REST-API-%EA%B5%AC%ED%98%84
"""
app = Flask(__name__, static_url_path="", static_folder="web/static")

def rgb_to_hex(r,g,b):
    r,g,b = int(r),int(g), int(b)
    return hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(r)[2:].zfill(2)


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

    combi = get_combi(loc, color) #상의 또는 하의 어울리는 color -> list로 리턴
    combi = set(combi)
   # color_code = get_color_code(combi) #param changed combi -> color (get_color_code 함수가 color를 받습니다)
    color_code_dic=[]
    for c in combi:
        color_code = get_color_code(c)
        r,g,b= color_code[0],color_code[1],color_code[2]
        temp = {"name": c, "code":rgb_to_hex(r,g,b)}
        color_code_dic.append(temp)
    combi_db={
        "pickedColor":color,
        "pickedLoc":loc,
        "colors":combi,
        "colorCode":color_code_dic
    }
    return jsonify(combi_db) 

# TODO: Implement color combinations API Route


@app.route("/api/color/list")
def color_list():
    list_db=[]
    for c in combinations:
        list_db.append({"top":c[0], "bottom":c[1]})
        
    color_code_db=[]
    for c in color_code_map:
        r,g,b= color_code_map[0],color_code_map[1],color_code_map[2]
        temp = {"name": c, "code":rgb_to_hex(r,g,b)}
        color_code_db.append(temp)
    combi_data={
        "list":list_db,
        "colorCode":color_code_db,
    }
    return jsonify(combi_data)


# TODO: Implement color list API Route


def page_not_found():
    return "04_ERROR_PAGE_WILL_BE_RETURN"


# TODO: Implement 404 Error Page


app.register_error_handler(404, page_not_found)

if __name__ == "__main__":
    app.debug = True
    app.run()
