import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 200))
pygame.display.set_caption("Music Player")

# Set up the font
myfont = pygame.font.SysFont(None, 30)   # None -> system's default font

# Set up the music
music_dir = "D:\Desktop\KBTU_PP2\PP2\lab7\music_player\songs"
songs = os.listdir(music_dir)
current_song = 0
# Load the first song
pygame.mixer.music.load(os.path.join(music_dir, songs[current_song]))

# Set up the keyboard commands
play_key = pygame.K_SPACE
stop_key = pygame.K_ESCAPE
next_key = pygame.K_RIGHT
prev_key = pygame.K_LEFT

# Start the music
pygame.mixer.music.play()

# Main loop
while True:
    screen.fill((10, 34, 10))
    songname = myfont.render(songs[current_song], True, "Red")
    screen.blit(songname,(10, 10))
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()            # cleans up resources used by Pygame
            quit()                   # exits the entire Python interpreter
        elif event.type == pygame.KEYDOWN:
            if event.key == play_key:
                pygame.mixer.music.unpause()
            elif event.key == stop_key:
                pygame.mixer.music.pause()
            elif event.key == next_key:
                current_song = (current_song + 1) % len(songs)
                pygame.mixer.music.load(os.path.join(music_dir, songs[current_song]))
                pygame.mixer.music.play()
            elif event.key == prev_key:
                current_song = (current_song - 1) % len(songs)
                pygame.mixer.music.load(os.path.join(music_dir, songs[current_song]))
                pygame.mixer.music.play()

    # Draw the screen
    text = myfont.render('Press Space to Play, Esc to Stop, Left/Right to Change Song', True, "white")
    screen.blit(text, (10, 50))
    pygame.display.update()
