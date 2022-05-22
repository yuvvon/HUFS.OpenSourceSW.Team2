const getElem = (querySelector) => {
    return document.querySelector(querySelector);
};

// html elements
const partTopButton = getElem("#main-part-top-button");
const partBottomButton = getElem("#main-part-bottom-button");
const choosePartDiv = getElem("#choose-part-div");
const colorPaletteDiv = getElem("#main-part-color-palette");

const hideElem = (elem) => {
    elem.className += " hide-with-animation";
    setTimeout(() => {
        elem.style.display = "hide";
    }, 1000);
}

const showElem = (elem) => {
    elem.style.display = "block";
    setTimeout(() => {
        elem.className = elem.className.replace("hide-with-animation", "show-with-animation");
    }, 1000);
}

const createColorPalette = (colorList, codeList) => {

}

// Run Async Code Here
(async () => {
    try {
        // fetch color combi list
        const colorList = await fetchColorList();

        const partSelectOnClick = (loc) => {
            hideElem(choosePartDiv);

            let sortColorList
            if (loc === "TOP") {
                sortColorList = colorList.list.sort((prev, next) => {
                   return prev.top - next.top;
                });
            } else {

            }


            showElem(colorPaletteDiv);
        };

        // add onclick event to part select button
        partTopButton.onclick = () => { partSelectOnClick("TOP"); };
        partBottomButton.onclick = () => { partSelectOnClick("BOTTOM"); };


    } catch (e) {
        console.log(e);
    }
})();