import reflex as rx

import reflex_pokedex.styles.styles as  styles
import reflex_pokedex.constants as constants

import reflex_pokedex.pages.index as index
import reflex_pokedex.pages.detalle as detalle

app = rx.App(
    
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={constants.GOOGLE_ANALYTICS_TAG}"
        ),
        rx.script(
            f"""
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{constants.GOOGLE_ANALYTICS_TAG}');
            """
            ),
        ],
    )

