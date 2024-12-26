import reflex as rx


class State(rx.State):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1


def index():
    return rx.box(
        rx.heading("Count: "),
        rx.cond(
            State.count % 2 == 0,
            rx.text("Even"),
            rx.text("Odd"),
        ),
        rx.button(
            "Increment", on_click=State.increment
        ),
    )


app = rx.App()
app.add_page(index)
