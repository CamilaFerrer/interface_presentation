# Projeto

Este projeto busca a criação de um editor gratuito e online de apresentações do reveal.js para pessoas que não saibam HTML ao utilizar o Tiny MCE como editor.


## Implementado

- Tela administrativa;
- Criação de apresentações;
- Exclusão de apresentações;
- Atualização de apresentações;
- Visualização da apresentação;
- Criação de slides;
- Exclusão de slides;
- Atualização de slides;
- Pré-visualização individual de slide;

## Ferramentas

### Django

Django é um framework de desenvolvimento rápido para web escrito em Python, que utiliza o padrão model-template-view (MTV).

### Tiny MCE

O TinyMCE é um editor WYSIWYG com capacidade de converter campos de área de texto HTML, ou outros elementos HTML, em instâncias do editor. O TinyMCE foi projetado para integrar-se facilmente a bibliotecas JavaScript como React, Vue.js e AngularJS, bem como sistemas de gerenciamento de conteúdo como Joomla! E WordPress.

### Reveal JS

O reveal.js é um framework que permite facilmente criar belas apresentações usando HTML. Ele vem com uma ampla gama de recursos, incluindo slides aninhados, conteúdo Markdown, exportação de PDF, anotações de palestrantes e uma API JavaScript. Há também um editor visual completo e uma plataforma para compartilhar apresentações do reveal.js no site slides.com, porém essas funcionalidades são pagas.

## Requisitos para utilização

- Copiar pasta old_app/presentation para new_app/
- Copiar pasta old_app/static/revealjs  para new_app/static/
- Copiar pasta old_app/template/presentation para new_app/template/

- Em new_app/embrapii/settings.py adicionar:

```python
INSTALLED_APPS = [
    ...
    'presentations',
    'tinymce_4',
    'grappelli',
    'filebrowser',
    'widget_tweaks',
    ...
]

from filebrowser.sites import site
site.directory = ""
```

- Instalar os pacotes no seu ambiente virtual:

```bash
pip install -r requirements.txt
```

- Fazer as migrações e iniciar o app na porta 8080:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver localhost:8080
```
