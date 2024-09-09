from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='html', attr=attr)


class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='head', attr=attr)


class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='body', attr=attr)


class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='title', attr=attr)
        

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='meta', tag_type='simple', attr=attr)


class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='img', tag_type='simple', attr=attr)
        

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='table', attr=attr)


class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='th', attr=attr)
        

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='tr', attr=attr)


class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='td', attr=attr)


class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='ul', attr=attr)
        
class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='ol', attr=attr)


class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='li', attr=attr)


class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='h1', attr=attr)


class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='h2', attr=attr)


class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='p', attr=attr)

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content)


class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(content=content, tag='span', attr=attr)


# Thematic break, horizontal rule
class Hr(Elem):
    def __init__(self, content):
        super().__init__(content=content, tag='hr', tag_type='simple')


class Br(Elem):
    def __init__(self, content):
        super().__init__(content=content, tag='br', tag_type='simple')


if __name__ == "__main__":
    try:
        print( Html( [Head(), Body()] ) )
        print("-------------------------------------")
        
        html_file = open("html_file.html", "w")
        html_content = (Html([
                            Head([
                                Title( Text("Django Piscine")),
                                Meta(None,{"charset": "UTF-8"})
                                ]),
                            Body([  Img(None, {"src": "https://avatars.githubusercontent.com/u/118269569?v=4"}),
                                    Table([
                                        Tr([
                                            Th(Text("Table Header")),
                                            Th(Text("Table Header"))
                                           ]),
                                        Tr([Td(Text("Data")),
                                            Td(Text("Data"))
                                          ]) 
                                         ]),
                                    Ul([Text("Unordered List"),
                                        Li(Text("Item 1")),
                                        Li(Text("Item 2"))
                                      ]),
                                    Ol([Text("Ordered List"),
                                        Li(Text("Ordered List item 1")),
                                        Li(Text("Ordered List item 2"))
                                      ]),
                                    H1(Text("This is a h1 Heading")),
                                    H2(Text("This is a h2 Heading")),
                                    P([Text("This is a paragraph"),
                                       Span(
                                           Text("with blue color from a span"),
                                           {"style": "color:blue"}
                                           ),
                                       Text("inside it")
                                     ]),
                                    Div([Text("This is a div"),
                                         Hr(None),
                                         Text("with thematic break and"),
                                         Br(None),
                                         Text("a line break")
                                       ])
                                ])
                            ])
                       )
        html_file.write(html_content.__str__())
        html_file.close()
        
        example_html = Html([Head(Text('"Hello ground!"')),
                             Body([H1(Text('"Oh no, not again!"')),
                                   Img(None, {"src": "http://i.imgur.com/pfp3T.jpg"})
                                 ])
                           ])
        print(example_html)
    except Exception as e:
        print("Error: ", e)