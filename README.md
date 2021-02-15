# Content Generator

This content generator takes a primary and secondary keyword, either from the user inputting it through Tkinter GUI or by reading an input.csv file. Then, using the Wikipedia API, the program finds the Wikipedia article that has the primary keyword as a title. Then, the program searches through the article to return the first paragraph that has both the primary and the secondary keyword within the paragraph and then writes the paragraph to an output.csv file.

## Installation

Use the python package manager [pip](https://pip.pypa.io/en/stable/) to install the following dependencies. The program also uses the csv and sys modules which should already be built into Python.

```bash
pip install tkinter
pip install wikipedia

```

## Usage

If you'd like to run the program directly from the terminal, set up an input.csv file within the same folder as the content_generator.py file that has 'input_keywords' as the header and two colon-separated keywords as the first non-header cell in the next row (beagle;dog). Run the program using this command:

```bash
python content_generator.py input.csv
```

If you'd like to run the program using the Tkinter general user interface, simply enter
```bash
python content_generator.py
```
and follow the instructions on the general user interface.

## GIF Walkthroguh

![Alt Text](https://media.giphy.com/media/AqhLI3Zrv5i8ksK4qF/giphy.gif)


