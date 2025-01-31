import os
import yaml
import matplotlib.pyplot as plt

# daily note folder
FOLDER_NAME = "C:/Users/Ivan/Documents/Obsidian/Vault1/Daily"
IMAGE_FOLDER = "C:/Users/Ivan/Documents/Obsidian/Vault1/Files/attachments"

# get yaml section
def get_yaml_section(note):
    yaml_section = note.split("---")[1].strip()
    return yaml.safe_load(yaml_section)

# get mood pie chart
def get_mood_pie_chart(notes):
    labels = ['shit', 'bad', 'okay', 'good', 'great']
    colors = ['#e8685f', '#e39c5d', '#d4c222', '#20d42f', '#2ba9d6']
    sizes = [0]*5

    for note in notes:
        for i, label in enumerate(labels):
            if note['mood'] == label:
                sizes[i] += 1

    plt.figure(figsize=(8, 8), facecolor='#a19e9c')
    plt.rcParams['font.size'] = 18
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.legend()
    plt.savefig(os.path.join(IMAGE_FOLDER, "mood_pie_chart.png"))

# get mood graph
def get_mood_graph(notes):
    labels = ['shit', 'bad', 'okay', 'good', 'great']

    def evaluate_mood(note):
        note_mood = note['mood']
        for label in labels:
            if note_mood == label:
                return labels.index(label)

    mood_values = [evaluate_mood(note) for note in notes]

    # adjust x axis labels
    x_labels = ['']*len(notes)
    x_labels[0] = notes[0]['дата создания']
    x_labels[len(notes) - 1] = notes[len(notes) - 1]['дата создания']

    plt.figure(figsize=(8, 8), facecolor='#a19e9c')
    plt.rcParams['font.size'] = 18
    plt.gca().set_facecolor('#a19e9c')

    plt.plot([i + 1 for i in range(len(notes))], mood_values)
    plt.xticks([i + 1 for i in range(len(notes))], x_labels)
    plt.yticks([-1, 0, 1, 2, 3, 4, 5], [''] + labels + [''])
    plt.savefig(os.path.join(IMAGE_FOLDER, "mood_graph.png"))

# TODO:
# get productivity pie chart

# get activities bar chart



# read file data
notes_list = []

for file_name in os.listdir(FOLDER_NAME):
    with open(os.path.join(FOLDER_NAME, file_name), 'r', encoding="utf-8") as file:
        note = file.read()
        yaml_section = get_yaml_section(note)
        notes_list.append(yaml_section)

# create and save charts
get_mood_pie_chart(notes_list)
get_mood_graph(notes_list)