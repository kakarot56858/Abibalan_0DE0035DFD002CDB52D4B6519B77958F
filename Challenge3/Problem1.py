products=["Pen","Pencil","Eraser","Scale","Pencil","pen"]
def Linear_Search_product(targetProduct):
  indices=[]
  for ind,items in enumerate(products):
       if(targetProduct==items):
             indices.append(ind)
  return indices

target="pen"
print(Linear_Search_product(target))
