import sys


def periodic_table():
    print("This is the table")
    file = open('periodic_table.txt', 'r')
    elements = file.read().split('\n')
    print(elements[0])


    html_content = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Periodic Table</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <table>
                <tr>
                    <td>
                        <h4>Hydrogen</h4>
                        <ul>
                            <li>No 42</li>
                            <li>H</li>
                            <li>1.00794</li>
                        <ul>
                    </td>
                <tr>
            </table>
        <body>
    </html>
    """
    html_file = open("periodic_table.html", 'w')
    html_file.write(html_content)

    css_content="""
    td {
        border: 3px solid;
    }
    """
    css_file = open("style.css", 'w')
    css_file.write(css_content)
    
    
if __name__ == '__main__':
    try:
        periodic_table()
    except Exception as e:
        print("Error: ", e)
