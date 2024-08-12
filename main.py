import time
import sys
import combat
ascii_art = """
░▒▓██████████████▓▒░ ░▒▓██████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓███████▓▒░▒▓████████▓▒░
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░   ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░  ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░  ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░   ░▒▓█▓▒░
                                                             ░▒▓█▓▒░
                                                              ░▒▓██▓▒░
"""
print(ascii_art)
def typewriter_print(text, delay=0.02):
    lines = text.split('\n')
    for line in lines:
        padded_line = f"{' ' * 5}{line}"
        for char in padded_line:
            sys.stdout.write(char)
            sys.stdout.flush()  
            time.sleep(delay)   
        print() 
        time.sleep(delay)

text = """In the ancient land of Numeria, once a realm of vibrant knowledge and harmony, darkness has spread its shadow.
The sacred Math Crystals, revered like the jewels of ancient temples, have been shattered by the malevolent sorcerer Malfus.
This once-flourishing land, where the art of mathematics was intertwined with the rich traditions and wisdom of its people,
now faces confusion and chaos.As the sacred chants and mathematical hymns lose their power, you, the chosen Math Samurai, 
rise to restore the ancient balance.Armed with a mystical sword inscribed with the symbols of forgotten sages, your journey
begins in the serene Village of Simplex.Here, amidst the echoes of ancient mantras and the vibrant colors of festival banners,
your quest unfolds.You will traverse through enchanted realms reminiscent of India's majestic landscapes, solve puzzles inspired
by age-old knowledge, and confront formidable guardians of wisdom.The fate of Numeria, like the tales of old, rests in your hands.
Will you reclaim the Math Crystals and restore peace to this storied land? Your epic adventure begins now."""

typewriter_print(text)
if __name__ == "__main__":
    boss =combat.Boss("Solving Linear Equations")
    battle = combat.BossBattle(boss)
    battle.fight()
