from flask import Flask

app = Flask(__name__,
            static_url_path="",
            static_folder="web/static")


@app.route("/api/get_color")
def color_api():
    # Call "get_combi" Function
    return "RESULT_OF_GET_COMBI_WILL_BE_RETURN"
# TODO: Implement get_color API Route


def page_not_found():
    return "04_ERROR_PAGE_WILL_BE_RETURN"
# TODO: Implement 404 Error Page


app.register_error_handler(404, page_not_found)
