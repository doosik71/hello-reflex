import reflex as rx


class State(rx.State):
    items: list[str] = ["Apple", "Banana", "Cherry"]


def render_item(item: rx.Var[str]):
    return rx.list.item(item)


def index():
    return rx.box(
        rx.foreach(State.items, render_item),
    )


app = rx.App()
app.add_page(index)
