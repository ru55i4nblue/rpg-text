import tkinter as tk
from tkgui.window import Window
import io
from rpglib.game import Game
from rpglib.utils import parse_dice_format


game = Game()


def loop():
    global game
    game.next_turn()


def new_game():
    global game
    p_name = "Dogeek"
    p_job = "warrior"
    game.player.name = p_name
    game.player.job = p_job
    game.player.health_rolls.append(parse_dice_format(game.player.job.hp_die))
    game.player.mana_rolls.append(parse_dice_format(game.player.job.mp_die))
    game.player.stats.randomize()
    game.player.health = game.player.max_health


def on_click(event):
    print("Clicked!")


new_game()

root = tk.Tk()
window = Window(root, loop=loop)
window.pack()

with io.open("assets/screens/game", encoding='utf-8') as f:
    for i, line in enumerate(f):
        window.print(line, (0, i))

window.print(game.player.name, (50, 1))

# window.button('CLICK', (10, 4), on_click)

root.mainloop()