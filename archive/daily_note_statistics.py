import os
import yaml
import matplotlib.pyplot as plt

# daily note folder
FOLDER_NAME = "C:/Users/Ivan/Documents/Obsidian/Vault1/Daily"
IMAGE_FOLDER = "C:/Users/Ivan/Documents/Obsidian/Vault1/Files/attachments"

PLOT_BACKGROUND_COLOR = '#b5b1ae'

MOOD_LABELS = ['shit', 'bad', 'okay', 'good', 'great']
MOOD_COLORS = ['#e8685f', '#e39c5d', '#d4c222', '#20d42f', '#2ba9d6']

PRODUCTIVITY_COLORS = ['#e8685f', '#d4c222', '#2ba9d6']
PRODUCTIVITY_LABELS = ['работал', 'всё-понемногу', 'отдыхал']

ACTIVITY_COLORS = ['#e8685f', '#e39c5d', '#d4c222', '#20d42f', '#2ba9d6', '#d64b7c', '#ff7f50', '#8a2be2', '#3cb371', '#ffd700']

# get yaml section
def get_yaml_section(note):
    yaml_section = note.split("---")[1].strip()
    return yaml.safe_load(yaml_section)

# get mood pie chart
def get_mood_pie_chart(notes, labels, colors):
    sizes = [0]*len(labels)

    for note in notes:
        for i, label in enumerate(labels):
            if note['mood'] == label:
                sizes[i] += 1

    plt.figure(figsize=(8, 8), facecolor=PLOT_BACKGROUND_COLOR)
    plt.rcParams['font.size'] = 18
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.legend()
    plt.savefig(os.path.join(IMAGE_FOLDER, "mood_pie_chart.png"))

# get mood graph
def get_mood_graph(notes, labels):
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

    plt.figure(figsize=(8, 8), facecolor=PLOT_BACKGROUND_COLOR)
    plt.rcParams['font.size'] = 18
    plt.gca().set_facecolor(PLOT_BACKGROUND_COLOR)

    plt.plot([i + 1 for i in range(len(notes))], mood_values)
    plt.xticks([i + 1 for i in range(len(notes))], x_labels)
    plt.yticks([-1, 0, 1, 2, 3, 4, 5], [''] + labels + [''])
    plt.savefig(os.path.join(IMAGE_FOLDER, "mood_graph.png"))

# get productivity pie chart
def get_productivity_pie_chart(notes, labels, colors):
    sizes = [0]*len(labels)
    for note in notes:
        for i, label in enumerate(labels):
            if note['что делал'] == label:
                sizes[i] += 1

    plt.figure(figsize=(8, 8), facecolor=PLOT_BACKGROUND_COLOR)
    plt.rcParams['font.size'] = 18
    plt.pie(sizes, labels=labels, colors=colors[:len(sizes)], autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.legend()
    plt.savefig(os.path.join(IMAGE_FOLDER, "productivity_pie_chart.png"))

# get activities bar chart
def get_activities_bar_chart(notes, colors):
    labels = []

    for note in notes:
        for activity in note['чем занимался']:
            if activity not in labels:
                labels.append(activity)

    sizes = [0] * len(labels)

    for note in notes:
        for activity in note['чем занимался']:
            index = labels.index(activity)
            sizes[index] += 1

    plt.figure(figsize=(8, 8), facecolor=PLOT_BACKGROUND_COLOR)
    plt.rcParams['font.size'] = 18
    plt.gca().set_facecolor(PLOT_BACKGROUND_COLOR)
    bars = plt.bar(range(len(labels)), sizes, color=colors[:len(labels)])

    # Add legend instead of x-ticks
    plt.legend(bars, labels, title="Activities", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks([])
    plt.title('Activities Distribution')
    plt.xlabel('Activities')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGE_FOLDER, "activities_bar_chart.png"))

# TODO:
# sort notes by date properly
# add linear regression to mood graph



# read file data
notes_list = []

for file_name in os.listdir(FOLDER_NAME):
    with open(os.path.join(FOLDER_NAME, file_name), 'r', encoding="utf-8") as file:
        note = file.read()
        yaml_section = get_yaml_section(note)
        notes_list.append(yaml_section)

# create and save charts
get_mood_pie_chart(notes_list, MOOD_LABELS, MOOD_COLORS)
get_mood_graph(notes_list, MOOD_LABELS)
get_productivity_pie_chart(notes_list, PRODUCTIVITY_LABELS, PRODUCTIVITY_COLORS)
get_activities_bar_chart(notes_list, ACTIVITY_COLORS)