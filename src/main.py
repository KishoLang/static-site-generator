from textnode import TextNode, TextType, text_node_to_html_node
from extract_markdown_links import extract_markdown_images, extract_markdown_links

def main():
    images_text = "This is text with a and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(images_text))

    links_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(links_text))
    
    images_text2 = ""
    print(extract_markdown_images(images_text2))

    


if __name__ == "__main__":
    main()