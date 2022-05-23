// html elements
const combinationTitle = getElem("#main-picked-title");
const pickedColorDiv = getElem("#picked-color-div");
const pickedColorBox = getElem("#picked-color-box");
const combiPaletteDiv = getElem("#combi-color-div");

/**
 * make #main-picked-title to `Your Color: ${color} on ${loc}`
 * @param elem - \#main-picked-title
 * @param {string} color - picked color
 * @param {string} loc - picked loc
 */
const makeCombinationTitle = (elem, color, loc) => {
    elem.innerText += ` ${color} on ${loc}`;
}

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

/**
 * make \#picked-color-box to colored
 * @param {HTMLElement} elem
 * @param {string} colorCode
 */
const makePickedColorBoxToColored = (elem, colorCode) => {
    if (colorCode.toLowerCase() === "ffffff") {
        elem.style.borderStyle = "solid";
        elem.style.borderWidth = "1px";
        elem.style.borderColor = "#000000";
    } else {
        elem.style.backgroundColor = `#${colorCode}`;
    }
}

// Run Async Code Here
(async () => {
    const params = extractQuery(getCurrentUrl());
    const color = params.get("color");      // picked color name
    const loc = params.get("loc");          // picked loc ("TOP" or "BOTTOM")

    makeCombinationTitle(combinationTitle, color, loc);

    if (isValidParam(color, loc)) {
        try {
            const colorData = await fetchColorCombi(color, loc);
            const combinationList = colorData.colors;       // color combinations
            const colorCodeList = colorData.colorCode       // color code

            /**
             * get color code from color name
             * @param {string} colorName
             * @returns {string}
             */
            const getColorCode = (colorName) => {
                return colorCodeList.find(colorCodeObj => colorCodeObj.name.toUpperCase() === colorName.toUpperCase()).code;
            }

            const pickedColorCode = getColorCode(color);
            makePickedColorBoxToColored(pickedColorBox, pickedColorCode);

            // ------------- ADD YOUR CODE HERE --------------
            // TODO: MAKE COMBINATION COLOR LIST FROM combinationList

        } catch (e) {
            console.log(e);
        }
    }
})();