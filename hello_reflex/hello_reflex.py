import reflex as rx


class CounterState(rx.State):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1


def index() -> rx.Component:
    return rx.hstack(
        rx.heading(CounterState.count),
        rx.button(
            "Increment", on_click=CounterState.increment
        ),
    )


app = rx.App()
app.add_page(index)
