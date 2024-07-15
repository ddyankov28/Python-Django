import sys
from settings import *

def render():
    assert len(sys.argv) == 2, "Wrong number of arguments"
    file1 = open(sys.argv[1], "r")
    template_content = file1.read()
    globals_dict = globals()
    template_content = template_content.format(**globals_dict)
    
    html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>CV</title>
            </head>
            <body style="background-color: rgb(207, 250, 250);
                         text-align: center">
                {template_content}
            </body>
        </html>
        """
    html_file = open("myCVtemplate.html", 'w')
    html_file.write(html_content)



if __name__ == '__main__':
    try:
        render()
    except Exception as e:
        print("Error: ", e)
