import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from text_node_splitter import split_nodes_delimiter


class TestSplitNodesFunc(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expexted_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(expexted_result, new_nodes)
    
    def test_unmatched_delimiters(self):
        node = TextNode("some **bold text", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_italic(self):
        node = TextNode("This is text with *italic text part* words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expexted_result = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("italic text part", TextType.ITALIC),
            TextNode(" words", TextType.TEXT),
        ]
        self.assertEqual(expexted_result, new_nodes)

    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expexted_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(expexted_result, new_nodes)



if __name__ == "__main__":
    unittest.main()