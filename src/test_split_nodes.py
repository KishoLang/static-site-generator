import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from text_node_splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_node_converstion(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        test_result = text_to_textnodes(text)
        expected_result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(expected_result, test_result)



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

class TestSplitLinkFunc(unittest.TestCase):
    def test_standard_link_split(self):
        node = TextNode(
         "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
        test_result = split_nodes_link([node])
        expected_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(expected_result, test_result)
    
    def test_no_links(self):
        node = TextNode("This is text with no links in it", TextType.TEXT)
        test_result = split_nodes_link([node])
        expected_result = [node]  # Should return original node
        self.assertEqual(expected_result, test_result)
    
    def test_text_starts_with_link(self):
        node = TextNode(
         "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
        test_result = split_nodes_link([node])
        expected_result = [
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(expected_result, test_result)

class TestSplitImageFunc(unittest.TestCase):
    def test_standard_image_split(self):
        node = TextNode(
         "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
        test_result = split_nodes_image([node])
        expected_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(expected_result, test_result)
    
    def test_no_images(self):
        node = TextNode("This is text with no images in it", TextType.TEXT)
        test_result = split_nodes_image([node])
        expected_result = [node]  # Should return original node
        self.assertEqual(expected_result, test_result)
        



if __name__ == "__main__":
    unittest.main()