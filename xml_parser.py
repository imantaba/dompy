from xml.dom.minidom import parse, parseString, Node


def set_id_attribute(parent, attribute_name="id"):
    if parent.nodeType == Node.ELEMENT_NODE:
        if parent.hasAttribute(attribute_name):
            parent.setIdAttribute(attribute_name)
    for child in parent.childNodes:
        print(child)
        set_id_attribute(child, attribute_name)
        # print(f"'nodeType:'{parent.nodeType} 'element node:' {Node.ELEMENT_NODE}")



document = parse("smiley.svg")
set_id_attribute(document)
print(document.getElementById("skin"))