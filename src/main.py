from textnode import TextNode, TextType, text_node_to_html_node

def main():
    text_node = TextNode("Hello", TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    print(html_node)
    


if __name__ == "__main__":
    main()