import unittest

from handle_blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_case_one(self):
        input_md = "# Heading\n\nThis is a paragraph"
        test_result = markdown_to_blocks(input_md)
        expected_result = ["# Heading", "This is a paragraph"]
        self.assertEqual(expected_result, test_result)
    
    def test_case_two(self):
        input_md = "# Heading\n\n\n\nThis is a paragraph"  # multiple blank lines
        test_result = markdown_to_blocks(input_md)
        expected_result = ["# Heading", "This is a paragraph"]
        self.assertEqual(expected_result, test_result)
    
    def test_case_three(self):
        input_md = "* List item 1\n* List item 2\n\nParagraph text"
        test_result = markdown_to_blocks(input_md)
        expected_result = ["* List item 1\n* List item 2", "Paragraph text"]
        self.assertEqual(expected_result, test_result)

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block(self):
        # Test heading
        self.assertEqual(
            block_to_block_type("# Simple heading"),
            "heading"
        )
        
        # Test code block
        self.assertEqual(
            block_to_block_type("```\nsome code\n```"),
            "code"
        )
        
        # Test quote
        self.assertEqual(
            block_to_block_type("> some quote\n> more quote"),
            "quote"
        )
        
        # Test unordered list
        self.assertEqual(
            block_to_block_type("* item 1\n* item 2"),
            "unordered_list"
        )
        
        # Test ordered list
        self.assertEqual(
            block_to_block_type("1. first\n2. second"),
            "ordered_list"
        )

        # Valid ordered list
        self.assertEqual(
            block_to_block_type("1. First\n2. Second\n3. Third"),
            "ordered_list"
        )
        
        # Invalid ordered list (numbers out of sequence)
        self.assertEqual(
            block_to_block_type("1. First\n3. Second\n4. Third"),
            "paragraph"
        )
        
        # Invalid ordered list (doesn't start with 1)
        self.assertEqual(
            block_to_block_type("2. First\n3. Second"),
            "paragraph"
        )
        
        # Invalid ordered list (missing space after period)
        self.assertEqual(
            block_to_block_type("1.First\n2.Second"),
            "paragraph"
        )
        
        # Test paragraph
        self.assertEqual(
            block_to_block_type("just some\nregular text"),
            "paragraph"
        )


if __name__ == "__main__":
    unittest.main()