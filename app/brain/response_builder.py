class ResponseBuilder:
    """
    Builds the final response returned to the user.
    """

    def build(self, response):

        if response is None:

            return "No response generated."

        if isinstance(response, list):

            return "\n".join(str(item) for item in response)

        return str(response)