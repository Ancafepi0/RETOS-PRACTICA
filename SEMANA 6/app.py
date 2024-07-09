from flask import Flask, jsonify,request
#Jsonify es para convertir el cosas en lenguaje jason
#request proporciona los datos que me llegan de peticiones http
#ESTE APP ES LA APLICACION
app = Flask (__name__)
#FROM QUE IMPORTA LA LISTA DE PRODUCTOS DEL ARCHIVO PRODUCTS
from products import products
#ESTA ASIGNACION CREA LAS RUTAS Y SUS RESPECTIVAS FUNCIONALIDADES EN LA PAGINA
@app.route('/ping')
#DENTRO DE LA  RUTA SE PUEDEN AGREGAR METODOS UTLIZANDO UNA , Y DICIENDO METHODS
#DESPUES DE CADA RUTA VA EL METODO QUE EJECUTA LA ACCION QUE SE DESEE
def ping():
    return jsonify({"message": "pong"})
@app.route('/products')
def getProducts():
    return jsonify({"products": products,"message": "LISTA DE PRODUCTOS"})
@app.route('/products/<string:product_name>')
#TAMBIEN SE PUEDEN ALMACENAR VALORES EN VARIABLES UTILIZANDO LOS <> Y DESIGANDO QUE SERA LA VARIABLE
def getProduct (product_name):
    productsFound=[]
    for producto in products:
        if producto["nombre"] == product_name:
            productsFound= producto
    if (productsFound):
        return jsonify({"product": productsFound})
    return jsonify({"message": "producto no encontrado"})
#ESTE IF CREA LA CONEXION CON LA APLICACION ATRAVES DE UN PUERTO EN ESTE CASO 4000
#RUTA PARA CREAR DATOS
@app.route ('/products', methods=['POST'])
def addProduct ():
    new_product = {
        "name": request.json['nombre'],
        "precio":request.json['precio'],
        "quantity":request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Producto agreago satisfactoriamente", "products": products})
@app.route ('/products/<string:product_name>',methods=['PUT'])
def editProduct (product_name):
    product_fond=[product for product in products if product['nombre']== product_name]
    if (len(product_fond)>0):
        product_fond[0]['nombre'] = request.json['nombre']
        product_fond[0]['precio'] = request.json['precio']
        product_fond[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Producto actualizado",
            "product" : product_fond[0]
        })
    return jsonify ({'message': 'Producto no actualizado'})
@app.route ('/products/<string:product_name>',methods=['DELETE'])
def deleteProduct(product_name):
    product_fond=[product for product in products if product['nombre']== product_name]
    if len (product_fond) > 0:
        products.remove(product_fond[0])
        return jsonify({
            "message": "Producto Borrado",
            "products": products
        })
    return jsonify ({'message':'Producto no encontrado'})
if __name__ == '__main__':
    app.run(debug=True,port=4000)