import reflex as rx
import reflex_pokedex.styles.styles as styles

import reflex_pokedex.constants as const
from reflex_pokedex.components.titulo import titulo
from reflex_pokedex.components.link_icon import link_icon

TITLE_SIZE = ["1.5em", styles.Size.DEFAULT.value]

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.link(
                rx.hstack(
                    rx.span( titulo("Hernandez", styles.Font.LOGO, styles.FontWeight.BOLD, TITLE_SIZE , styles.Color.PRIMARY ),),
                    rx.span( titulo("Palo", styles.Font.LOGO, styles.FontWeight.BOLD, TITLE_SIZE, styles.Color.SECONDARY ),),
               ),
                href="/",
            ),
         ),
        rx.spacer(), 
        rx.hstack(
            link_icon(
                "/icons/github.svg",
                const.GITHUB_URL,
                "GitHub",
            ),
            link_icon(
                "/icons/x.svg",
                const.TWITTER_X_URL,
                "X",
            ),
             
            link_icon(
                "/icons/linkedin.svg",
                const.LINKEDIN_URL,
                "Linkedin",
            ),           
        ),
        bg= styles.Color.BACKGROUND.value,
        width="100%",        
        position="sticky",
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.DEFAULT.value,
        z_index="999",
        top="0",


    )