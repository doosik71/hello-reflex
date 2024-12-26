import reflex as rx


class CounterState(rx.State):
    count: int = 0

    @rx.event
    def increment(self, amount: int):
        self.count += amount


def index() -> rx.Component:
    return rx.hstack(
        rx.heading(CounterState.count),
        rx.button(
            "Increment by 1",
            on_click=lambda: CounterState.increment(1),
        ),
        rx.button(
            "Increment by 5",
            on_click=lambda: CounterState.increment(5),
        ),
    )


app = rx.App()
app.add_page(index)
