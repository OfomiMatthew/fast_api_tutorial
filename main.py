from fastapi import FastAPI 
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


# @app.get('/blog')
# def index(limit=10,published:bool=True,sort=Optional[str] = None):
#   if(published):
#      return {"data":f"blog list of {limit}"
#   }
#   else:
#     return "All blogs"
    
 
  
  
@app.get('/blog/unpublished')
def unpublished():
  return {'data':'all unpublished'}  
  
@app.get('/blog/{id}')
def showBlog(id:int):
  return {"data":f'I have an id of {id}'}



@app.get('/blog/{id}/comments')
def comments(id,limit):
  return limit
  return {"data":f'comments of id: {id}'}


class Blog(BaseModel):
  title:str
  body:str
  description:str
  published: Optional[bool]
  
  


@app.post('/blog')
def createBlog(request:Blog):
  return {"data":f"blog created with title {request.title}, body:{request.body}, description:{request.description}"}
  
@app.get('/api/about')
def about():
  return "About me"



