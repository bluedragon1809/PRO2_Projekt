from flask import Flask, render_template, request, redirect
# import from datenbank.py
from datenbank import read, save, entries_sorted, read_selected, entry_corrected, \
    delete_entry, draw_graph

app = Flask("Bücherverwaltung")


@app.route("/")  # whenever / is inserted in the URL it will lead to the homepage
def home():
    return render_template("index.html")


# erfassen page gets the data and post is inorder to get the form data
@app.route('/erfassen', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("erfassen.html")
    if request.method == "POST":
        data_entries = request.form.to_dict()
        save(data_entries)
        return redirect("/uebersicht")  # saves data to uebersicht


@app.route("/uebersicht", methods=["GET", "POST"])
def summary():
    # creating filter option
    entries = read()
    list_title = [result['title'] for result in entries]  # list for every title will be created
    list_title = sorted(list_title)

    list_author = [result['author'] for result in entries]  # list for every author will be created
    list_author = set(list_author)
    list_author = sorted(list_author)

    list_genre = [result['genre'] for result in entries]  # list for every genre will be created
    list_genre = set(list_genre)
    list_genre = sorted(list_genre)

    # creating choice of options
    title = list_title
    author = list_author
    genre = list_genre
    bewertung = ["1", "2", "3", "4", "5"]

    if request.method == "GET":  # shows all books in uebersicht
        entries = read()
    if request.method == "POST":  # shows chosen options after filtering
        entries = entries_sorted(request.form.to_dict())
    return render_template("uebersicht.html", titles=title, authors=author, genres=genre, bewertungen=bewertung,
                           entries=entries)


@app.route("/edit/<entry_id>", methods=["GET", "POST"])
def modify(entry_id):
    if request.method == "GET":  # selected entry can be edited
        entry = read_selected(int(entry_id))
        return render_template("edit.html", entry=entry)
    if request.method == "POST":  # changes will be saved to json file
        entry_corrected(int(entry_id), request.form.to_dict())
        return redirect("/uebersicht")


@app.route("/delete/<entry_id>", methods=["GET", "POST"])  # delete entry
def remove(entry_id):  # entry will be deleted with the help of id
    delete_entry(int(entry_id))
    return redirect("/uebersicht")


# Route Statistiken
@app.route("/analyse", methods=["GET", "POST"])
def graph():
    if request.method == "GET":
        return render_template("analyse.html")
    if request.method == "POST":
        range_x = request.form.to_dict()["x-axis"]
        div = draw_graph(range_x)

        # different titles according to chosen data
        if range_x == "bewertung":
            diagram_title = "Alle Bewertungen:"
        elif range_x == "author":
            diagram_title = "Alle Authoren:"
        else:
            diagram_title = "Alle Genres:"

        return render_template("analyse.html", barchart=div, diagram_title=diagram_title)


if __name__ == "__main__":
    app.run(debug=True)  # ensures not to rerun the server every time a change has been made
