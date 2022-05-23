/**
 * API root url
 * @type {string}
 */
const API_ROOT = "http://127.0.0.1:5000"

/**
 * api endpoints
 * @type {{list: {path: string, method: string}, combi: {path: string, method: string, query: string[]}}}
 */
const API_URL = {
    combi: {
        path: "/api/color/combi",
        method: "GET",
        query: ["loc", "color"]
    },
    list: {
        path: "/api/color/list",
        method: "GET"
    }
}


const TEST_DATA = {
    fetchColorCombiRes: {
        pickedLoc: "TOP",
        pickedColor: "WHITE",
        colors: [
            "LIGHTBLUE",
            "BEIGE"
        ],
        colorCode: [
            { name: "WHITE", code: "ffffff" },
            { name: "LIGHTBLUE", code: "add8e6" },
            { name: "BEIGE", code: "f5f5dc" }
        ]
    },
    fetchColorListRes: {
        list: [
            { top: "WHITE", bottom: "LIGHTBLUE" },
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
            { top: "WHITE", bottom: "BEIGE"},
        ],
        colorCode: [
            { name: "WHITE", code: "ffffff" },
            { name: "LIGHTBLUE", code: "add8e6" },
            { name: "BEIGE", code: "f5f5dc" }
        ]
    }
};


/**
 * check loc is correct. loc must be "TOP" or "BOTTOM".
 * @param {string} loc
 * @returns {boolean}
 */
const isCorrectLoc = (loc) => {
    return (loc === "TOP" || loc === "BOTTOM");
}

/**
 * fetch color combi from "/api/color/combi"
 * @param {string} color - color name
 * @param {"TOP" | "BOTTOM"} loc - cloth location
 * @returns {Promise<{pickedColor: string, pickedLoc: "TOP" | "BOTTOM", colors: Array<string>, colorCode: Array<{name: string, code: string}>}>}
 * @async
 */
const fetchColorCombi = async (color, loc) => {
    if (!isCorrectLoc(loc)) {
        throw new Error(`${loc} is Invalid Loc`);
    }
    /*const endpoint = API_URL.combi;

    const url = `${API_ROOT}${endpoint.path}?color=${color}&loc=${loc}`;
    const res = await fetch(url, {
        method: endpoint.method
    });

    return res.json();*/
    return TEST_DATA.fetchColorCombiRes;
}

/**
 * fetch color list from "/api/color/list"
 * @returns {Promise<{list: Array<{top: string, bottom: string}>, colorCode: Array<{name: string, code: string}>}>}
 * @async
 */
const fetchColorList = async () => {
    /*const endpoint = API_URL.list;
    const url = `${API_ROOT}${endpoint.path}`;
    const res = await fetch(url, {
        method: endpoint.method
    });
    return res.json();*/
    return TEST_DATA.fetchColorListRes;
}