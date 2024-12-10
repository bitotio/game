from tkinter import *


def set_status(text, color='black'):
    pass
# Эта функция обновляет текстовую метку на холсте (Canvas), отображая текущее состояние игры.
# Она принимает два аргумента: text — текст, который будет отображён, и color — цвет текста (по умолчанию чёрный).

def key_handler(event):
    pass
# Функция обрабатывает нажатия клавиш. Если игра уже завершена (game_over=True), то дальнейшие события игнорируются. В противном случае:
#
# Текстовая метка обновляется сообщением «Вперед!».
# Если нажата клавиша управления игроком 1 (KEY_PLAYER1), фигура игрока 1 перемещается вправо со скоростью SPEED.
# Если нажата клавиша управления игроком 2 (KEY_PLAYER2), фигура игрока 2 также перемещается вправо со скоростью SPEED.
# После каждого перемещения вызывается функция check_finish(), чтобы проверить, достиг ли какой-то игрок финиша.

def check_finish():
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
