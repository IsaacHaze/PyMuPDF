# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_fitz', [dirname(__file__)])
        except ImportError:
            import _fitz
            return _fitz
        if fp is not None:
            try:
                _mod = imp.load_module('_fitz', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _fitz = swig_import_helper()
    del swig_import_helper
else:
    import _fitz
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



VersionFitz = "1.7a"
VersionBind = "1.7.0"

class Document(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Document, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Document, name)
    __repr__ = _swig_repr

    def __init__(self, filename, stream=None, streamlen=0):

        '''
        filename or filetype: string specifying a file name or a MIME type
        stream:               string containing document data
        streamlen:            integer containing length of stream
        '''
        if type(filename) == str:
            pass
        elif type(filename) == unicode:
            filename = filename.encode('utf8')
        else:
            raise TypeError("filename must be a string")
        self.name = filename
        self.isClosed = 0



        this = _fitz.new_Document(filename, stream, streamlen)
        try:
            self.this.append(this)
        except:
            self.this = this

                    #================================================================
                    # Function: Table of Contents
                    #================================================================
        def ToC():

            def recurse(olItem, liste, lvl):
                while olItem:
                    if olItem.title:
                        title = olItem.title.decode("utf-8")
                    else:
                        title = u" "
                    if olItem.dest.kind == 1:
                        page = olItem.dest.page + 1
                    else:
                        page = 0
                    liste.append([lvl, title, page])
                    if olItem.down:
                        liste = recurse(olItem.down, liste, lvl+1)
                    olItem = olItem.next
                return liste

            olItem = self.outline
            if not olItem: return []
            lvl = 1
            liste = []
            return recurse(olItem, liste, lvl)

        if this:
            self._outline = self._loadOutline()
            self.metadata = dict([(k,self._getMetadata(v)) for k,v in {'format':'format','title':'info:Title',
                                                                       'author':'info:Author','subject':'info:Subject',
                                                                       'keywords':'info:Keywords','creator':'info:Creator',
                                                                       'producer':'info:Producer','creationDate':'info:CreationDate',
                                                                       'modDate':'info:ModDate'}.items()])
            self.metadata['encryption'] = None if self._getMetadata('encryption')=='None' else self._getMetadata('encryption')
            self.ToC = ToC
            self.thisown = False




    def close(self):

        if self.isClosed == 1:
            raise ValueError("operation on closed document")
        if hasattr(self, '_outline') and self._outline:
            self._dropOutline(self._outline)
            self._outline = None
        self.metadata = None
        self.ToC = None
        self.isClosed = 1


        return _fitz.Document_close(self)


    def loadPage(self, number):

        if self.isClosed == 1:
            raise ValueError("operation on closed document")


        val = _fitz.Document_loadPage(self, number)

        if val:
            val.thisown = True
            val.number = number
            val.parent = self


        return val


    def _loadOutline(self):

        if self.isClosed == 1:
            raise ValueError("operation on closed document")


        return _fitz.Document__loadOutline(self)


    def _dropOutline(self, ol):

        if self.isClosed == 1:
            raise ValueError("operation on closed document")


        return _fitz.Document__dropOutline(self, ol)


    def _getPageCount(self):

        if self.isClosed == 1:
            raise ValueError("operation on closed document")


        return _fitz.Document__getPageCount(self)


    def _getMetadata(self, key):

        if self.isClosed == 1:
            raise ValueError("operation on closed document")


        return _fitz.Document__getMetadata(self, key)


    def _needsPass(self):

        if self.isClosed == 1:
            raise ValueError("operation on closed document")


        return _fitz.Document__needsPass(self)


    def authenticate(self, arg2):

        if self.isClosed == 1:
            raise ValueError("operation on closed document")


        return _fitz.Document_authenticate(self, arg2)


    def save(self, filename, garbage=0, clean=0, deflate=0, incremental=0, ascii=0, expand=0, linear=0):

        '''
        filename:     path / name of file to save to, must be unequal the document's filename
        garbage:      level of garbage collection, 0 = none, 3 = all
        clean:        clean content streams, 0 = False, 1 = True
        deflate:      deflate uncompressed streams, 0 = False, 1 = True
        incremental:  write just the changed objects, 0 = False, 1 = True
        ascii:        where possible make the output ascii, 0 = False, 1 = True
        expand:       one bytpe bitfield to decompress content, 0 = none, 1 = images, 2 = fonts, 255 = all
        linear:       write linearised, 0 = False, 1 = True
        '''
        if self.isClosed == 1:
            raise ValueError("operation on closed document")
        if type(filename) == str:
            pass
        elif type(filename) == unicode:
            filename = filename.encode('utf8')
        else:
            raise TypeError("filename must be a string")
        if filename == self.name:
            raise ValueError("cannot save to input file")


        return _fitz.Document_save(self, filename, garbage, clean, deflate, incremental, ascii, expand, linear)


    pageCount = property(lambda self: self._getPageCount())
    outline = property(lambda self: self._outline)
    needsPass = property(lambda self: self._needsPass())

    __swig_destroy__ = _fitz.delete_Document
    __del__ = lambda self: None
Document_swigregister = _fitz.Document_swigregister
Document_swigregister(Document)

class Page(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Page, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Page, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _fitz.delete_Page
    __del__ = lambda self: None

    def bound(self):

        if self.parent.isClosed == 1:
            raise ValueError("page operation on closed document")


        val = _fitz.Page_bound(self)

        if val:
            val.thisown = True


        return val


    def run(self, dw, m):

        if self.parent.isClosed == 1:
            raise ValueError("page operation on closed document")


        return _fitz.Page_run(self, dw, m)


    def loadLinks(self):

        if self.parent.isClosed == 1:
            raise ValueError("page operation on closed document")


        val = _fitz.Page_loadLinks(self)

        if val:
            val.thisown = True


        return val

Page_swigregister = _fitz.Page_swigregister
Page_swigregister(Page)


def _fz_transform_rect(rect, transform):
    return _fitz._fz_transform_rect(rect, transform)
_fz_transform_rect = _fitz._fz_transform_rect
class Rect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Rect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Rect, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x0"] = _fitz.Rect_x0_set
    __swig_getmethods__["x0"] = _fitz.Rect_x0_get
    if _newclass:
        x0 = _swig_property(_fitz.Rect_x0_get, _fitz.Rect_x0_set)
    __swig_setmethods__["y0"] = _fitz.Rect_y0_set
    __swig_getmethods__["y0"] = _fitz.Rect_y0_get
    if _newclass:
        y0 = _swig_property(_fitz.Rect_y0_get, _fitz.Rect_y0_set)
    __swig_setmethods__["x1"] = _fitz.Rect_x1_set
    __swig_getmethods__["x1"] = _fitz.Rect_x1_get
    if _newclass:
        x1 = _swig_property(_fitz.Rect_x1_get, _fitz.Rect_x1_set)
    __swig_setmethods__["y1"] = _fitz.Rect_y1_set
    __swig_getmethods__["y1"] = _fitz.Rect_y1_get
    if _newclass:
        y1 = _swig_property(_fitz.Rect_y1_get, _fitz.Rect_y1_set)

    def __init__(self, *args):
        this = _fitz.new_Rect(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def round(self):
        val = _fitz.Rect_round(self)

        val.thisown = True


        return val


    def transform(self, m):
        _fitz._fz_transform_rect(self, m)
        return self
    width = property(lambda self: self.x1-self.x0)
    height = property(lambda self: self.y1-self.y0)

    __swig_destroy__ = _fitz.delete_Rect
    __del__ = lambda self: None
Rect_swigregister = _fitz.Rect_swigregister
Rect_swigregister(Rect)

class IRect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IRect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IRect, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x0"] = _fitz.IRect_x0_set
    __swig_getmethods__["x0"] = _fitz.IRect_x0_get
    if _newclass:
        x0 = _swig_property(_fitz.IRect_x0_get, _fitz.IRect_x0_set)
    __swig_setmethods__["y0"] = _fitz.IRect_y0_set
    __swig_getmethods__["y0"] = _fitz.IRect_y0_get
    if _newclass:
        y0 = _swig_property(_fitz.IRect_y0_get, _fitz.IRect_y0_set)
    __swig_setmethods__["x1"] = _fitz.IRect_x1_set
    __swig_getmethods__["x1"] = _fitz.IRect_x1_get
    if _newclass:
        x1 = _swig_property(_fitz.IRect_x1_get, _fitz.IRect_x1_set)
    __swig_setmethods__["y1"] = _fitz.IRect_y1_set
    __swig_getmethods__["y1"] = _fitz.IRect_y1_get
    if _newclass:
        y1 = _swig_property(_fitz.IRect_y1_get, _fitz.IRect_y1_set)

    def __init__(self, *args):
        this = _fitz.new_IRect(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    width = property(lambda self: self.x1-self.x0)
    height = property(lambda self: self.y1-self.y0)

    __swig_destroy__ = _fitz.delete_IRect
    __del__ = lambda self: None
IRect_swigregister = _fitz.IRect_swigregister
IRect_swigregister(IRect)

class Pixmap(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Pixmap, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Pixmap, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _fitz.Pixmap_x_set
    __swig_getmethods__["x"] = _fitz.Pixmap_x_get
    if _newclass:
        x = _swig_property(_fitz.Pixmap_x_get, _fitz.Pixmap_x_set)
    __swig_setmethods__["y"] = _fitz.Pixmap_y_set
    __swig_getmethods__["y"] = _fitz.Pixmap_y_get
    if _newclass:
        y = _swig_property(_fitz.Pixmap_y_get, _fitz.Pixmap_y_set)
    __swig_setmethods__["w"] = _fitz.Pixmap_w_set
    __swig_getmethods__["w"] = _fitz.Pixmap_w_get
    if _newclass:
        w = _swig_property(_fitz.Pixmap_w_get, _fitz.Pixmap_w_set)
    __swig_setmethods__["h"] = _fitz.Pixmap_h_set
    __swig_getmethods__["h"] = _fitz.Pixmap_h_get
    if _newclass:
        h = _swig_property(_fitz.Pixmap_h_get, _fitz.Pixmap_h_set)
    __swig_setmethods__["n"] = _fitz.Pixmap_n_set
    __swig_getmethods__["n"] = _fitz.Pixmap_n_get
    if _newclass:
        n = _swig_property(_fitz.Pixmap_n_get, _fitz.Pixmap_n_set)
    __swig_setmethods__["interpolate"] = _fitz.Pixmap_interpolate_set
    __swig_getmethods__["interpolate"] = _fitz.Pixmap_interpolate_get
    if _newclass:
        interpolate = _swig_property(_fitz.Pixmap_interpolate_get, _fitz.Pixmap_interpolate_set)
    __swig_setmethods__["xres"] = _fitz.Pixmap_xres_set
    __swig_getmethods__["xres"] = _fitz.Pixmap_xres_get
    if _newclass:
        xres = _swig_property(_fitz.Pixmap_xres_get, _fitz.Pixmap_xres_set)
    __swig_setmethods__["yres"] = _fitz.Pixmap_yres_set
    __swig_getmethods__["yres"] = _fitz.Pixmap_yres_get
    if _newclass:
        yres = _swig_property(_fitz.Pixmap_yres_get, _fitz.Pixmap_yres_set)

    def __init__(self, cs, bbox):
        this = _fitz.new_Pixmap(cs, bbox)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _fitz.delete_Pixmap
    __del__ = lambda self: None

    def clearWith(self, value):
        return _fitz.Pixmap_clearWith(self, value)

    def writePNG(self, filename, savealpha=0):

        if type(filename) == str:
            pass
        elif type(filename) == unicode:
            filename = filename.encode('utf8')
        else:
            raise TypeError("filename must be a string")


        return _fitz.Pixmap_writePNG(self, filename, savealpha)


    def invertIRect(self, irect):
        return _fitz.Pixmap_invertIRect(self, irect)

    def _getSamples(self):
        return _fitz.Pixmap__getSamples(self)

    samples = property(lambda self: self._getSamples())

Pixmap_swigregister = _fitz.Pixmap_swigregister
Pixmap_swigregister(Pixmap)


_fitz.CS_RGB_swigconstant(_fitz)
CS_RGB = _fitz.CS_RGB

_fitz.CS_GRAY_swigconstant(_fitz)
CS_GRAY = _fitz.CS_GRAY

_fitz.CS_CMYK_swigconstant(_fitz)
CS_CMYK = _fitz.CS_CMYK
class Colorspace(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Colorspace, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Colorspace, name)
    __repr__ = _swig_repr

    def __init__(self, type):
        this = _fitz.new_Colorspace(type)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _fitz.delete_Colorspace
    __del__ = lambda self: None
Colorspace_swigregister = _fitz.Colorspace_swigregister
Colorspace_swigregister(Colorspace)

class Device(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Device, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Device, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _fitz.new_Device(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _fitz.delete_Device
    __del__ = lambda self: None
Device_swigregister = _fitz.Device_swigregister
Device_swigregister(Device)


def _fz_pre_scale(m, sx, sy):
    return _fitz._fz_pre_scale(m, sx, sy)
_fz_pre_scale = _fitz._fz_pre_scale

def _fz_pre_shear(m, sx, sy):
    return _fitz._fz_pre_shear(m, sx, sy)
_fz_pre_shear = _fitz._fz_pre_shear

def _fz_pre_rotate(m, degree):
    return _fitz._fz_pre_rotate(m, degree)
_fz_pre_rotate = _fitz._fz_pre_rotate
class Matrix(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Matrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Matrix, name)
    __repr__ = _swig_repr
    __swig_setmethods__["a"] = _fitz.Matrix_a_set
    __swig_getmethods__["a"] = _fitz.Matrix_a_get
    if _newclass:
        a = _swig_property(_fitz.Matrix_a_get, _fitz.Matrix_a_set)
    __swig_setmethods__["b"] = _fitz.Matrix_b_set
    __swig_getmethods__["b"] = _fitz.Matrix_b_get
    if _newclass:
        b = _swig_property(_fitz.Matrix_b_get, _fitz.Matrix_b_set)
    __swig_setmethods__["c"] = _fitz.Matrix_c_set
    __swig_getmethods__["c"] = _fitz.Matrix_c_get
    if _newclass:
        c = _swig_property(_fitz.Matrix_c_get, _fitz.Matrix_c_set)
    __swig_setmethods__["d"] = _fitz.Matrix_d_set
    __swig_getmethods__["d"] = _fitz.Matrix_d_get
    if _newclass:
        d = _swig_property(_fitz.Matrix_d_get, _fitz.Matrix_d_set)
    __swig_setmethods__["e"] = _fitz.Matrix_e_set
    __swig_getmethods__["e"] = _fitz.Matrix_e_get
    if _newclass:
        e = _swig_property(_fitz.Matrix_e_get, _fitz.Matrix_e_set)
    __swig_setmethods__["f"] = _fitz.Matrix_f_set
    __swig_getmethods__["f"] = _fitz.Matrix_f_get
    if _newclass:
        f = _swig_property(_fitz.Matrix_f_get, _fitz.Matrix_f_set)

    def __init__(self, *args):
        this = _fitz.new_Matrix(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def preScale(self, sx, sy):
        _fitz._fz_pre_scale(self, sx, sy)
        return self
    def preShear(self, sx, sy):
        _fitz._fz_pre_shear(self, sx, sy)
        return self
    def preRotate(self, degree):
        _fitz._fz_pre_rotate(self, degree)
        return self

    __swig_destroy__ = _fitz.delete_Matrix
    __del__ = lambda self: None
Matrix_swigregister = _fitz.Matrix_swigregister
Matrix_swigregister(Matrix)

class Outline(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Outline, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Outline, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["title"] = _fitz.Outline_title_get
    if _newclass:
        title = _swig_property(_fitz.Outline_title_get)
    __swig_getmethods__["dest"] = _fitz.Outline_dest_get
    if _newclass:
        dest = _swig_property(_fitz.Outline_dest_get)
    __swig_getmethods__["next"] = _fitz.Outline_next_get
    if _newclass:
        next = _swig_property(_fitz.Outline_next_get)
    __swig_getmethods__["down"] = _fitz.Outline_down_get
    if _newclass:
        down = _swig_property(_fitz.Outline_down_get)
    __swig_getmethods__["is_open"] = _fitz.Outline_is_open_get
    if _newclass:
        is_open = _swig_property(_fitz.Outline_is_open_get)

    def saveXML(self, filename):

        if type(filename) == str:
            pass
        elif type(filename) == unicode:
            filename = filename.encode('utf8')
        else:
            raise TypeError("filename must be a string")


        return _fitz.Outline_saveXML(self, filename)


    def saveText(self, filename):

        if type(filename) == str:
            pass
        elif type(filename) == unicode:
            filename = filename.encode('utf8')
        else:
            raise TypeError("filename must be a string")


        return _fitz.Outline_saveText(self, filename)

    __swig_destroy__ = _fitz.delete_Outline
    __del__ = lambda self: None
Outline_swigregister = _fitz.Outline_swigregister
Outline_swigregister(Outline)
cvar = _fitz.cvar
Identity = cvar.Identity


_fitz.LINK_NONE_swigconstant(_fitz)
LINK_NONE = _fitz.LINK_NONE

_fitz.LINK_GOTO_swigconstant(_fitz)
LINK_GOTO = _fitz.LINK_GOTO

_fitz.LINK_URI_swigconstant(_fitz)
LINK_URI = _fitz.LINK_URI

_fitz.LINK_LAUNCH_swigconstant(_fitz)
LINK_LAUNCH = _fitz.LINK_LAUNCH

_fitz.LINK_NAMED_swigconstant(_fitz)
LINK_NAMED = _fitz.LINK_NAMED

_fitz.LINK_GOTOR_swigconstant(_fitz)
LINK_GOTOR = _fitz.LINK_GOTOR
class linkDest(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, linkDest, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, linkDest, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["kind"] = _fitz.linkDest_kind_get
    if _newclass:
        kind = _swig_property(_fitz.linkDest_kind_get)

    def _getPage(self):
        return _fitz.linkDest__getPage(self)

    def _getDest(self):
        return _fitz.linkDest__getDest(self)

    def _getFlags(self):
        return _fitz.linkDest__getFlags(self)

    def _getLt(self):
        return _fitz.linkDest__getLt(self)

    def _getRb(self):
        return _fitz.linkDest__getRb(self)

    def _getFileSpec(self):
        return _fitz.linkDest__getFileSpec(self)

    def _getNewWindow(self):
        return _fitz.linkDest__getNewWindow(self)

    def _getUri(self):
        return _fitz.linkDest__getUri(self)

    def _getIsMap(self):
        return _fitz.linkDest__getIsMap(self)

    def _getIsUri(self):
        return _fitz.linkDest__getIsUri(self)

    def _getNamed(self):
        return _fitz.linkDest__getNamed(self)
    __swig_destroy__ = _fitz.delete_linkDest
    __del__ = lambda self: None

    page = property(_getPage)
    dest = property(_getDest)
    flags = property(_getFlags)
    lt = property(_getLt)
    rb = property(_getRb)
    fileSpec = property(_getFileSpec)
    newWindow = property(_getNewWindow)
    uri = property(_getUri)
    isMap = property(_getIsMap)
    isUri = property(_getIsUri)
    named = property(_getNamed)

linkDest_swigregister = _fitz.linkDest_swigregister
linkDest_swigregister(linkDest)


def _fz_transform_point(point, transform):
    return _fitz._fz_transform_point(point, transform)
_fz_transform_point = _fitz._fz_transform_point
class Point(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Point, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _fitz.Point_x_set
    __swig_getmethods__["x"] = _fitz.Point_x_get
    if _newclass:
        x = _swig_property(_fitz.Point_x_get, _fitz.Point_x_set)
    __swig_setmethods__["y"] = _fitz.Point_y_set
    __swig_getmethods__["y"] = _fitz.Point_y_get
    if _newclass:
        y = _swig_property(_fitz.Point_y_get, _fitz.Point_y_set)

    def __init__(self, *args):
        this = _fitz.new_Point(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def transform(self, m):
        _fitz._fz_transform_point(self, m)
        return self

    __swig_destroy__ = _fitz.delete_Point
    __del__ = lambda self: None
Point_swigregister = _fitz.Point_swigregister
Point_swigregister(Point)


_fitz.LINK_FLAG_L_VALID_swigconstant(_fitz)
LINK_FLAG_L_VALID = _fitz.LINK_FLAG_L_VALID

_fitz.LINK_FLAG_T_VALID_swigconstant(_fitz)
LINK_FLAG_T_VALID = _fitz.LINK_FLAG_T_VALID

_fitz.LINK_FLAG_R_VALID_swigconstant(_fitz)
LINK_FLAG_R_VALID = _fitz.LINK_FLAG_R_VALID

_fitz.LINK_FLAG_B_VALID_swigconstant(_fitz)
LINK_FLAG_B_VALID = _fitz.LINK_FLAG_B_VALID

_fitz.LINK_FLAG_FIT_H_swigconstant(_fitz)
LINK_FLAG_FIT_H = _fitz.LINK_FLAG_FIT_H

_fitz.LINK_FLAG_FIT_V_swigconstant(_fitz)
LINK_FLAG_FIT_V = _fitz.LINK_FLAG_FIT_V

_fitz.LINK_FLAG_R_IS_ZOOM_swigconstant(_fitz)
LINK_FLAG_R_IS_ZOOM = _fitz.LINK_FLAG_R_IS_ZOOM
class Link(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Link, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Link, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["rect"] = _fitz.Link_rect_get
    if _newclass:
        rect = _swig_property(_fitz.Link_rect_get)
    __swig_getmethods__["dest"] = _fitz.Link_dest_get
    if _newclass:
        dest = _swig_property(_fitz.Link_dest_get)
    __swig_destroy__ = _fitz.delete_Link
    __del__ = lambda self: None

    def _getNext(self):
        val = _fitz.Link__getNext(self)

        if val:
            val.thisown = True


        return val


    next = property(_getNext)

Link_swigregister = _fitz.Link_swigregister
Link_swigregister(Link)

class DisplayList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DisplayList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DisplayList, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _fitz.new_DisplayList()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _fitz.delete_DisplayList
    __del__ = lambda self: None

    def run(self, dw, m, area):
        return _fitz.DisplayList_run(self, dw, m, area)
DisplayList_swigregister = _fitz.DisplayList_swigregister
DisplayList_swigregister(DisplayList)

class TextSheet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TextSheet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TextSheet, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _fitz.new_TextSheet()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _fitz.delete_TextSheet
    __del__ = lambda self: None
TextSheet_swigregister = _fitz.TextSheet_swigregister
TextSheet_swigregister(TextSheet)

class TextPage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TextPage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TextPage, name)
    __repr__ = _swig_repr
    __swig_setmethods__["len"] = _fitz.TextPage_len_set
    __swig_getmethods__["len"] = _fitz.TextPage_len_get
    if _newclass:
        len = _swig_property(_fitz.TextPage_len_get, _fitz.TextPage_len_set)

    def __init__(self):
        this = _fitz.new_TextPage()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _fitz.delete_TextPage
    __del__ = lambda self: None

    def search(self, needle, hit_max=16):
        return _fitz.TextPage_search(self, needle, hit_max)

    def extractText(self, basic=0):
        val = _fitz.TextPage_extractText(self, basic)

        if not val:
           return None
        if basic == 1: # no XML-based re-ordering required
            return val

        def TrueText(xml):
            '''
            Converts MuPDF TextPage.extractXML() output (parameter) into plain text.
            This is an alternative to the extractText() method with the following
            advantages:
            1) Encoding is unicode, making it easier to print in appropriate locales
            2) It is re-arranged according to normal reading sequence by sorting the
               page blocks according to their top-left (Y || X) coordinates
            '''
            spec_chars = {"&amp;":"&",
                      "&lt;":"<",
                      "&gt;":">",
                      "&quot;":'"',
                      "&apos;":"'",
                      "&tilde;":"~",
                      "&#x8;":" ",                  # backspace becomes space!
                      }
            fin_lines = xml.split("\n")             # split string into lines
            out_blocks = []                         # initialize my list of page blocks
            old_srt = "........"                    # initialize block sort field
            for i in range(len(fin_lines)):
                z = fin_lines[i]                    # z contains 1 line
                if z.startswith("<page "):          # should be first line
                    continue
                if z.startswith("<block "):         # a new page block
                    p0 = z.find("bbox=")            # extract top-left point from it
                    p0 = p0 + 6                     # start of x0 behind '"'
                    p1 = z.find(" ", p0)            # end of x0
                    x0 = int(float(z[p0:p1]) + 0.99999)  # calc pixel value
                    p0 = p1 + 1                     # start of y0
                    p1 = z.find(" ", p0)            # end of y0
                    y0 = int(float(z[p0:p1]) + 0.99999)  # calc pixel value
                    x0 = str(x0).rjust(4,'0')       # make it a 4-digit string
                    y0 = str(y0).rjust(4,'0')       # make it a 4-digit string
                    b_srt = y0 + x0                 # sort field of the block
        # check if we rather should extend the previous block.
        # can only be true if y is greater and x is equal
                    if b_srt >= old_srt and \
                        b_srt[4:] == old_srt[4:]:   # equal x coords: extends prev block
                        old_block = out_blocks[-1]  # get last block's entry
                        del out_blocks[-1]          # delete it from the list
                        b_srt = old_srt             # retain old sort field
                        b_lines = old_block[1]      # get the lines buffer for extension
                    else:
                        old_srt = b_srt             # really a new block
                        b_lines = []                # initialize list of block lines
                    continue
                if z.startswith("<line "):          # a new line
                    out_buff = ""                   # init char buffer
                    last_x = 0.0                    # init char's x coord
                    last_y = 0.0                    # init char's y coord
                    continue
                if z.startswith("<span "):          # a new span (sequence of char's)
                    continue
                if z.startswith("<char "):          # a new character
                    p0 = z.find(" x=")              # find its x coordinate
                    p0 = p0 + 4                     # step behind the "
                    p1 = z.find('"', p0)            # end of x value
                    neu_x = float(z[p0:p1])         # this is the x coordinate
                    p0 = z.find("y=",p1) + 3        # find y coord
                    p1 = z.find('"',p0)             # end of coord
                    neu_y = float(z[p0:p1])         # this is the y coordinate
                    p0 = z.find('c="', p1)          # find char value
                    p0 += 3                         # step behind the "
                    p1 = z.find('"', p0)            # end of char value
                    c = z[p0:p1]                    # this is the char value
                    if c in spec_chars:             # handle special characters
                        c = spec_chars[c]           # get rid of '&amp;' etc.
                    if c.startswith("&#x"):         # handle hex unicodes
                        c = unichr(int("0" + c[2:-1], base = 16))  # this is the unicode
                    if c.startswith("&#"):          # handle dec unicodes
                        c = unichr(int(c[2:-1]))
                    if neu_x != last_x or \
                        neu_y != last_y:            # char coords != last ones?
                        out_buff += unicode(c)      # normal append
                        last_x = neu_x              # save as last x coord
                        last_y = neu_y              # save as last y coord
                    else:
                        out_buff = out_buff[:-1] + unicode(c)  # no pesky spaces
                    continue
                if z.startswith("</span>"):         # end of span
                    out_buff += u" "
                    continue
                if z.startswith("</line>"):         # end of line
                    b_lines.append(out_buff)        # append line to block line buffer
                    continue
                if z.startswith("</block>"):        # end of block
                    out_blocks.append([b_srt, b_lines]) # append lines to block buffer
                    continue
                if z.startswith("</page>"):         # should be last line
                    continue
            out_blocks.sort()                       # sort blocks by top-left coord
            big_string = u""                        # initialize final output
            for b in out_blocks:                    # for each block ...
                for z in b[1]:                      # ... take each line ...
                    big_string += unicode(z) + u"\n"  # and append it to final output
                big_string += u"\n"                 # add a line break after the block
            return big_string                       # done

        val = TrueText(val)


        return val


    def extractXML(self):
        return _fitz.TextPage_extractXML(self)

    def extractHTML(self):
        return _fitz.TextPage_extractHTML(self)

    def extractJSON(self):
        return _fitz.TextPage_extractJSON(self)
TextPage_swigregister = _fitz.TextPage_swigregister
TextPage_swigregister(TextPage)

# This file is compatible with both classic and new-style classes.


