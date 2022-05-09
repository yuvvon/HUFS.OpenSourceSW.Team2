from flask import Flask

from color import *

app = Flask(__name__,
            static_url_path="",
            static_folder="web/static")


@app.route("/")
def index():
    with open("./web/static/index.html", encoding="utf8", mode="r") as idx_file:
        return idx_file.read()


@app.route("/api/color")
def color_api():
    color = ""
    loc = ""

    combi = get_combi(loc, color)
    color_code = get_color_code(combi)
    # Call "get_combi" Function
    return "RESULT_OF_GET_COMBI_WILL_BE_RETURN"
# TODO: Implement color API Route


def page_not_found():
    return "04_ERROR_PAGE_WILL_BE_RETURN"
# TODO: Implement 404 Error Page


app.register_error_handler(404, page_not_found)

if __name__ == "__main__":
    app.run()
