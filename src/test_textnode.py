import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.crooked.com")
        node2 = TextNode("This is another text node", TextType.ITALIC, "www.crooked.com")
        self.assertEqual(node.url, node2.url)

    def test_type(self):
        node = TextNode("This is a text node", TextType.CODE, "www.crooked.com")
        node2 = TextNode("This is another text node", TextType.CODE, "www.foxnews.com")
        self.assertEqual(node.text_type.value, node2.text_type.value)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node['tag'], None)
        self.assertEqual(html_node['value'], "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node["tag"], "img")
        self.assertEqual(html_node['value'], "")
        self.assertEqual(
            html_node['props'],
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node['tag'], "b")
        self.assertEqual(html_node['value'], "This is bold")

if __name__ == "__main__":
    unittest.main()