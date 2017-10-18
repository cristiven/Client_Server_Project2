from channels.staticfiles import StaticFilesConsumer
from chat import consumers
from channels.routing import route

channel_routing = {
    # Esto hace que Django sirva archivos estáticos desde settings.STATIC_URL, similar
	# a django.views.static.serve. Esto no es ideal (no exactamente la producción
	# calidad) pero funciona para un ejemplo mínimo.
    'http.request': StaticFilesConsumer(),

    # Conecte los canales websocket a nuestros consumidores:
    'websocket.connect': consumers.ws_connect,
    'websocket.receive': consumers.ws_receive,
    'websocket.disconnect': consumers.ws_disconnect,
}

	