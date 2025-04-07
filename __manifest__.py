{
    "name": "Etiqueta de Compras 2x1",
    "version": "1.0",
    "summary": "Impresión de etiquetas 2x1 desde órdenes de compra",
    "description": "Imprime etiquetas por unidad comprada desde órdenes de compra.",
    "category": "Purchases",
    "author": "TuNombre",
    "depends": ["purchase", "stock"],
    "data": [
    "security/ir.model.access.csv",
    "views/pucharse_label_wizard_view.xml",
    "views/pucharse_order_view.xml",
],
    "installable": True,
    "application": False
}
