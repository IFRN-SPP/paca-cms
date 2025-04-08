from django.urls import reverse
from simple_menu import Menu, MenuItem

Menu.add_item(
    "cms",
    MenuItem(
        "Início",
        reverse("cms:index"),
        icon="bi bi-house-fill",
        exact_url=reverse("cms:index"),
    ),
)

submenu_items = [
    MenuItem("Informações", reverse("cms:publication_detail"), icon="bi bi-circle"),
    MenuItem(
        "Redes Sociais",
        reverse("cms:socialmedia_list"),
        icon="bi bi-circle",
        check=lambda r: r.user.has_perm("cms.view_socialmedia"),
    ),
]
Menu.add_item(
    "cms",
    MenuItem(
        "Publicação",
        "#",
        icon="bi bi-journals",
        children=submenu_items,
        check=lambda r: r.user.has_perm("cms.view_publication"),
    ),
)

Menu.add_item(
    "cms",
    MenuItem(
        "Edições",
        reverse("cms:issue_list"),
        icon="bi bi-files",
        check=lambda r: r.user.has_perm("cms.view_issue"),
    ),
)

Menu.add_item(
    "cms",
    MenuItem(
        "Páginas",
        reverse("cms:page_list"),
        icon="bi bi-hand-index-thumb",
        check=lambda r: r.user.has_perm("cms.view_page"),
    ),
)

Menu.add_item(
    "cms",
    MenuItem(
        "Documentos",
        reverse("cms:document_list"),
        icon="bi bi-file-earmark-arrow-up-fill",
        check=lambda r: r.user.has_perm("cms.view_document"),
    ),
)

Menu.add_item(
    "cms",
    MenuItem(
        "Usuários",
        reverse("users:user_list"),
        icon="bi bi-person-lines-fill",
        check=lambda r: r.user.has_perm("users.view_user"),
    ),
)

Menu.add_item(
    "cms",
    MenuItem(
        "Grupos",
        reverse("users:group_list"),
        icon="bi bi-people-fill",
        check=lambda r: r.user.has_perm("auth.view_group"),
    ),
)
