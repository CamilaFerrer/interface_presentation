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

## Falta implementar

- Junção da aplicação com o srinfo;
- Editar possíveis erros após junção;

### Para realizar a junção

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