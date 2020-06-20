""" Some function I wish some xml library had """

from IPython.display import HTML
from lxml import etree


def render(xml):
    """ Similar to kora.json.render(s) 
    
    Accept both xml string or xml filename
    """
    if xml.endswith('.xml'): # a filename
        with open(xml) as f:
            xml = f.read()
            
    template = """
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/borsuksoftware/simpleXML/js/simpleXML.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/borsuksoftware/simpleXML/css/simpleXML.css">
    <script>
    $("#output-body").simpleXML({ 
        xmlString: "%s" 
    });
    </script>"""
    return HTML(template % xml
                          .replace('>\n','>')
                          .replace('"','\\"')
               )


def iterparse(source, tag=None, **kw):
    """ memory-efficient parsing for a big xml file
    
    Just etree.iterparse, with my favorite defaults 
    """
    for _, elem in etree.iterparse(source, ("end",), tag=tag, **kw):
        yield elem
        elem.clear()  # auto clear, so, must copy first
