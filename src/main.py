from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    node = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")
    print(node)


if __name__ == main():
    main()