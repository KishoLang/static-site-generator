from textnode import TextNode, TextType

def main():
    node = TextNode("This is some text", TextType.BOLD, "https://boot.dev")
    other_node = TextNode("This is some text", TextType.BOLD, "https://boot.dev")
    print(TextNode.__repr__(node))
    print(TextNode.__eq__(node, other_node))

if __name__ == "__main__":
    main()