# -*- encoding: utf-8 -*-
'''
Notas:
La función "walk" es útil para recorrer todos los ficheros y directorios que se encuentran incluidos en un directorio concreto.
'''
''' importamos modulo y librerias '''
from PyPDF2 import PdfFileReader, PdfFileWriter
import os 

def printMeta():
    '''para el diretorio, nombre y archivos en la carpeta docs'''
    for dirpath, dirnames, files in os.walk("docs"):
        '''recorremos los posibles fichreos'''
        for name in files:
            ext = name.lower().rsplit('.', 1)[-1]
            if ext in ['pdf']:
                '''pintamos el titulo de metadata for file y el directorio y nombre del documento'''
                print "[+] Metadata for file: %s " %(dirpath+os.path.sep+name)
                '''abrimos el fichero'''
                pdfFile = PdfFileReader(file(dirpath+os.path.sep+name, 'rb'))
                ''' obtenemos el numero de paginas de cada documento '''
                paginas = pdfFile.getNumPages()
                xmp = pdfFile.getXmpMetadata()
                if xmp is not None:
                    "\n*** XMP data -\n"
                    print "-dc_contributor: ", xmp.dc_contributor
                    print "-dc_coverage: ", xmp.dc_coverage
                    print "-dc_creator: ", xmp.dc_creator
                    print "-dc_date: ", xmp.dc_date
                    print "-dc_description: ", xmp.dc_description
                    print "-dc_format: ", xmp.dc_format
                    print "-dc_identifier: ", xmp.dc_identifier
                    print "-dc_language: ", xmp.dc_language
                    print "-dc_publisher: ", xmp.dc_publisher
                    print "-dc_relation: ", xmp.dc_relation
                    print "-dc_rights: ", xmp.dc_rights
                    print "-dc_source: ", xmp.dc_source
                    print "-dc_subject: ", xmp.dc_subject #tags/keywords
                    print "-dc_title: ", xmp.dc_title
                    print "-dc_type: ", xmp.dc_type
                    print "-pdf_keywords: ", xmp.pdf_keywords
                    print "-pdf_pdfversion: ", xmp.pdf_pdfversion
                    print "-pdf_producer: ", xmp.pdf_producer
                    print "-xmp_createDate: ", xmp.xmp_createDate
                    print "-xmp_creatorTool: ", xmp.xmp_creatorTool
                    print "-xmp_metadataDate: ", xmp.xmp_metadataDate
                    print "-xmpmm_documentId: ", xmp.xmpmm_documentId
                    print "-xmpmm_instanceId: ", xmp.xmpmm_instanceId
                    print "-xmp_modifyDate: ", xmp.xmp_modifyDate

                #Imprimimos tambien el numero de paginas del documento    
                print '[+] Paginas ' + str(paginas)
                print '*' * 50
                '''creamos un diccionario con la info recolectada'''
                docInfo = pdfFile.getDocumentInfo()
                for metaItem in docInfo:
                    if metaItem != '/AAPL:Keywords':
                        print '[+] ' + metaItem + ':' + docInfo[metaItem]
                print "\n"
'''invocamos la funcion '''
printMeta()