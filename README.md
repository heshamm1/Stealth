# Stealth - PDF XSS Tool


<div style="text-align:center">
 
```
          _______  _______  _______  _______  ___      _______  __   __   
          |       ||       ||       ||   _   ||   |    |       ||  | |  |
          |  _____||_     _||    ___||  |_|  ||   |    |_     _||  |_|  |
          | |_____   |   |  |   |___ |       ||   |      |   |  |       |
          |_____  |  |   |  |    ___||       ||   |___   |   |  |       |
           _____| |  |   |  |   |___ |   _   ||       |  |   |  |   _   |
          |_______|  |___|  |_______||__| |__||_______|  |___|  |__| |__|
                              Created By heshamm1
```
</div>



## Overview

Stealth is a tool that allows you to generate PDF files with custom JavaScript code for testing cross-site scripting (XSS) vulnerabilities. It's designed to demonstrate the potential security risks associated with executing JavaScript code embedded in PDF files.

## Features

- Customizable JavaScript code execution in PDFs.
- Web defacement option for including defacement JavaScript.
- Easy setup with a setup script.

## Prerequisites

- Python 3
- pip (Python package installer)

## Setup

Run the following command to set up the tool:

```bash
./setup.sh
```

## Usage

```bash
python stealth.py -o output_file.pdf -js "your_javascript_code_here"
```

## Options
`-o` , `--output`: Output PDF file name (required).

`-js`, `--javascript`: JavaScript code to be executed in the PDF.

`-r`, `--render`: Render the generated PDF in the default browser.

`-m`, `--metadata`: PDF metadata in the format '/Title (Title) /Author (Author) /Subject (Subject)'.

`--defacement`: Include web defacement JavaScript.

## Examples

Generate a PDF with custom JavaScript:

```
python stealth.py -o output.pdf -js "alert('XSS')"
```

Generate a PDF with web defacement JavaScript:

```bash
python stealth.py -o output_defaced.pdf -js "alert('XSS')" --defacement
```

