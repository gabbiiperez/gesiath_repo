{
    "name": "Videoclub Santiago",
    "version": "17.0.0.0.1",
    "summary": "Gestion de peliculas para un videoclub",
    "category": "Movies",
    "author": "Santiago Perez",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "data/movie_data.xml",
        "views/menu_views.xml",
        "views/movie_views.xml",
    ],
    "installable": True,
    "application": True,
}
