from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, otherNode):
        return (
            self.text == otherNode.text,
            self.text_type == otherNode.text_type,
            self.url == otherNode.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url}"

