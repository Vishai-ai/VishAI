class CommandPipeline:
    """
    Executes the complete command processing pipeline.
    """

    def __init__(
        self,
        detector,
        parser,
        dispatcher,
        response_builder,
    ):
        self.detector = detector
        self.parser = parser
        self.dispatcher = dispatcher
        self.response_builder = response_builder

    def process(self, command: str):

        intent = self.detector.detect(command)

        action = self.parser.parse(command)

        result = self.dispatcher.dispatch(intent)

        return self.response_builder.build(result)