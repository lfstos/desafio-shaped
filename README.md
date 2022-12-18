# desafio-shaped
Desafio para a vaga de Backend da Shaped


Clonando o projeto:
```console
git clone git@github.com:lfstos/desafio-shaped.git
```

Configurando o ambiente
```console
cd desafio-shaped
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Para rodar o projeto:
```console
python manage.py runserver
```

Para acessar os links do Paciente:

URL base:
```console
/localhost:8000/paciente/
```

Listando todos pacientes:
Método GET
```console
/localhost:8000/paciente/
```
Listando um paciente:
Método GET
```console
/localhost:8000/paciente/<id>/
```

Criando um paciente:
Método POST
```console
/localhost:8000/paciente/
```

Editando um paciente:
Método PUT
```console
/localhost:8000/paciente/<id>/
```

Excluindo um paciente:
Método DELETE
```console
/localhost:8000/paciente/<id>/
```

Para acessar os links do Exames:

Listando todos exames de um paciente:
Método GET
```console
/localhost:8000/exame/<id_do_paciente>/
```

Criando um exame:
Método POST
```console
/localhost:8000/exame/
```

Editando um exame:
Método PUT
```console
/localhost:8000/exame/<id>/
```

Excluindo um exame:
Método DELETE
```console
/localhost:8000/exame/<id>/
```