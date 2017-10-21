from cement.core.controller import CementBaseController, expose
from cement.core.foundation import CementApp


class TemplateController(CementBaseController):
    class Meta:
        label = 'base'
        arguments = [
            (['-f', '--foo'],
             dict(action='store', help='The foo option')),
        ]

    @expose(help='Help for some-function')
    def some_function(self):
        self.app.log.info("Doing something")


class TemplateApp(CementApp):
    class Meta:
        label = 'CliTemplate'
        base_controller = 'base'
        handlers = [TemplateController]
