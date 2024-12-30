from textnode import TextType, TextNode
from htmlnode import HTMLNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_node_text = node.text.split(delimiter)
            if len(split_node_text) % 2 == 0:
                raise Exception("Delimiter does not properly close")
            for i, split_text in enumerate(split_node_text):
                if i % 2 == 0: #even index
                    new_nodes.append(TextNode(split_text, TextType.TEXT))
                else: #odd index
                    new_nodes.append(TextNode(split_text, text_type))
    return new_nodes




            
