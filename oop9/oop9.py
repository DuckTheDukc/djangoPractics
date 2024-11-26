from typing import Any


# class Handler:
    
#     def __init__(self,methods=("GET",)):
#         self.methods=methods
        
#     def __call__(self,func, *args: Any, **kwargs: Any):
#         type_methods={
#             "GET":self.get,
#             "POST":self.post,
#         }
#         def wrapper(request,*args,**kwargs):
#             if request["methods"] not in self.methods:
#                 raise f'данная страница не принимает тип запросов {request['methods']}'
#             return type_methods[request["methods"]](func,request,*args,**kwargs)
        
#     def get(self,func,request,*args,**kwargs):
#         return func(request,*args,**kwargs)
#     def post(self,func,request,*args,**kwargs):
#         return func(request,*args,**kwargs)
    
# @Handler(methods=("GET",))
# def get_page(request):
#     return "выаывафвфы"

# print(
#     get_page(
#         {
#             "methods":"POST",
#         }
#     )
# )

class Power:
    