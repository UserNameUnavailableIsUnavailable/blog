function getContainingDirectory(url) {
    // url: https://example.com/path/to/file.txt
    let origin = url.origin // https://example.com
    let pathname = url.pathname // /path/to/file.txt
    let lastSlashIndex = pathname.lastIndexOf("/")
    let directoryPath = pathname.slice(0, lastSlashIndex + 1) // /path/to/
    return new URL(`${origin}${directoryPath}`) // https://example.com/path/to/
}

function makeEl(name, attr, doc) {
    const el = doc.createElement(name);
    if (attr.id) {
        el.id = attr.id;
    }
    for (const cls of attr.classes || []) {
        el.classList.add(cls);
    }
    const attribs = attr.attributes || {};
    for (const key of Object.keys(attribs)) {
        el.setAttribute(key, attribs[key]);
    }
    return el;
}

let sectionId = 1

function makeRuntimeSidebarItems(list, level, doc, baseUrl) {
    let ul = undefined
    if (!list) { return }
    let attr = { classes: ["list-unstyled"] }
    if (list.type === "root") {
        attr.classes.push("mt-1")
    } else {
        if (list.type === "section") {
            attr.classes.push("sidebar-section")
        }
        if (list.collapse) {
            attr.classes.push("collapse")
        }
        attr.classes.push(`depth${level}`)
        attr.classes.push("show")
    }
    ul = makeEl("ul", attr, doc)
    list.children.forEach(e => {
        if (e.type === "section") {
            let li = makeEl("li", { classes: ["sidebar-item", "sidebar-item-section"] }, doc)
            let div = makeEl("div", { classes: ["sidebar-item-container"] }, doc)
            let url = new URL(e.href, baseUrl)
            let a1 = makeEl("a", { classes: ["sidebar-item-text", "sidebar-link"], attributes: { "href": url.href } }, doc)
            a1.innerHTML = `<span class="menu-text">${e.title}</span>`
            let a2 = makeEl("a", { classes: ["sidebar-item-toggle", "text-start"], attributes: { "href": url.href } }, doc)
            a2.setAttribute("data-bs-toggle", "collapse")
            a2.setAttribute("data-bs-target", `#quarto-sidebar-section-${sectionId}`)
            a2.setAttribute("role", "navigation")
            a2.setAttribute("aria-expanded", e.collapse ? "false" : "true")
            a2.innerHTML = `<i class="bi bi-chevron-right ms-2"></i>`
            if (window.location.href === url.href) { // 地址匹配
                a1.classList.add("active")
            }
            div.appendChild(a1)
            div.appendChild(a2)
            li.appendChild(div)
            let subul = makeRuntimeSidebarItems(e, level + 1, doc, baseUrl)
            if (subul) {
                li.appendChild(subul)
            }
            subul.id = `quarto-sidebar-section-${sectionId}`
            subul.classList.add("collapse")
            sectionId++
            ul.appendChild(li)
        } else if (e.type === "document") { // 普通文档
            let li = makeEl("li", { classes: ["sidebar-item"] }, doc)
            let div = makeEl("div", { classes: ["sidebar-item-container"] }, doc)
            let url = new URL(e.href, baseUrl)
            let a = makeEl("a", { classes: ["sidebar-item-text", "sidebar-link"], attributes: { "href": url.href } }, doc)
            if (window.location.href === url.href) {
                a.classList.add("active")
            }
            a.innerHTML = `<span class="menu-text">${e.title}</span>`
            div.appendChild(a)
            li.appendChild(div)
            ul.appendChild(li)
        }
    })
    return ul
}

async function makeRuntimeSidebar() {
    let quartoSidebar = document.getElementById("quarto-sidebar")
    if (!quartoSidebar) {
        return
    }
    let runtimeSidebar
    let meta = document.querySelector("meta[name=RuntimeSidebar]")
    if (!meta) {
        runtimeSidebar = true
    } else {
        runtimeSidebar = meta.getAttribute("content") === "true" ? true : false
    }
    if (!runtimeSidebar) { return }
    let documentUrl = new URL(window.location.href) // https://example.com/path/to/file.txt
    let fallbackSidebarUrl = new URL("sidebar.json", documentUrl.origin) // https://example.com/path/to/sidebar.json
    let containingDirectory = getContainingDirectory(documentUrl) // https://example.com/path/to/
    let sidebar = "sidebar.json"
    let sidebarUrl = new URL(sidebar, containingDirectory) // https://example.com/path/to/sidebar.json
    let response = await fetch(sidebarUrl)
    if (!response.ok) {
        return
    }
    await response.json().then((sidebarJson) => {
        console.log(sidebarJson)
        let sidebarNav = makeEl("nav", { id: "quarto-sidebar", classes: ["sidebar", "collapse", "collapse-horizontal", "quarto-sidebar-collapse-item", "sidebar-navigation", "docked", "overflow-auto",] }, document)
        let sidebarMenuContainer = makeEl("div", { classes: ["sidebar-menu-container",] }, document)
        let ul = makeRuntimeSidebarItems(sidebarJson, 0, document, documentUrl.origin)
        if (ul) {
            sidebarMenuContainer.appendChild(ul)
        }
        sidebarNav.appendChild(sidebarMenuContainer)
        console.log(quartoSidebar)
        sidebarNav.style = quartoSidebar.style
        quartoSidebar.replaceWith(sidebarNav)
        console.log(sidebarNav)
        console.log(document.getElementById("quarto-content"))

    })
}

makeRuntimeSidebar()