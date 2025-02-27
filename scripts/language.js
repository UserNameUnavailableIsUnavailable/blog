const language = document.querySelector(`meta[name="language"]`)
if (language == "zh_cn") {
    let collection
    collection = document.getElementsByClassName("quarto-appendix-heading")
    for (let e of collection) {
        if (e.innerHTML == "Footnotes") {
            e.innerHTML = "脚注"
        }
    }
    collection = document.getElementsByClassName("quarto-title-meta-heading")
    for (let e of collection) {
        if (e.innerHTML == "Author") {
            e.innerHTML = "作者"
        }
    }
    collection = document.getElementById("toc-title")
    collection?.innerHTML = "在本页中"
}
