from tkinter import *


def set_status(text, color='black'):
    canvas.itemconfig(text_id, text=text, fill=color)
    pass
# Эта функция обновляет текстовую метку на холсте (Canvas), отображая текущее состояние игры.
# Она принимает два аргумента: text — текст, который будет отображён, и color — цвет текста (по умолчанию чёрный).

def key_handler(event):
    if event.keycode == KEY_UP:
        menu_up()
    if event.keycode == KEY_DOWN:
        menu_down()
    if event.keycode == KEY_ENTER:
        menu_enter()

    if game_over:
        return
    if event.keycode == KEY_PAUSE:
        pause_toggle()

    if pause:
        return
    if event.keycode == KEY_ESC:
        menu_toggle()

    if menu_mode:
        return

    set_status('Вперед!')
    if event.keycode == KEY_PLAYER1:
        canvas.move(player1, SPEED, 0)
    if event.keycode == KEY_PLAYER2:
        canvas.move(player2, SPEED, 0)

    check_finish()

    pass
# Функция обрабатывает нажатия клавиш. Если игра уже завершена (game_over=True), то дальнейшие события игнорируются. В противном случае:
#
# Текстовая метка обновляется сообщением «Вперед!».
# Если нажата клавиша управления игроком 1 (KEY_PLAYER1), фигура игрока 1 перемещается вправо со скоростью SPEED.
# Если нажата клавиша управления игроком 2 (KEY_PLAYER2), фигура игрока 2 также перемещается вправо со скоростью SPEED.
# После каждого перемещения вызывается функция check_finish(), чтобы проверить, достиг ли какой-то игрок финиша.

def check_finish():
    global game_over
    coords_player1 = canvas.coords(player1)
    coords_player2 = canvas.coords(player2)
    coords_finish = canvas.coords(finish_id)

    x1_right = coords_player1[2]
    x2_right = coords_player2[2]
    x_finish = coords_finish[0]

    if x1_right >= x_finish:
        set_status('Победа верхнего игрока', player1_color)
        game_over = True

    if x2_right >= x_finish:
        set_status('Победа нижнего игрока', player2_color)
        game_over = True
    pass
# Функция проверяет, достигли ли игроки финиша.
# Для этого она получает координаты обоих игроков и финишной линии.
# Затем сравнивает правую границу фигур игроков с левой границей финишной линии.
# Если хотя бы одна из фигур пересекла линию финиша, объявляется победитель соответствующего цвета,
# и игра считается завершённой (game_over=True).

# область глобальных переменных
game_width = 800
game_height = 800

KEY_UP = 87
KEY_DOWN = 83
KEY_ESC = 27
KEY_ENTER = 13
KEY_PLAYER1 = 39
KEY_PLAYER2 = 68
KEY_PAUSE = 19


player_size = 100
x1, y1 = 50, 50
x2, y2 = x1, y1 + player_size + 100
player1_color = 'red'
player2_color = 'blue'
x_finish = game_width - 50
SPEED = 12

game_over = False

window = Tk()
window.title('Меню игры')

canvas = Canvas(window, width=game_width, height=game_height, bg='white')
canvas.pack()
player1 = canvas.create_rectangle(x1,
                                  y1,
                                  x1 + player_size,
                                  y1 + player_size,
                                  fill=player1_color)
player2 = canvas.create_rectangle(x2,
                                  y2,
                                  x2 + player_size,
                                  y2 + player_size,
                                  fill=player2_color)
finish_id = canvas.create_rectangle(x_finish,
                                    0,
                                    x_finish + 10,
                                    game_height,
                                    fill='black')

text_id = canvas.create_text(x1,
                             game_height - 50,
                             anchor=SW,
                             font=('Arial', '25'),
                             text='Вперед!')


window.bind('<KeyRelease>', key_handler)
window.mainloop()
