# -*- coding: utf-8 -*-

{
    'name': 'Master Pack',
    'version': '13.0.0.2',
    'description': ''' MasterPack
    Compras:
        - Se añade el campo Cajas/Pieza en la interfaz de presupuesto y orden de compra.
        - Se añade el campo Cajas en la interfaz de presupuesto y orden de compra. El cual se calcula dividiendo
        - Cantidad entre Cajas/Pieza.
        - Se añade el Total de Cajas al final.
        - Los campos nuevos se deben reflejar en el PDF de Presupuesto y Orden de compra
    Ventas : 
        • Se añade el campo Cajas/Pieza en la interfaz de presupuesto y pedido de venta.
        • Se añade el campo Cajas en la interfaz de presupuesto y pedido de venta. El cual se calcula dividiendo Cantidad entre Cajas/Pieza.
        • Se añade el Total de Cajas al final.
        • Los campos nuevos se deben reflejar en el PDF de Presupuesto y pedido de venta.
    Transferencias:
        • Se añade el campo Cajas/Pieza en la interfaz de transferencias.
        • Se añade el campo Cajas en la interfaz de trasferencias. El cual se calcula dividiendo Cantidad entre Cajas/Pieza.
        • Se añade el Total de Cajas al final.
        • Los campos nuevos se deben reflejar en el PDF de Vale entrega.
    ''',
    'author': 'ITATIX SA DE CV',
    'website': 'www.itatix.net',
    'depends': [
        'product', 'sale', 'purchase', 'stock'
    ],
    'data': [
        'views/product_template_view.xml',
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
        'views/stock_picking_view.xml',
    ],
    'application': False,
    'installable': True,
    'license': 'OPL-1',
}
