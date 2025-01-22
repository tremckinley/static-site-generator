import unittest
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = HTMLNode(tag="div", value="Hello, World!", props={"id": "main", "class": "container"})
        node2 = HTMLNode(tag="div", value="Hello, World!", props={"id": "main", "class": "container"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(tag="div", value="Hello, World!", props={"id": "main", "class": "container"})
        self.assertEqual(node.props_to_html(), 'id="main" class="container"')

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello, World!", props={"id": "main", "class": "container"})
        self.assertEqual(node.__repr__(), {'id': 'main', 'class': 'container'})

    if __name__ == "__main__":
        unittest.main()