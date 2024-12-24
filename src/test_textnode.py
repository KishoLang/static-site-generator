import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is another text node", TextType.IMAGES, "www.boot.dev")
        node2 = TextNode("This is another text node", TextType.IMAGES, "www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is another text node", TextType.IMAGES, "www.boot.dev")
        node2 = TextNode("This is not another text node", TextType.IMAGES, "www.boot.dev")
        self.assertNotEqual(node, node2)

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode(props={
             "href": "https://www.google.com", 
             "target": "_blank",
            })
        html_prop = html_node.props_to_html()
        html_prop_answer =  ' href="https://www.google.com" target="_blank"'
        self.assertEqual(html_prop, html_prop_answer)

    

    


if __name__ == "__main__":
    unittest.main()