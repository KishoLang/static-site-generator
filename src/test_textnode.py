import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_repr(self):
        html_node = HTMLNode("p", "this is a test paragraph", children=None, props={"style": "font-size: 16px; color: black;"})
        repr_html_node = "HTMLNode(p, this is a test paragraph, None, {'style': 'font-size: 16px; color: black;'})"
        repr_html_test_node = html_node.__repr__()
        self.assertEqual(repr_html_test_node, repr_html_node)

    def test_eq(self):
        html_node1 = HTMLNode("p", "this is another test", children=None, props={"id": "parag"})
        html_node2 = HTMLNode("p", "this is another test", children=None, props={"id": "parag"})
        self.assertEqual(html_node1, html_node2)
    
    def test_eq2(self):
        html_node1 = HTMLNode("a", "this is another test", children=None, props={"id": "parag"})
        html_node2 = HTMLNode("p", "this is another test", children=None, props={"id": "parag"})
        self.assertNotEqual(html_node1, html_node2)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf_node1 = LeafNode("p", "This is a paragraph of text.")
        answer = "<p>This is a paragraph of text.</p>"
        self.assertEqual(answer, leaf_node1.to_html())
    
    def test_to_html2(self):
        leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        answer = """<a href="https://www.google.com">Click me!</a>"""
        self.assertEqual(answer, leaf_node2.to_html())

class TestParentNode(unittest.TestCase):
    def test_basic_case(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        test_case = node.to_html()
        expected_case = """<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>""" 
        self.assertEqual(test_case, expected_case)
    
    def test_nested_case(self):
        nested_node = ParentNode("div", [
            LeafNode("p", "First paragraph"),
            ParentNode("section", [
                LeafNode("h1", "Title"),
                ParentNode("article", [
                    LeafNode("p", "Article text"),
                    LeafNode("i", "Italic text")
                ]),
                LeafNode("footer", "Footer text")
            ]),
            LeafNode("p", "Last paragraph")
        ])
        test_case = nested_node.to_html()
        expected_case = """<div><p>First paragraph</p><section><h1>Title</h1><article><p>Article text</p><i>Italic text</i></article><footer>Footer text</footer></section><p>Last paragraph</p></div>"""
        self.assertEqual(test_case, expected_case)

    def test_no_children(self):
        node = ParentNode("div", [])
        test_case = node.to_html()
        expected_case = """<div></div>""" 
        self.assertEqual(test_case, expected_case)
    
    def test_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "text")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_none_as_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_deep_nested(self):
        node = ParentNode("div", [
            LeafNode(None, "plain text"),
            ParentNode("p", [
                LeafNode(None, "more text"),
                LeafNode("span", "spantext")
            ])
        ])
        test_case = node.to_html()
        expected_case = """<div>plain text<p>more text<span>spantext</span></p></div>"""
        self.assertEqual(test_case, expected_case)

    def test_multiple_parent_nodes(self):
        node = ParentNode("main", [
            ParentNode("nav", [
                LeafNode("a", "Link")
            ]),
            ParentNode("div", [
                LeafNode("p", "Para")
            ])
        ])
        test_case = node.to_html()
        expected_case = """<main><nav><a>Link</a></nav><div><p>Para</p></div></main>"""
        self.assertEqual(test_case, expected_case)
    


if __name__ == "__main__":
    unittest.main()