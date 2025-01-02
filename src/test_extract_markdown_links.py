import unittest

from extract_markdown_links import extract_markdown_links, extract_markdown_images


# What kinds of test cases do you think would be important to verify? Consider:

# Empty strings
class TestExtractMarkdownLinks(unittest.TestCase):
    def test_empty_string(self):
        image_text = ""
        test_result = extract_markdown_images(image_text)
        expected_result = []
        self.assertEqual(test_result, expected_result)
    
    def test_empty_link(self):
        image_text = "This is text"
        test_result = extract_markdown_images(image_text)
        expected_result = []
        self.assertEqual(test_result, expected_result)
    
    def test_multiple_images(self):
        image_text = "This is text with a and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)![anakin sky](https://i.imgur.com/fJRm4Vk.jpeg)"
        test_result = extract_markdown_images(image_text)
        expected_result = [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg'), ('anakin sky', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(test_result, expected_result)
    
    def test_multiple_links(self):
        link_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        test_result = extract_markdown_links(link_text)
        expected_result = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(test_result, expected_result)    
    

# Text with no links/images
# Multiple links/images
# Links and images mixed together
# Edge cases with special characters in the alt text or URLs


if __name__ == "__main__":
    unittest.main()