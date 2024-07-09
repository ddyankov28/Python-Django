import sys


def periodic_table():
    print("This is the table")
    file = open('periodic_table.txt', 'r')
    elements = file.read().split('\n')
    table_rows = "<tr>"
    current_position = 0
    for element in elements:
        if element.strip():
            components = element.split(',')
            position = int(components[0].split(':')[1].strip())
            name = components[0].split('=')[0].strip()
            atomic_number = components[1].split(':')[1].strip()
            symbol = components[2].split(':')[1].strip()
            atomic_mass = components[3].split(':')[1].strip()
            print(f"Position: {position}")
            print(f"Current position: {current_position}")
        
            if position == 0 and current_position != 0:
                table_rows += "</tr><tr>"
            
            while current_position < position:
                table_rows += "<td></td>"
                current_position += 1
                
            table_rows += f"""
            <td>
                <h4>{name}</h4>
                <ul>
                    <li>No {atomic_number}</li>
                    <li>{symbol}</li>
                    <li>{atomic_mass}</li>
                </ul>
            </td>
            """
        current_position = position + 1
    
    table_rows += "</tr>"
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Periodic Table</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <table>
                {table_rows}
            </table>
        <body>
    </html>
    """
    html_file = open("periodic_table.html", 'w')
    html_file.write(html_content)

    css_content="""
    table {
        border-collapse: collapse;
    }
    td {
        border: 3px solid;
        width: 100px;
        height: 100px;
        text-align: center;
        vertical-align: middle;
    }
    ul {
        list-style-type: none;
        padding: 0;
        margin: 0
    }
    """
    css_file = open("style.css", 'w')
    css_file.write(css_content)
    
    
if __name__ == '__main__':
    try:
        periodic_table()
    except Exception as e:
        print("Error: ", e)
