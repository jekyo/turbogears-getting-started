from tg import expose, TGController

class RootController(TGController):
    @expose()
    def index(self):
        return 'TurboGears app successfully deployed on Jekyo'

from tg import MinimalApplicationConfigurator

config = MinimalApplicationConfigurator()
config.update_blueprint({
    'root_controller': RootController()
})

application = config.make_wsgi_app()

from wsgiref.simple_server import make_server

print("Serving on port 4139...")
httpd = make_server('0.0.0.0', 4139, application)
httpd.serve_forever()