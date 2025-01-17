{
    "name": "Library",
    "version": "17.0.0.0.1",
    "summary": "Book manager in a library",
    "category": "Library",
    "author": "Santiago the GOAT",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "data/library_data.xml",
        "views/library_menu_views.xml",
        "views/library_book_views.xml",
        "views/library_author_views.xml",
        "views/library_libraries_views.xml",
        "views/course_views.xml",
    ],
    "installable": True,
    "application": True,
}
