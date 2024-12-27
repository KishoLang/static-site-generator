class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other):
        return isinstance(other, HTMLNode) and self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        return "".join(map(lambda key: f' {key}="{self.props[key]}"', self.props))
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = {}):
        super().__init__(tag = tag, value = value, props = props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError()
        if self.tag == None:
            return f"{str(self.value)}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, children = children, props = props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag")
        if self.children == None:
            raise ValueError("No value")
        result = ""
        for child in self.children:
            result = result + child.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"  
    