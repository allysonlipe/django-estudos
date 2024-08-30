# Tarefa Django

## Objetivo

Modifique a aplicação Django para atender aos seguintes requisitos:

### 1. Modificar a View da Rota Principal
- Modifique a view associada à rota raiz (`'/'`) para que ela retorne a mensagem: **"HelloWorld"**.

### 2. Organizar Templates
- Crie uma pasta chamada `templates` na raiz do seu app Django.
- Mova os arquivos `primeiro.html`, `segundo.html`, `terceiro.html` e `quarto.html` para dentro dessa pasta `templates`.

### 3. Criar Novas Rotas e Renderizar Templates
- Crie 4 novas rotas no arquivo `urls.py` de seu app Django.
  - Cada rota deve renderizar um dos arquivos HTML (`primeiro.html`, `segundo.html`, `terceiro.html`, `quarto.html`) que foram movidos para a pasta `templates`.
- Utilize o método `render` nas views associadas a essas rotas para retornar os templates correspondentes.

### 4. Modificar os Arquivos HTML
- Em cada um dos arquivos HTML (`primeiro.html`, `segundo.html`, `terceiro.html`, `quarto.html`):
  - Adicione as tags necessárias para que as disciplinas sejam exibidas em listas não ordenadas (`<ul>` e `<li>`).

## Observações
- Certifique-se de que o Django esteja configurado corretamente para localizar os templates na pasta `templates`.
- Verifique se todas as rotas estão funcionando conforme o esperado após as modificações.
