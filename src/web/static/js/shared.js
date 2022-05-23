/**
 * get HTMLElement by query selector
 * @param {string} querySelector
 * @returns {HTMLElement}
 */
const getElem = (querySelector) => {
    return document.querySelector(querySelector);
};

/**
 * hide element (make css display property to "none")
 * @param {HTMLElement} elem
 */
const hideElem = (elem) => {
    elem.style.display = "none";
}

/**
 * show element (make css display property to "block")
 * @param {HTMLElement} elem
 */
const showElem = (elem) => {
    elem.style.display = "block";
}

/**
 * create square div tag w/ colorCode background color
 * @param {string} colorCode - color code
 * @returns {HTMLDivElement}
 */
const createSquareDiv = (colorCode) => {
    const box = document.createElement("div");
    box.className = "box";

    box.style.backgroundColor = `#${colorCode}`;

    // if WHITE color, add black border
    if (colorCode.toLowerCase() === "ffffff") {
        box.style.borderColor = "#000000";
        box.style.borderWidth = "1px";
        box.style.borderStyle = "solid";
    }

    box.style.borderRadius = "0.5em";

    return box;
}
