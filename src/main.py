from textnode import TextNode, TextType, text_node_to_html_node
from extract_markdown_links import extract_markdown_images, extract_markdown_links
from text_node_splitter import split_nodes_image, split_nodes_link, split_nodes_delimiter

def main():
    link_text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_links(link_text))

    # # node1 = TextNode(
    # # "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
    # # new_nodes = split_nodes_image([node1])
    # # print(new_nodes)



    # node2 = TextNode(
    # "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
    # new_link_nodes = split_nodes_link([node2])
    # print(new_link_nodes)


    


if __name__ == "__main__":
    main()