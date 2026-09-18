import tkinter as tk
from tkinter import ttk
from tkextrafont import Font
import pyperclip

def copy_citation(citation):
    """
    Copies the citation onto the user's clipboard

    Args:
        citation(str)
    """
    pyperclip.copy(citation)

def get_entry(want_clear, style_type):
    """
    Outputs and clears the citation based on the style type

    Args:
        want_clear(bool)
        style_type(str)
    """

    # List where citation features are added
    f.config(state="normal")
    f.delete(1.0, tk.END)

    # Temporary list that will hold all the citation features
    temp_list = []
    
    if style_type == "MLA":

        author = f"{ln.get()}, {fn.get()}"
        temp_list.insert(1, author)

        ititle = f"{variables["ititle"][0].get()}"
        temp_list.insert(3, ititle)

        title = f"{variables["title"][0].get()}"
        temp_list.insert(4, title)

        edition = f"{variables["edition"][0].get()}"
        temp_list.insert(7, edition)

        institution = f"{variables["institution"][0].get()}"
        temp_list.insert(14, institution)

        type = f"{variables["type"][0].get()}"
        temp_list.insert(10, type)

        album = f"{variables["album"][0].get()}"
        temp_list.insert(11, album)

        issue = f"{variables["issue"][0].get()}"
        temp_list.insert(9, issue)

        source = f"{variables["source"][0].get()}"
        temp_list.insert(12, source)

        isource = f"{variables["isource"][0].get()}"
        temp_list.insert(13, isource)

        episode = f"{variables["episode"][0].get()}"
        temp_list.insert(6, episode)

        pub = f"{variables["pub"][0].get()}"
        temp_list.insert(15, pub)

        ipub = f"{variables["ipub"][0].get()}"
        temp_list.insert(16, ipub)

        volume = f"{variables["volume"][0].get()}"
        temp_list.insert(8, volume)
        
        location = f"{variables["city"][0].get()}, {variables["country"][0].get()}"
        temp_list.insert(18, location)

        time = f"{date.get()}"
        temp_list.insert(2, time)

        pages = f"{variables["sp"][0].get()}-{variables["ep"][0].get()}"
        temp_list.insert(17, pages)

        doi = f"{variables["doi"][0].get()}"
        temp_list.insert(19, doi)

        link = f"{url.get()}"
        temp_list.insert(20, link)

        accessed = f"{variables["accessed"][0].get()}"
        temp_list.insert(21, accessed)

        formats_m = {
            
        author : "n",
        ititle : "*i*",
        title : "n",
        pub: "n",
        ipub: "*i*",
        episode : "n",
        edition : "n",
        volume : "*i*",
        issue : "*i*",
        type: "n",
        source : "n",
        isource : "*i*",
        album : "n",
        location : "n",
        institution : "c",
        time : "n",
        pages : "pp.",
        doi : "n",
        link: "n",
        accessed: "a"

        }

    else:

        author = f"{ln.get()}, {fn.get()[0]}"
        temp_list.insert(1, author)

        time = f"{date.get()}"
        temp_list.insert(2, time)

        ititle = f"{variables["ititle"][0].get()}"
        temp_list.insert(3, ititle)

        title = f"{variables["title"][0].get()}"
        temp_list.insert(4, title)
        years = f"{variables["sy"][0].get()}-{variables["ey"][0].get()}"
        temp_list.insert(5, years)

        episode = f"{variables["episode"][0].get()}"
        temp_list.insert(6, episode)

        edition = f"{variables["edition"][0].get()}"
        temp_list.insert(7, edition)

        volume = f"{variables["volume"][0].get()}"
        temp_list.insert(8, volume)

        # Issue and volume are sometimes the same
        issue = f"{variables["issue"][0].get()}"
        temp_list.insert(9, issue)

        type = f"{variables["type"][0].get()}"
        temp_list.insert(10, type)

        album = f"{variables["album"][0].get()}"
        temp_list.insert(11, album)

        source = f"{variables["source"][0].get()}"
        temp_list.insert(12, source)

        isource = f"{variables["isource"][0].get()}"
        temp_list.insert(13, isource)

        institution = f"{variables["institution"][0].get()}"
        temp_list.insert(14, institution)

        pub = f"{variables["pub"][0].get()}"
        temp_list.insert(15, pub)

        ipub = f"{variables["ipub"][0].get()}"
        temp_list.insert(16, ipub)

        pages = f"{variables["sp"][0].get()}-{variables["ep"][0].get()}"
        temp_list.insert(17, pages)

        location = f"{variables["city"][0].get()}, {variables["country"][0].get()}"
        temp_list.insert(18, location)

        doi = f"{variables["doi"][0].get()}"
        temp_list.insert(19, doi)

        link = f"{url.get()}"
        temp_list.insert(20, link)

        accessed = f"{variables["accessed"][0].get()}"
        temp_list.insert(21, accessed)

        formats_a = {
                
            author : "n",
            ititle : "*i*",
            title : "n",
            pub: "n",
            ipub: "*i*",
            episode : "(b)",
            edition : "n",
            volume : "*i*",
            issue : "*i*",
            type: "[sb]",
            source : "n",
            isource : "*i*",
            album : "n",
            location : "n",
            institution : "*i*",
            time : "(b)",
            pages : "(pp.)",
            years : "(b)",
            doi : "n",
            link: "n",
            accessed: "a"

        }

    if want_clear:
        for j in variables:
            variables[j][0].delete(0, tk.END)

        ln.delete(0, tk.END)
        fn.delete(0, tk.END)
        date.delete(0, tk.END)
        url.delete(0, tk.END)

    else:
        if style_type == "MLA":
             for i in temp_list:

                if i != "" and i != ", " and i != "-":
                    if formats_m[i] == "n":
                        f.insert(tk.END, i + ". ")
                    elif formats_m[i] == "c":
                        f.insert(tk.END, i + ", ")
                    elif formats_m[i] == "*i*":
                        f.insert(tk.END, f"*{i}*. ")
                    elif formats_m[i] == "(b)":
                        f.insert(tk.END, f"({i}). ")
                    elif formats_m[i] == "pp.":
                        f.insert(tk.END, f"pp. {i}. ")
                    elif formats_m[i] == "a":
                        f.insert(tk.END, f"Accessed {i}")

        else:
            for i in temp_list:

                if i != "" and i != ", " and i != "-":
                    if formats_a[i] == "n":
                        f.insert(tk.END, i + ". ")
                    elif formats_a[i] == "*i*":
                        f.insert(tk.END, f"*{i}*. ")
                    elif formats_a[i] == "(b)":
                        f.insert(tk.END, f"({i}). ")
                    elif formats_a[i] == "[sb]":
                        f.insert(tk.END, f"[{i}]. ")
                    elif formats_a[i] == "(pp.)":
                        f.insert(tk.END, f"(pp. {i}). ")
                    elif formats_a[i] == "a":
                        f.insert(tk.END, f"Accessed {i}")
            



    f.config(state="disabled")


def select_type(event):
    option = sourcetype.get(sourcetype.curselection())

    for widget in fields.winfo_children():
        widget.grid_remove()

    i = 0
    fields_used = sourcetypes[option]
    for field in fields_used:
        i += 1
        tk.Label(fields, text=field).grid(row=i, column=0)
        for j, widget in enumerate(variables[fields_used[field]]):
            widget.grid(row=i, column=j + 1)


root = tk.Tk()
root.title("Citation Machine")
root.geometry(f"960x720")

# THIS SETS THE FONT
font = Font(file="fonts/sniglet.ttf", family="Sniglet")
root.option_add("*Font", "Sniglet 10")

# Change window display
root.title("Citation Machine")
root_img = tk.PhotoImage(file = 'assets/lockedin_mascot.png')
root.wm_iconphoto(False, root_img)

root.option_add('*Button.Background', "#64c5ba")
root.option_add('*Button.Foreground', 'white')
root.option_add('*OptionMenu.background', '#64c5ba')
root.option_add('*OptionMenu.foreground', 'white')
root.option_add('*Entry.background', '#64c5ba')
root.option_add('*Entry.foreground', 'white')
root.option_add("*Menu*Background", "#64c5ba")
root.option_add('*Label.background', '#64c5ba')
root.option_add('*Label.foreground', 'white')
root.option_add('*Frame.background', '#64c5ba')


root.title("Lockedin Citation")

# Stops the user from entering full screen
root.resizable(False, False) 

bg = tk.PhotoImage(file = "assets/g_citations.png")
bg_label = tk.Label(root, image = bg)
bg_label.place(x = 0, y = 0)

general = tk.Frame(root)
general.grid(row=1, column=0)

bg2 = tk.PhotoImage(file = "assets/g_citations.png")
bg2_label = tk.Label(general, image = bg2)
bg2_label.place(x = 0, y = 0)

fields = tk.Frame(root)
fields.grid(row=8, column=0)


"""
Every field has
- Label
- Entry
- variable

{"variable": [Label, Entry]}
"""

variables = {
    "author": [tk.Entry(fields)],
    "ititle": [tk.Entry(fields)],
    "title": [tk.Entry(fields)],
    "subtitle": [tk.Entry(fields)],
    "pub": [tk.Entry(fields)],
    "ipub": [tk.Entry(fields)],
    "episode": [tk.Entry(fields)],
    "edition": [tk.Entry(fields)],
    "volume": [tk.Entry(fields)],
    "issue": [tk.Entry(fields)],
    "type": [tk.Entry(fields)],
    "source": [tk.Entry(fields)],
    "isource": [tk.Entry(fields)],
    "album": [tk.Entry(fields)],
    "city": [tk.Entry(fields)],
    "country": [tk.Entry(fields)],
    "institution": [tk.Entry(fields)],
    "date": [tk.Entry(fields)],
    "sp": [tk.Entry(fields)],
    "ep": [tk.Entry(fields)],
    "sy": [tk.Entry(fields)],
    "ey": [tk.Entry(fields)],
    "doi": [tk.Entry(fields)],
    "accessed": [tk.Entry(fields)],
}

sourcetypes = {
    "Book": {
        "Title": "ititle",
        "Subtitle": "subtitle",
        "Publisher": "pub",
        "Edition": "edition",
        "Volume": "volume",
        "DOI": "doi"
    },

    "Article": {
        "Article title": "title",
        "Journal name": "isource",
        "Volume No.": "volume",
        "Issue No.": "issue",
        "Start page": "sp",
        "End page": "ep",
        "DOI": "doi"
    },

    "Website": {
        "Page title": "ititle",
        "Website name": "source",
        "Date accessed": "accessed"
    },

    "Blog post": {
        "Post title": "title",
        "Blog name": "isource",
        "Publisher": "ipub",
        "Date accessed": "accessed",
    },

    "Social media": {
        "Post title": "ititle",
        "Content": "ititle",
        "Website name": "source",
        "Date accessed": "accessed"
        
    },

    "Video": {
        "Video title": "ititle",
        "Website name": "source"
    },

    "Artwork": {
        "Title": "ititle",
        "Medium": "type",
        "Museum or source": "source",
        "City": "city",
        "Country": "country"
    },

    "Image": {
        "Title or description": "title",
        "Medium": "type",
        "Source": "source"
    },

    "Music": {
        "Title": "title",
        "Album": "album",
        "Label": "source"
    }, 

    "Podcast": {
        "Podcast title": "isource",
        "Episode title": "title",
        "Episode number": "episode",
        "Year started": "sy",
        "Year ended": "ey",
        "Production company": "source",
    },

    "Presentation": {
        "Title": "ititle",
        "Type of presentation": "type",
        "Title of conference": "source",
        "City": "city",
        "Country": "country"
    },

    "Thesis or dissertation": {
        "Title": "ititle",
        "Institution": "institution",
        "Source name": "source"
    }
}

sourcetype = tk.Listbox(general, listvariable=tk.Variable(value=list(sourcetypes.keys())), selectmode="browse", height=len(sourcetypes), exportselection=False)
sourcetype.bind("<<ListboxSelect>>", select_type)
sourcetype.grid(row=1, column=0, padx=40, pady=40)

"""
style = tk.ttk.Combobox(general, values=["APA", "MLA"])
style.bind("<<ComboboxSelected>>", select_style)
style.grid(row=2, column=0)
"""


tk.Label(general, text="Author's first name").grid(row=4, column=2)
tk.Label(general, text="Author's last name").grid(row=5, column=2)
tk.Label(general, text="Publication date").grid(row=4, column=4)
tk.Label(general, text="URL").grid(row=5, column=4)


fn = tk.Entry(general)
fn.grid(row=4, column=3)

ln = tk.Entry(general)
ln.grid(row=5, column=3)

date = tk.Entry(general)
date.grid(row=4, column=5)

url = tk.Entry(general)
url.grid(row=5, column=5)

textframe = tk.Frame(general)
textframe.grid(row=1, column=2)

chosen_style = tk.StringVar(general, "Style...")


f = tk.Text(textframe, wrap="word", width=20, height=10, state="disabled")
f.grid(row=0, column=0)

style = tk.OptionMenu(textframe, chosen_style, "APA", "MLA")
style.grid(row=1, column=0, padx=10, pady=10)

button = tk.Button(general, text="Update", command=lambda:get_entry(False, chosen_style.get()))
button.grid(row=7, column=2, padx=10, pady=10)

clear = tk.Button(general, text="Clear", command=lambda:get_entry(True, chosen_style.get()))
clear.grid(row=11, column=2, padx=10, pady=6)
    
copy = tk.Button(general, text="Copy Citation", command=lambda:copy_citation(f.get("1.0", "end-1c")))
copy.place(x=450, y=210)


root.mainloop()
