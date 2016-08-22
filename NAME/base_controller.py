from cement.core.controller import CementBaseController, expose

class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = "Does some stuff"
        arguments = [
                ( ['-f', '--foo'],
                    dict(action='store', help='Does foo stuff') ),
                ]

    @expose(hide=True)
    def default(self):
        self.app.log.info('You probably want to run the -h command')

    @expose(help="This does a thing")
    def thing(self):
        self.app.log.debug("Inside thing")
        if self.app.pargs.foo:
            self.app.log.debug("Option: foo => %s" % self.app.pargs.foo)
