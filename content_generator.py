import tkinter as tk
import wikipedia as wiki
from tkinter import *
import csv
import sys


def generate_text_terminal():
    # If user runs program using the terminal and an input csv file, this function will parse the input csv file to find
    # which keywords to use and then write output content into a csv file entitled output.csv
    with open('input.csv', 'r') as file:
        reader = csv.reader(file)
        header_row = next(reader)
        input_row = next(reader)
        input_row = input_row[0].split(';')
        print(input_row)
    primary_keyword = input_row[0]
    secondary_keyword = input_row[1]
    page = (wiki.page(primary_keyword))
    paragraphs = (page.content.split('\n'))
    for paragraph in paragraphs:
        if str(primary_keyword) in paragraph and str(secondary_keyword) in paragraph:
            print(paragraph)
            with open('output.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["input_keywords", "output_content"])
                writer.writerow([(primary_keyword + ";" + secondary_keyword), paragraph])
            return


def generate_text_gui():
    primary_keyword = e1.get()
    secondary_keyword = e2.get()
    page = (wiki.page(primary_keyword))
    paragraphs = (page.content.split('\n'))
    for paragraph in paragraphs:
        if str(primary_keyword) in paragraph and str(secondary_keyword) in paragraph:
            text_label.config(text=paragraph)
            with open('output.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["input_keywords", "output_content"])
                writer.writerow([(primary_keyword + ";" + secondary_keyword), paragraph])
            return

# Check if a second argument was passed when the program was run through the terminal, if so, generate text without
# going into the GUI. If the argument wasn't passed, create the GUI and use the user input for keywords.
if len(sys.argv) > 1:
    generate_text_terminal()
else:
    master = tk.Tk()
    master.geometry("700x700")

    tk.Label(master, text="Primary Keyword: ").grid(row=0)
    tk.Label(master, text="Secondary Keyword: ").grid(row=1)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='Generate Text', command=generate_text_gui).grid(row=3, column=1, sticky=tk.W, pady=4)

    global text_label
    text_label = Message(master, text='Text will appear here')
    text_label.grid(row=5, column=0, sticky=NSEW)
    text_label.grid_columnconfigure(0, weight=1)
    text_label.grid_rowconfigure(0, weight=1)



    master.mainloop()

    tk.mainloop()