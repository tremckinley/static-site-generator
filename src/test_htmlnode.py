import unittest
from htmlnode import HTMLNode, LeafNode

class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = HTMLNode(tag="div", value="Hello, World!", props={"id": "main", "class": "container"})
        node2 = HTMLNode(tag="div", value="Hello, World!", props={"id": "main", "class": "container"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(tag="div", value="Hello, World!", props={"id": "main", "class": "container"})
        self.assertEqual(node.props_to_html(), ' id="main" class="container"')

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello, World!", props={"id": "main", "class": "container"})
        self.assertEqual(node.__repr__(), "HTMLNode(div, Hello, World!, {'id': 'main', 'class': 'container'})")

    def test_leaf(self):
        leaf = LeafNode(tag="a", value="Click Here for more", props={"href": "https://www.crooked.com"})
        expected_html = '<a href="https://www.crooked.com">Click Here for more</a>'
        self.assertEqual(leaf.to_html(), expected_html)

    def test_leaf_no_tag(self):
        leaf = LeafNode(tag=None, value="Click Here for more", props={"href": "https://www.crooked.com"})
        expected_html = 'Click Here for more'
        self.assertEqual(leaf.to_html(), expected_html)

    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            leaf = LeafNode(tag="a", value=None, props={"href": "https://www.crooked.com"})

    if __name__ == "__main__":
        unittest.main()