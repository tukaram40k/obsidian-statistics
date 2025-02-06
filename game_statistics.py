import os
import yaml
import matplotlib.pyplot as plt

GAMES_FOLDER = "C:/Users/Ivan/Documents/Obsidian/Vault1/Personal/Для души/Games/Played Games"

PLOT_BACKGROUND_COLOR = '#b5b1ae'
GENRE_COLORS = ['#e8685f', '#e39c5d', '#d4c222', '#20d42f', '#2ba9d6', '#d64b7c', '#ff7f50', '#8a2be2', '#3cb371', '#ffd700', '#e8685f', '#e39c5d', '#d4c222', '#20d42f', '#2ba9d6', '#d64b7c', '#ff7f50', '#8a2be2', '#3cb371', '#ffd700']

# get yaml section
def get_yaml_section(note):
    yaml_section = note.split("---")[1].strip()
    return yaml.safe_load(yaml_section)

# get game genres
def get_genres_bar_chart(notes, colors):
    genres = []
    for note in notes:
        if note['genre']:
            for genre in note['genre']:
                if genre not in genres:
                    genres.append(genre)

    sizes = [0]*len(genres)
    for note in notes:
        if note['genre']:
            for genre in note['genre']:
                index = genres.index(genre)
                sizes[index] += 1

    plt.figure(figsize=(8, 8), facecolor=PLOT_BACKGROUND_COLOR)
    plt.rcParams['font.size'] = 18
    plt.bar(genres, sizes)
    plt.show()

# read file data
notes_list = []

for file_name in os.listdir(GAMES_FOLDER):
    with open(os.path.join(GAMES_FOLDER, file_name), 'r', encoding="utf-8") as file:
        note = file.read()
        print(note)
        yaml_section = get_yaml_section(note)
        notes_list.append(yaml_section)

get_genres_bar_chart(notes_list, GENRE_COLORS)