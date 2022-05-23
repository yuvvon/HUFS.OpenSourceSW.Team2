// html elements
const partTopButton = getElem("#main-part-top-button");
const partBottomButton = getElem("#main-part-bottom-button");
const choosePartDiv = getElem("#choose-part-div");
const colorPaletteDiv = getElem("#main-part-color-palette-div");
const colorPaletteButtonContainer = getElem("#color-palette-row-div");
const colorPaletteBackButton = getElem("#color-palette-back-button");

/**
 * sort color list from loc
 * @param {Array<{top: string, bottom: string}>} colorList - color combinations list
 * @param {"TOP" | "BOTTOM"} loc - loc
 * @returns {Array<{top: string, bottom: string}>}
 */
const sortColorCombi = (colorList, loc) => {
    if (loc === "TOP") {
        return colorList.sort((prev, next) => {
            return prev.top < next.top ? -1 : prev.top > next.top ? 1 : 0;
        });
    } else {
        return colorList.sort((prev, next) => {
            return prev.bottom < next.bottom ? -1 : prev.bottom > next.bottom ? 1 : 0;
        });
    }
}

/**
 * onClick event function for color select button
 * @param {string} colorName - color name
 * @param {"TOP" | "BOTTOM"} loc
 */
const colorButtonOnClick = (colorName, loc) => {
    location.href = `/color?color=${colorName}&loc=${loc}`;
}

/**
 * create color palette HTML element
 * @param {number} idx - index for element id
 * @param {string} colorName - color name
 * @param {string} colorCode - hex color code
 * @param {"TOP" | "BOTTOM"} loc
 * @returns {HTMLDivElement}
 */
const createColorPaletteElem = (idx, colorName, colorCode, loc) => {
    const box = createSquareDiv(colorCode);

    const text = document.createElement("p");
    text.innerText = colorName;

    const boxWrap = document.createElement("div");
    boxWrap.style.width = "100%";
    boxWrap.appendChild(box);

    const setWrap = document.createElement("div");
    setWrap.className = "col-6 col-xs-4 col-md-3 col-lg-2 text-center";
    setWrap.id = `color-palette-color-set-wrap-${idx}`;
    setWrap.appendChild(boxWrap)
    setWrap.appendChild(text);

    setWrap.onclick = () => {
        colorButtonOnClick(colorName, loc);
    }

    return setWrap;
}

/**
 * append color palette elements
 * @param {Array<{top: string, bottom: string}>} colorList - color combination list
 * @param {Array<{name: string, code: string}>} codeList - color code list
 * @param {"TOP" | "BOTTOM"} loc
 */
const appendColorPalettes = (colorList, codeList, loc) => {
    const targetLoc = loc === "TOP" ? "top" : "bottom";
    const colorNameSet = new Set();
    colorList.map(color => {
        colorNameSet.add(color[targetLoc]);
    });

    Array.from(colorNameSet.values()).map((colorName, idx) => {
        const colorCode = codeList.find(codeObj => codeObj.name.toUpperCase() === colorName.toUpperCase());
        const elem = createColorPaletteElem(idx, colorName, colorCode.code, loc);
        colorPaletteButtonContainer.appendChild(elem);
    });
}

/**
 * onClick event function for back button
 */
const backButtonOnClick = () => {
    colorPaletteButtonContainer.innerText = "";
    hideElem(colorPaletteDiv);
    showElem(choosePartDiv);
};

// add onclick event to back button
colorPaletteBackButton.onclick = backButtonOnClick;

/**
 * onClick event function for part select button
 * @param {{list: Array<{top: string, bottom: string}>, colorCode: Array<{name: string, code: string}>}} colorList
 * @param {"TOP" | "BOTTOM"} loc
 */
const partSelectOnClick = (colorList, loc) => {
    hideElem(choosePartDiv);
    appendColorPalettes(colorList.list, colorList.colorCode, loc);
    showElem(colorPaletteDiv);
};

// Run Async Code Here
(async () => {
    try {
        // fetch color combi list
        const colorList = await fetchColorList();

        // add onclick event to part select button
        partTopButton.onclick = () => {
            partSelectOnClick(colorList, "TOP");
        };
        partBottomButton.onclick = () => {
            partSelectOnClick(colorList, "BOTTOM");
        };
    } catch (e) {
        console.log(e);
    }
})();