#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        replace_char_dict = {"<": "&lt", ">": "&rt", '"': "&quot", "\n": '\n<br />\n'}
        for key, value in replace_char_dict.items():
            text = super().__str__().replace(key, value)
        return text


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self, err_message="Element Validation Error"):
            super().__init__(err_message)

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.content = []
        if type(content) == list:
            self.content = content
        elif content is not None:
                self.content.append(content)
        self.tag_type = tag_type
        if tag_type != "double" and tag_type != "simple":
            raise self.ValidationError("Wrong Element Tag Type")

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = f"<{self.tag}{self.__make_attr()}>{self.__make_content()}</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"<{self.tag}{self.__make_attr} />"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            if (len(str(elem))):
                result += f"{elem}\n"
        result = " ".join(line for line in result.splitlines(True))
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError("Not right type")
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    try:
        html_page = Elem("html", {"lang": "en"}, content=[
                        Elem("head", content=[
                            Elem("title", content="\"Hello ground!\"")
                        ])
        ])
        print(html_page)
    except Exception as e:
        print("Error: ", e)
