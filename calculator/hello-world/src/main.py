import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    hoge = ft.Text("Hello-World", size=50, data=0)

    # ボタンがクリックされたときの処理
    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    def decrement_click(e):
        counter.data -= 1
        counter.value = str(counter.data)
        counter.update()

    # カウンターを増やすボタン
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )

    # SafeAreaで囲んで、デバイスのセーフエリアを考慮する
    page.add(
        ft.SafeArea(
            ft.Container(
                content=ft.Column(controls=[counter, hoge]),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=decrement_click)
        
    )


ft.app(main)
