local custom_keys = {
    "FootnotesSectionName"
}

function Meta(meta)
    local meta_tag_template = '<meta name="%s" content="%s">\n'
    -- add sharing keys
    local tags = ""
    for j = 1, #custom_keys
    do
        local i = custom_keys[j]
        if meta[i]
        then
            tags = tags .. string.format(meta_tag_template, i, pandoc.utils.stringify(meta[i]))
        end
    end
    quarto.doc.include_text('in-header', tags)
    return meta
end