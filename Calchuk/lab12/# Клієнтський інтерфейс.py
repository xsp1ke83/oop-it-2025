# Клієнтський інтерфейс
class Player:
    def play(self):
        raise NotImplementedError()

# Клас з несумісним інтерфейсом
class OldMediaPlayer:
    def play_mp3(self):
        print("Грає MP3-файл")

# Адаптер
class MediaAdapter(Player):
    def __init__(self, old_player: OldMediaPlayer):
        self.old_player = old_player

    def play(self):
        # Адаптація методу
        self.old_player.play_mp3()

# Використання
if __name__ == "__main__":
    old = OldMediaPlayer()
    player = MediaAdapter(old)
    player.play()
