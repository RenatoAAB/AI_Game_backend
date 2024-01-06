Inside AI_Game_backend
-- __init__.py fala pro python que eh um package
-- asgi e wsgi são arquivos para configuração com o web server
-- settings.py tem varios apps, plugins, engines, etc
-- urls.py - configurar url roots
-- manage.py eh um especial que serve meio que p executar comandos


Inside core_persistence:
-- admin.py é pra registrar databases e models e usar no painel de admin
-- apps.py ?
-- models.py -- database models
-- tests.py são os testes
-- views.py -- criar views/roots pra acessar do website/jogo
-- templates - é uma página dedicada a html para mostrar melhor dados
-- serializers - é responsavel por serializar os dados


Comandos uteis

python manage.py test <nome_do_app>  #para testar o app, executa os testes em tests.py
python manage.py startapp <nome_do_app>
python manage.py runserver - roda o servidor

toda vez que eu modificar qualquer model, é preciso fazer a migração
-- python manage.py makemigrations
-- python manage.py migrate