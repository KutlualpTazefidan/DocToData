class PDFContentAnalyzer:
    def __init__(self, keywords):
        """
        Initializes the analyzer with a set of keywords to look for in the text.

        :param keywords: A list of keywords that signify important content.
        """
        self.keywords = keywords

    def analyze_text_blocks(self, text_blocks):
        """
        Analyzes text blocks to determine their importance based on the presence of predefined keywords.

        :param text_blocks: A list of text blocks to analyze.
        :return: A list of tuples, each containing a text block and its importance score.
        """
        analyzed_results = []
        for text in text_blocks:
            score = self.calculate_importance(text)
            analyzed_results.append((text, score))
        return analyzed_results

    def calculate_importance(self, text):
        """
        Calculates the importance of a text block based on the number of keywords it contains.

        :param text: The text block to analyze.
        :return: An importance score based on the presence of keywords.
        """
        score = sum(text.count(keyword) for keyword in self.keywords)
        return score