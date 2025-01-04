from textnode import TextType, TextNode
from htmlnode import HTMLNode
from extract_markdown_links import extract_markdown_links, extract_markdown_images

def text_to_textnodes(text):
    text_node = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(text_node, "**", TextType.BOLD), "*", TextType.ITALIC), "`", TextType.CODE) 
    return split_nodes_link(split_nodes_image(nodes))


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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        current_text = node.text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            extracted_images = extract_markdown_images(current_text)
            for image in extracted_images:
                parts = current_text.split(f"![{image[0]}]({image[1]})", 1)
                if parts[0] != "":
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                current_text = parts[1]
            if current_text != "":
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        current_text = node.text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            extracted_links = extract_markdown_links(current_text)
            for link in extracted_links:
                parts = current_text.split(f"[{link[0]}]({link[1]})", 1)
                if parts[0] != "":
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                if len(parts) > 1:
                    current_text = parts[1]
            if current_text != "":
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes


            
