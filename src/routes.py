# coding:utf-8
import tornado
import tornado.ioloop
import tornado.web
import tornado.template
from src.controller import (search,demo,compare,upload,bindex,urltool,mix)
import os

def getRoutes(config):
    Routes = [

        # ---------------------------------------------
        # demo url
        # ---------------------------------------------
        (r"/", demo.HomeHandler),
        (r"/demo", demo.DemoHandler),
        (r"/search", demo.DemoSearchHandler),
        (r"/search_color", demo.DemoSearchColorHandler),
        (r"/upload_search", demo.DemoUploadSearchHandler),
        (r"/upload_search_color", demo.DemoUploadSearchColorHandler),

        # ---------------------------------------------
        # static url
        # ---------------------------------------------
        (r'/img/(.*)', tornado.web.StaticFileHandler, {'path': os.environ[config.STATIC_DIR]}),
        (r'/tests/(.*)', tornado.web.StaticFileHandler, {'path': os.environ[config.PROJECT_DIR]+"/tests/"}),

        # ---------------------------------------------
        # supply restful api just like elasticsearch
        # ---------------------------------------------
        (r'/_search/json/(.*)', search.JsonHandler),
        (r'/_pc(.*)',compare.pcHandler),
        (r'/_upload(.*)',upload.UploadHandler),
        (r'/_mix(.*)',mix.MixHandler),
        # (r'/_color(.*)',compare.pcHandler),
        (r'/_index(.*)',bindex.BuildIndexHandler),


        (r'/crossdomain.xml',urltool.urltoolHandler)
    ]

    return Routes