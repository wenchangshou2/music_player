# -*- coding: UTF-8 -*-
from termcolor import colored

class GenericError(Exception):
    message = "error class"
    def __init__(self,message=None,**kwargs):
        self.kwargs=kwargs

        if not message:
            message=self.message%kwargs
        super(GenericError,self).__init__(colored(message,'red'))

class ApiError(GenericError):
    pass