from app.planner.task import Task


class TaskFactory:

    @staticmethod
    def open_app(name):

        return Task(

            action="open_app",

            target=name

        )

    @staticmethod
    def wait(seconds):

        return Task(

            action="wait",

            value=seconds

        )

    @staticmethod
    def type_text(text):

        return Task(

            action="type",

            value=text

        )

    @staticmethod
    def browser(site, value=None):

        return Task(

            action="browser",

            target=site,

            value=value

        )