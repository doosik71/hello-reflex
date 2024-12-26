import reflex as rx


class LoginState(rx.State):
    logged_in: bool = False

    @rx.event
    def toggle_login(self):
        self.logged_in = not self.logged_in


def index():
    return rx.box(
        rx.cond(
            LoginState.logged_in,
            rx.heading("Logged In"),
            rx.heading("Not Logged In"),
        ),
        rx.button(
            "Toggle Login", on_click=LoginState.toggle_login
        ),
    )


app = rx.App()
app.add_page(index)
