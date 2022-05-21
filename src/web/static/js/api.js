/**
 * API root url
 * @type {string}
 */
const API_ROOT = "http://localhost:3000"

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
    const endpoint = API_URL.combi;

    const url = `${API_ROOT}${endpoint.path}?color=${color}&loc=${loc}`;
    const res = await fetch(url, {
        method: endpoint.method
    });

    return res.json();
}

/**
 * fetch color list from "/api/color/list"
 * @returns {Promise<{list: Array<{top: string, bottom: string}>, colorCode: Array<{name: string, code: string}>}>}
 * @async
 */
const fetchColorList = async () => {
    const endpoint = API_URL.list;
    const url = `${API_ROOT}${endpoint.path}`;
    const res = await fetch(url, {
        method: endpoint.method
    });
    return res.json();
}