# CMS para Periódicos e Anais de Congressos Acadêmicos - Paca CMS

Esse é um sistema desenvolvido em Django como um CMS (*Content Management System*) específico para periódicos online, como anais de eventos científicos/acadêmicos, atendendo aos requisitos para obtenção de ISSN (*Internacional Standard Serial Number*).

O sistema conta com autenticação via SUAP para usuários do IFRN.

## Requisitos para o ISSN

Para ser atribuído o ISSN a publicação deverá ter uma URL própria e deverá ser única para todas as edições. A revista eletrônica deve garantir e cuidar dos aspectos relativos à preservação digital, como também garantir a preservação da URL que permite o acesso à mesma.
 
A página principal da publicação, além de apresentar o título em destaque, sem contar designação numérica do evento deverá conter links para:

- Apresentação;
- Normas para publicação;
- Corpo editorial/Comissão organizadora/Expediente;
- Edições (com área de numeração para cada edição);
- Contato (constando o nome e endereço completo da instituição responsável pela publicação.)

### Referências

- https://cbissn.ibict.br/index.php/solicitar-issn/publicacao-eletronica/online
- https://doity.com.br/blog/como-solicitar-o-issn/

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
python manage loaddata app/fixture/initial.json
```

- Execute o servidor e acesse o sistema;

## Uso
- A interface de administração do sistema está em `/admin`.

- A interface de *admin* do Django está em `/djangoadmin` e está disponível apenas no ambiente de desenvolvimento. Na *fixture* inicial o usuário padrão do `/djangoadmin` é `admin` com a senha `1234`.

- O acesso ao `/admin` se dá apenas para usuários com permissão de editor ou administrador.

- Não há página de cadastro pública, apenas os administradores/editores têm acesso ao sistema. Novos usuários devem ser cadastrados por algum administrador.
