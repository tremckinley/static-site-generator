from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
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
    
    def __eq__(self, other):
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return {"tag": None, "value": text_node.text}
    elif text_node.text_type == TextType.BOLD:
        return {"tag": "b", "value": text_node.text}
    elif text_node.text_type == TextType.ITALIC:
        return {"tag": "i", "value": text_node.text}
    elif text_node.text_type == TextType.CODE:
        return {"tag": "code", "value": text_node.text}
    elif text_node.text_type == TextType.LINK:
        return {
            "tag": "a",
            "props": {"href": text_node.url},
            "value": text_node.text,
        }
    elif text_node.text_type == TextType.IMAGE:
        return {
            "tag": "img",
            "props": {"src": text_node.url, "alt": text_node.text},
            "value": "",
        }
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")
