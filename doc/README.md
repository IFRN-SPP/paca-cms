# CMS para Periódicos e Anais de Congressos Acadêmicos - Paca CMS

## Instalação

- Clone o projeto;

- Instale as dependências:

```bash
pip install -r requirements.txt
```

- Configure o sistema copiando o `.env.exemplo` para `.env` e realizando as alterações necessárias, como configurar as chaves do SUAP, informações do banco de dados, etc.;

- Faça as migrations:
```bash
python manage.py migrate
```

- Carregue a *fixture* inicial (inicializa o banco com um evento de exemplo e administrador padrão):
```bash
python manage loaddata initial.json
```

- Execute o servidor e acesse o sistema;

## Uso
- A interface de administração do sistema está em `/admin`.

- O acesso ao `/admin` se dá apenas para usuários com permissão de editor ou administrador.

- Na *fixture* inicial o usuário padrão é `admin@email.com` com a senha `1234`.

- A interface de *admin* do Django está em `/djangoadmin` e está disponível apenas no ambiente de desenvolvimento.

- Não há página de cadastro pública, apenas os administradores/editores têm acesso ao sistema. Novos usuários devem ser cadastrados por algum administrador.
