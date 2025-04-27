// 只创建一个 viewer 对象，该对象与唯一的 img 元素绑定（img 不包含在 DOM 中）
// 点击图像后，设置 img.src，然后更新并显示 viewer 对象
document.addEventListener("DOMContentLoaded", () => {
    let viewerLock = false;
    let div = document.createElement("div");
    let img = document.createElement("img");
    div.appendChild(img)
    img.style.display = "none"
    img.src = ""
    let viewer = new Viewer(
        img,
        {
            "url": "src",
            "hidden": () => {
                viewerLock = false;
            }
        }
    );
    Viewer.noConflict(); // 避免命名空间冲突
    viewer.hide(); // 默认隐藏
    document.addEventListener("click", function (event) {
        if (event.target.tagName !== "IMG") {
            return;
        }
        if (viewerLock) {
            return;
        }
        viewerLock = true;
        try {
            img.src = event.target.src;
            viewer.update();
            viewer.show();
        } catch (e) {
            console.log(e);
        }
    })
})