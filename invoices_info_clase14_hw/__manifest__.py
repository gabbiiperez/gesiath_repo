{
    "name": "Invoice info Class 14 hw",
    "version": "17.0.0.0.1",
    "summary": "Homework class 14",
    "category": "Uncategorized",
    "author": "Santiago Perez",
    "depends": ["account_accountant"],
    "data": [
        "reports/invoice_template_report.xml",
        "views/invoice_template_views.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'invoices_info_clase14_hw/static/src/css/custom_styles.css',
        ],
    },

    "installable": True,
    "application": False,
}
