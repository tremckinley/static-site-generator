import unittest

from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()