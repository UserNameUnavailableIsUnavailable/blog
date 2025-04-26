let ImageViewer = Viewer.noConflict();
let g_ViewLock = false;

document.addEventListener("click", function (event) {
    if (event.target.tagName !== "IMG") {
        return;
    }
    if (g_ViewLock) {
        return;
    }
    g_ViewLock = true;
    let viewer = new ImageViewer(
        event.target,
        {
            "url": 'src',
            "hidden": () => {
                g_ViewLock = false;
                viewer.destroy();
            }
        }
    )
    try {
        viewer.show();
    } catch (e) {
        console.log(e);
    }
})