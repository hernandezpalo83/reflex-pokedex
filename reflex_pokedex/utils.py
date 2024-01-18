import reflex as rx

# Común
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


meta = [
    {"name": "og:type", "content": "website"},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@hernandezpalo"}
]

# Index
title_index = "PoKeDeX | by HernandezPalo"
description_index = "PoKeDeX Ejemplo de pagina desarrollada en Reflex emulando la famosa Pokedex."
preview_index = "project/Portafolio.jpg"

meta_index = [
    {"name": "og:title", "content": title_index},
    {"name": "og:description", "content": description_index},
    {"name": "og:image", "content": preview_index}
]
meta_index.extend(meta)
