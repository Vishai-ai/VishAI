from app.brain.response_builder import ResponseBuilder

builder = ResponseBuilder()

print(builder.build("Hello"))

print("----------------")

print(

    builder.build(

        [

            "Open Chrome",

            "Open YouTube",

            "Done"

        ]

    )

)