import scrapy

class Producto(scrapy.Item):
    nombre = scrapy.Field()
    precio = scrapy.Field()
    descripcion = scrapy.Field()