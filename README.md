# PDF Finder

This Python script is designed to search for specific text in multiple PDF files within a directory.

## Requirements

- pdfminer.six library

## Installation

1. Clone the repository or download the script directly.
2. Install the required dependencies by running the following command:

```python
pip install pdfminer.six
```

## Usage

1. Place your PDF files in the `pdfs` directory within the project folder.
2. Open the script in a Python IDE or editor.
3. Modify the `what_to_find` variable with the desired text you want to search for within the PDF files.
4. Run the script.

The script will search through all the PDF files in the `pdfs` directory and print the file paths of the PDFs that contain the specified text.

Note: Make sure to update the `path` variable if the location of the `pdfs` directory is different.

## Example

Suppose you have a directory named `pdfs` with multiple PDF files. You want to find PDF files containing the text "Gdańsk University of Technology". You can modify the `what_to_find` variable in the script with the desired text and run it. The script will search through the PDF files and print the file paths of the matching PDFs.
