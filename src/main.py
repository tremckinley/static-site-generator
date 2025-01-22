from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = HTMLNode(tag="div", value="Hello, World!", props={"id": "main", "class": "container"})
    node2 = HTMLNode(tag="div", value="Hello, World!", props={"id": "main", "class": "container"})
    print(node.props_to_html(), node2.props_to_html())
    print(node.__repr__ == node2.__repr__)

main()