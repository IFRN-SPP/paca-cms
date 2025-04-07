from django.urls import reverse
from simple_menu import Menu, MenuItem

Menu.add_item(
    "dashboard",
    MenuItem(
        "Início",
        reverse("dashboard:index"),
        icon="bi bi-house-fill",
        exact_url=reverse("dashboard:index"),
    ),
)

submenu_items = [
    MenuItem(
        "Informações", reverse("dashboard:publication_detail"), icon="bi bi-circle"
    ),
    MenuItem(
        "Redes Sociais",
        reverse("dashboard:socialmedia_list"),
        icon="bi bi-circle",
        check=lambda r: r.user.has_perm("app.view_socialmedia"),
    ),
]
Menu.add_item(
    "dashboard",
    MenuItem(
        "Publicação",
        "#",
        icon="bi bi-journals",
        children=submenu_items,
        check=lambda r: r.user.has_perm("app.view_publication"),
    ),
)

Menu.add_item(
    "dashboard",
    MenuItem(
        "Edições",
        reverse("dashboard:issue_list"),
        icon="bi bi-files",
        check=lambda r: r.user.has_perm("app.view_issue"),
    ),
)

Menu.add_item(
    "dashboard",
    MenuItem(
        "Páginas",
        reverse("dashboard:page_list"),
        icon="bi bi-hand-index-thumb",
        check=lambda r: r.user.has_perm("app.view_page"),
    ),
)

Menu.add_item(
    "dashboard",
    MenuItem(
        "Documentos",
        reverse("dashboard:document_list"),
        icon="bi bi-file-earmark-arrow-up-fill",
        check=lambda r: r.user.has_perm("app.view_document"),
    ),
)

Menu.add_item(
    "dashboard",
    MenuItem(
        "Usuários",
        reverse("dashboard:user_list"),
        icon="bi bi-person-lines-fill",
        check=lambda r: r.user.has_perm("users.view_user"),
    ),
)

Menu.add_item(
    "dashboard",
    MenuItem(
        "Grupos",
        reverse("dashboard:group_list"),
        icon="bi bi-people-fill",
        check=lambda r: r.user.has_perm("users.view_group"),
    ),
)
