import cherrypy
import cherrypy_cors
import deli_pie as dp
import http.client
import json
import os
import os.path
import random
import string


@cherrypy.expose
class WebPageWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        'Servicio GET por si se requiere...'
        return str('data')

    @cherrypy.expose
    def POST(self, data_json):
        '''Servicio principal POST para obtener los resultados requeridos
        
        Args:
            data_json (json): json con las operaciones solicitadas

        Returns:
            json: json con los resultados de las operaciones solicitadas
        '''
        # 
        data = json.loads(data_json)
        fingers = dp.Fingers()
        operations = {
            'get_tables': fingers.get_tables
        }
        try:
            func = operations.get(data['operation'], lambda: {
                              'res': 'Error durante operación'})
        except KeyError:
            return json.dumps({'res': 'Operación inválida.'})
        response = {'res': func()}
        return json.dumps(response, ensure_ascii=False)


if __name__ == '__main__':
    cherrypy_cors.install()
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'cors.expose.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain'), ('Access-Control-Allow-Origin', '*')]
        }
    }
    cherrypy.config.update({'server.socket_host': '192.168.1.70'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.quickstart(WebPageWebService(), '/', conf)
