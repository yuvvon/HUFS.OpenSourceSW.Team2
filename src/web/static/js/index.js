// Run Async Code Here
(async () => {
    try {
        const colorList = await fetchColorList();
    } catch (e) {
        console.log(e);
    }
})();