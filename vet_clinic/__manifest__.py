{
    "name": "Veterinary clinic",
    "version": "17.0.0.0.1",
    "summary": "Manage information for a veterinary clinic",
    "category": "Health",
    "author": "Santiago Perez",
    "depends": ["contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_view.xml",
        "views/vet_clinic_appointment_view.xml",
        "views/vet_clinic_pet_view.xml",
        "views/menu_views.xml",
    ],
    "installable": True,
    "application": True,
}
