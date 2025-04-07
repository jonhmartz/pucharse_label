{
    "name": "Etiqueta de Compras 2x1",
    "version": "1.0",
    "summary": "Impresión de etiquetas 2x1 desde órdenes de compra",
    "description": "Imprime etiquetas por unidad comprada desde órdenes de compra.",
    "category": "Purchases",
    "author": "TuNombre",
    "license": "LGPL-3",
    "depends": ["purchase", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/pucharse_label_wizard_view.xml",
        "views/pucharse_order_view.xml",
        "reports/report.xml",
        "reports/report_purchase_label_template.xml"
    ],
    "installable": True,
    "application": False
}
