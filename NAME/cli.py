from base_controller import BaseController
from cement.core.foundation import CementApp

class NAME(CementApp):
    class Meta:
        label = 'NAME'
        base_controller = 'base'
        handlers = [BaseController]

with NAME() as app:
    app.run()

