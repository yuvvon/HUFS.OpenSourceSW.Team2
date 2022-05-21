/**
 * get current url
 * @returns {string}
 */
const getCurrentUrl = () => {
    return window.location.href;
}

/**
 * extract querystring from url
 * @param {string} url
 * @returns {URLSearchParams}
 */
const extractQuery = (url) => {
    return new URL(url).searchParams;
}

/**
 * check fetchColorCombi params are valid
 * @param {string} color
 * @param {string} loc
 * @returns {boolean}
 */
const isValidParam = (color, loc) => {
    return !(typeof color === "undefined" || !isCorrectLoc(loc));
}

// Run Async Code Here
(async () => {
    const params = extractQuery(getCurrentUrl());
    const color = params.get("color");
    const loc = params.get("loc");

    if (isValidParam(color, loc)) {
        try {
            const colorData = await fetchColorCombi(color, loc);

            // TODO: ADD DOM Modifier Functions

        } catch (e) {
            console.log(e);
        }
    }
})();