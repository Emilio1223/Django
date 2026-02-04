from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
from app.wsgi import *
from Core.erp.models import *

#SELECT * from tabla
# query = Type.objects.all()
# print(query)

#obj =Type.objects.filter(name__icontains='ko')
#obj =Type.objects.filter(name__istartswith='p')
# obj =Type.objects.filter(name__iendswith='o')
#obj =Type.objects.filter(name__exact='ko')
# obj =Type.objects.filter(name__in=['Presidente', 'Hola puto']).count()
#obj =Type.objects.filter(name__icontains='hola').query
#obj =Type.objects.filter(name__icontains='o').exclude(id=5)
Emplooye.objects.filter(type_id=1)

for obj in Type.objects.filter(Emplooye):
    print(obj.name)


# for obj in Type.objects.filter(name__icontains='ko')[:2]:
#     print(obj.name)

#INSERT 
# t = Type(name='Hola puto').save()
# t.name = "kojioj"
# t.save()

#EDIT 
# try: 
#     t = Type.objects.get(id=1)
#     t.name  = 'KOJIJSUEHD'
#     t.save()
# except Exception as e:
#     print(e)

#delete
# t = Type.objects.get(id=1)
#t.delete()

