import reflex as rx
import reflex_pokedex.utils as utils
import reflex_pokedex.styles.styles as  styles

from reflex_pokedex.components.navbar import navbar
from reflex_pokedex.components.footer import footer
from reflex_pokedex.components.titulo import titulo
from reflex_pokedex.data.list_pokemon import Pokemon

@rx.page(
    title=utils.title_index,
    description=utils.description_index,
    image=utils.preview_index,
    meta=utils.meta_index,
    route='/detalle/[pid]'
)

# class PokemonState(rx.State):
#      @rx.var
#      def post_id(self) -> str:
#         args = self.router.page.params
#         usernames = args.get('pid', [])
#         return usernames

def detalle() -> rx.Component:
    nuevo_pokemon = Pokemon()
    nuevo_pokemon.obtener_datos_de_pokeapi('metapod')
    #nuevo_pokemon.obtener_datos_de_pokeapi(PokemonState.post_id())
    
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        utils.lang(),
        navbar(),
        #rx.heading(PokemonState.post_id),
        rx.heading("DETALLE"),
        rx.heading(nuevo_pokemon.nombre),
        rx.heading(nuevo_pokemon.url),
        footer(),
        spacing=styles.Size.VERY_BIG.value,
        width="100%"
    )
        

