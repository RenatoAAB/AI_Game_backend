## Inside AI_Game_backend  
- __init__.py fala pro python que eh um package  
- asgi e wsgi são arquivos para configuração com o web server  
- settings.py tem varios apps, plugins, engines, etc  
- urls.py - configurar url roots  
- manage.py eh um especial que serve meio que p executar comandos  


## Inside core_persistence:  
- admin.py é pra registrar databases e models e usar no painel de admin  
- apps.py ?  
- models.py -- database models  
- tests.py são os testes  - estão testadas carta, deck, cardInDeck
- views.py -- criar views/roots pra acessar do website/jogo  
- templates - é uma página dedicada a html para mostrar melhor dados  
- serializers - é responsavel por serializar os dados - é possível criar todos os componentes a partir da view final de cardInDeck


## Comandos uteis

- python manage.py test <nome_do_app>  #para testar o app, executa os testes em tests.py
- python manage.py startapp <nome_do_app>
- python manage.py runserver - roda o servidor
- Ctrl+Shift+V é pra visualizar preview do markdown no VSCode


> toda vez que modificar qualquer model, é preciso fazer a migração
> - python manage.py makemigrations
> - python manage.py migrate


> Se deu BO na databse e vc pode reiniciá-la:
> - exclua todas as migrations da pasta
> - deleta a base de dados db.sqlite3
> - makemigrations && migrate
> - superuser, runserver
