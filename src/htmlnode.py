class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method is not implemented yet")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " " + " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        if self.value == None:
            raise ValueError("value cannot be blank")

        
    def to_html(self):
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        if self.children is None:
            raise ValueError("Parent Nodes must have 'children'.")
        if self.tag is None:
            raise ValueError("The 'tag' argument is required for Parent Nodes.")
        
    def to_html(self):
        child_text = ""
        for child in self.children:
            child_text += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_text}</{self.tag}>"

