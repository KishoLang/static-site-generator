import re

def markdown_to_blocks(markdown):
    list_of_blocks = []
    split_markdown = markdown.split("\n")
    current_block = ""
    for item in split_markdown:
        if item == "":
            if current_block != "":
                list_of_blocks.append(current_block.strip())
                current_block = ""
        else:
            if current_block == "":
                current_block = item
            else:
                current_block = current_block + "\n" + item
    if current_block != "":
        list_of_blocks.append(current_block.strip())
    return list_of_blocks

def block_to_block_type(single_md_block):
    match single_md_block:
        case _ if re.match(r"^#{1,6} +.*$", single_md_block):
            return "heading"
        case _ if re.match(r"^```[\s\S]*```$", single_md_block):
            return "code"
        case _ if re.match(r"^(> .*?(\n> .*?)*)$", single_md_block):
            return "quote"
        case _ if re.match(r"^(\* |\- )+.*(\n(\* |\- )+.*)*$", single_md_block):
            return "unordered_list"
        case _ if re.match(r"^(1\. .*(?:\n(?:\d+\. .*)?)*)$", single_md_block):
            expected_number = 1
            lines = single_md_block.split("\n")
            for i, line in enumerate(lines, 1):
                if not line.startswith(f"{i}. "):
                    return "paragraph"
            return "ordered_list"
        case _:
            return "paragraph"

