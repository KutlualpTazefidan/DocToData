class TextBlock:
    def __init__(self, content, order):
        """
        Initializes a new instance of the TextBlock class.

        :param content: The textual content of the text block.
        :param order: The order or position of the text block within the document.
        """
        self.content = content
        self.order = order
        self.uri = f"http://example.org/textBlock/{order}"  # Unique identifier as a URI

    def to_rdf(self):
        """
        Converts the TextBlock instance to an RDF representation.

        :return: A string representing the RDF of this text block.
        """
        rdf = f"""
        <rdf:Description rdf:about="{self.uri}">
            <rdf:type rdf:resource="http://example.org/TextBlock"/>
            <content>{self.content}</content>
            <order>{self.order}</order>
        </rdf:Description>
        """
        return rdf


class Image:
    def __init__(self, path, order):
        """
        Initializes a new instance of the Image class.

        :param path: The file path or URL to the image.
        :param order: The order or position of the image within the document.
        """
        self.path = path
        self.order = order
        self.uri = f"http://example.org/image/{order}"  # Unique identifier as a URI

    def to_rdf(self):
        """
        Converts the Image instance to an RDF representation.

        :return: A string representing the RDF of this image.
        """
        rdf = f"""
        <rdf:Description rdf:about="{self.uri}">
            <rdf:type rdf:resource="http://example.org/Image"/>
            <path>{self.path}</path>
            <order>{self.order}</order>
        </rdf:Description>
        """
        return rdf