from textnode import TextNode, TextType, text_node_to_html_node
from extract_markdown_links import extract_markdown_images, extract_markdown_links
from text_node_splitter import split_nodes_image, split_nodes_link, split_nodes_delimiter, text_to_textnodes

def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    print(nodes)



    


if __name__ == "__main__":
    main()