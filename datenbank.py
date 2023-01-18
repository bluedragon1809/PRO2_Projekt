import json
import plotly.express as px
from plotly.offline import plot


# read json file
def read():
    file = open("data/buecher.json")
    entries = json.load(file)
    return entries


def save(data):  # save new data
    file = open("data/buecher.json")
    entries = read()
    # dict structure for entries
    id_entry = entries[-1]["id"]
    entry = {
        "id": id_entry + 1,
        "title": data["title"],
        "author": data["author"],
        "genre": data["genre"],
        "bewertung": data["bewertung"],
    }
    entries.append(entry)  # new entry at the end of the dict
    entries_json = json.dumps(entries, indent=4)
    file = open("data/buecher.json", "w")
    file.write(entries_json)
    file.close()
    return


def entries_sorted(traits):  # filters entries
    entries = read()
    entries_filtered = []
    for entry in entries:
        # searches entries
        search = (
            traits["title"] == "" or entry["title"] == traits["title"],
            traits["author"] == "" or entry["author"] == traits["author"],
            traits["genre"] == "" or entry["genre"] == traits["genre"],
            traits["bewertung"] == "" or entry["bewertung"] == traits["bewertung"]
        )
        if all(search):
            entries_filtered.append(entry)
    return entries_filtered


def read_selected(entry_id):
    # used for editing and deleting selected entry
    for entry in read():
        if entry["id"] == entry_id:
            return entry
    return


# updated edited entries
def entry_corrected(entry_id, data):
    position = 0  # searches for the right position
    entries = read()
    entry_edited = {
        "id": entry_id,
        "title": data["title"],
        "author": data["author"],
        "genre": data["genre"],
        "bewertung": data["bewertung"],
    }

    for entry in entries:  # checks for edited entries
        if entry["id"] == entry_id:
            entries[position] = entry_edited
        else:
            position = position + 1

    entries_json = json.dumps(entries, indent=4)  # change data in json file
    file = open("data/buecher.json", "w")
    file.write(entries_json)
    file.close()
    return read_selected(entry_id)


def delete_entry(entry_id):  # update json
    entries = read()
    entries_01 = []  # for entries that haven't been deleted
    for entry in entries:
        if entry["id"] != entry_id:  # ! -> if entry is not to be deleted, will be added to list
            entries_01.append(entry)
    entries_json = json.dumps(entries_01, indent=4)
    file = open("data/buecher.json", "w")
    file.write(entries_json)
    file.close()
    return


# graph for analyse page
def draw_graph(range_x):
    entries = read()
    bewertungen = {}
    for entry in entries:
        if entry["bewertung"] not in bewertungen:
            bewertungen[entry["bewertung"]] = 1
        else:
            bewertungen[entry["bewertung"]] += 1

    genres = {}
    for entry in entries:
        if entry["genre"] not in genres:
            genres[entry["genre"]] = 1
        else:
            genres[entry["genre"]] += 1

    authors = {}
    for entry in entries:
        if entry["author"] not in authors:
            authors[entry["author"]] = 1
        else:
            authors[entry["author"]] += 1

    if range_x == "bewertung":
        x = bewertungen.keys()  # x = keys
        y = bewertungen.values()  # y = values
    elif range_x == "genre":
        x = genres.keys()
        y = genres.values()
    else:
        x = authors.keys()
        y = authors.values()

#  draw graph using plotly
    fig = px.bar(x=x, y=y,
                 color_discrete_sequence =['#007bff'])  # bars are in the same primary color as everything else
    div = plot(fig, output_type="div")
    return div




