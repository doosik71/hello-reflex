import reflex as rx


class State(rx.State):
    count: int = 0
    text_input: str = ""
    items: list[str] = []
    selected_color: str = "blue"

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1

    @rx.event
    def reset_count(self):
        self.count = 0

    @rx.event
    def update_text(self, value: str):
        self.text_input = value

    @rx.event
    def add_item(self):
        if self.text_input.strip():
            self.items.append(self.text_input.strip())
            self.text_input = ""

    @rx.event
    def remove_item(self, index: int):
        if 0 <= index < len(self.items):
            self.items.pop(index)
    
    @rx.event
    def remove_item_by_index(self, index: int):
        return self.remove_item(index)

    @rx.event
    def change_color(self, color: str):
        self.selected_color = color


def counter_section():
    return rx.box(
        rx.heading("카운터 예제", size="6", margin_bottom="20px"),
        rx.text(f"현재 카운트: {State.count}", font_size="20px", margin_bottom="10px"),
        rx.cond(
            State.count % 2 == 0,
            rx.text("짝수", color="green", font_weight="bold"),
            rx.text("홀수", color="red", font_weight="bold"),
        ),
        rx.hstack(
            rx.button("증가", on_click=State.increment, color_scheme="green"),
            rx.button("감소", on_click=State.decrement, color_scheme="red"),
            rx.button("리셋", on_click=State.reset_count, color_scheme="gray"),
            spacing="4",
        ),
        padding="20px",
        border="1px solid #ddd",
        border_radius="10px",
        margin_bottom="30px",
    )


def input_section():
    return rx.box(
        rx.heading("입력 및 리스트 관리", size="6", margin_bottom="20px"),
        rx.hstack(
            rx.input(
                placeholder="항목을 입력하세요...",
                value=State.text_input,
                on_change=State.update_text,
                width="300px",
            ),
            rx.button("추가", on_click=State.add_item, color_scheme="blue"),
            spacing="4",
            margin_bottom="20px",
        ),
        rx.cond(
            State.items.length() > 0,
            rx.vstack(
                rx.text("목록:", font_weight="bold"),
                rx.foreach(
                    State.items,
                    lambda item, index: rx.hstack(
                        rx.text(f"{index + 1}. {item}"),
                        rx.button(
                            "삭제",
                            on_click=State.remove_item_by_index(index),
                            size="1",
                            color_scheme="red",
                        ),
                        justify="between",
                        width="100%",
                    ),
                ),
                spacing="2",
            ),
            rx.text("목록이 비어있습니다.", color="gray"),
        ),
        padding="20px",
        border="1px solid #ddd",
        border_radius="10px",
        margin_bottom="30px",
    )


def styling_section():
    return rx.box(
        rx.heading("스타일링 예제", size="6", margin_bottom="20px"),
        rx.hstack(
            rx.button(
                "파란색",
                on_click=State.change_color("blue"),
                color_scheme="blue",
            ),
            rx.button(
                "빨간색",
                on_click=State.change_color("red"),
                color_scheme="red",
            ),
            rx.button(
                "초록색",
                on_click=State.change_color("green"),
                color_scheme="green",
            ),
            spacing="4",
            margin_bottom="20px",
        ),
        rx.box(
            rx.text(
                f"선택된 색상: {State.selected_color}",
                font_size="18px",
                font_weight="bold",
                color=State.selected_color,
            ),
            padding="20px",
            background_color=f"{State.selected_color}.100",
            border_radius="10px",
            border=f"2px solid {State.selected_color}",
        ),
        padding="20px",
        border="1px solid #ddd",
        border_radius="10px",
        margin_bottom="30px",
    )


def components_section():
    return rx.box(
        rx.heading("기본 컴포넌트 예제", size="6", margin_bottom="20px"),
        rx.vstack(
            rx.text("일반 텍스트입니다.", font_size="16px"),
            rx.text("굵은 텍스트입니다.", font_weight="bold", color="purple"),
            rx.text("이탤릭 텍스트입니다.", font_style="italic"),
            rx.divider(),
            rx.badge("뱃지", color_scheme="purple"),
            rx.divider(),
            rx.hstack(
                rx.button("기본 버튼", size="1"),
                rx.button("중간 버튼", size="2", color_scheme="teal"),
                rx.button("큰 버튼", size="3", color_scheme="orange"),
                spacing="4",
            ),
            rx.divider(),
            rx.link("Reflex 공식 문서", href="https://reflex.dev", color="blue"),
            spacing="4",
        ),
        padding="20px",
        border="1px solid #ddd",
        border_radius="10px",
        margin_bottom="30px",
    )


def index():
    return rx.center(
        rx.box(
            rx.heading("Reflex 사용법 예제", size="9", text_align="center", margin_bottom="40px"),
            components_section(),
            counter_section(),
            input_section(),
            styling_section(),
            max_width="800px",
            margin_top="50px",
        )
    )


app = rx.App()
app.add_page(index)
