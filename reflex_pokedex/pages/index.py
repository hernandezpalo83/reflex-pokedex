import reflex as rx
import reflex_pokedex.utils as utils
import reflex_pokedex.styles.styles as  styles

from reflex_pokedex.components.navbar import navbar
from reflex_pokedex.components.footer import footer
from reflex_pokedex.components.titulo import titulo
from reflex_pokedex.data.list_pokemon import lista_pokemon

@rx.page(
    title=utils.title_index,
    description=utils.description_index,
    image=utils.preview_index,
    meta=utils.meta_index
)

def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                rx.image(
                    src="pokedex_logo.png",
                    alt="pokedex logo"
                ),
                rx.box(
                    rx.responsive_grid(
                        *[
                                pintar_pokemon(data)
                                for data in lista_pokemon
                            ],
                        margin_top = styles.Size.BIG.value,    
                        spacing="20px",
                        columns=[1, 2, 3, 4, 5, 5],
                        ),            
                ),
                footer(),
                spacing=styles.Size.VERY_BIG.value,
                width="100%"
            ),
        ),
        padding=styles.Size.VERY_BIG.value,
    )

def pintar_pokemon(pokemonslist: list[lista_pokemon])  -> rx.Component:
    return  rx.box(
                rx.link(
                    rx.vstack(
                        rx.hstack(
                            rx.badge( pokemonslist.id),
                            titulo(pokemonslist.nombre.capitalize() ),                        
                        ),        
                        rx.avatar(
                            src=pokemonslist.imagen_url,
                            name= pokemonslist.nombre,
                            size='2xl',
                            show_border=True,
                            bg='#FFFFFF',
                            aling="center",
                        ),
                        rx.responsive_grid(
                            *[
                                pintar_tipo(data)
                                for data in pokemonslist.tipos 
                            ],
                            bg= "#FFFFFF",
                            spacing="20px",
                            columns=[2, 2, 2, 2, 2, 2],
                        ),
                    ),  
                    aling="center" ,              
                    href="#",
                    is_external=False,
                ),
                style = styles.container_style
            )
            


def pintar_tipo(data) -> rx.Component:
    return  rx.image( 
        src= _imagen_tipo(data),
        alt= data
    )
def _imagen_tipo(tipo: str) -> (str):
    return "tipos/" + tipo + ".jpg"
