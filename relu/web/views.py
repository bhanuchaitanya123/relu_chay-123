from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
def home(response):
   if response.method == "POST":
      print()
   else:
    la=[]
    dd=pd.read_csv("results.csv")
    da_0=dd['DA_Number'].tolist()
    da_1=dd['Detail_URL'].tolist()
    da_2=dd['Description'].tolist()
    da_3=dd['Submitted_Date'].tolist()
    da_4=dd['Decision'].tolist()
    da_5=dd['Categories'].tolist()
    da_6=dd['Property_Address'].tolist()
    da_7=dd['Applicant'].tolist()
    da_8=dd['Progress'].tolist()
    da_9=dd['Fees'].tolist()
    da_10=dd['Documents'].tolist()
    da_11=dd['Contact_Council'].tolist()
    
    le=len(dd)
    for i in range(le):
      la.append([da_0[i],da_1[i], da_2[i], da_3[i], da_4[i], da_5[i], da_6[i], da_7[i], da_8[i], da_9[i], da_10[i], da_11[i]])
    dat={'la':la}
    #return render(response,"home.html",{'da_0':da_0,'da_1':da_1,'da_2':da_2,'da_3':da_3,'da_4':da_4,'da_5':da_5,'da_6':da_6,'da_7':da_7,'da_8':da_8,'da_9':da_9,'da_10':da_10,'da_11':da_11,'le':le})

    return render(response,"index.html",{'dat': dat,'la':la,'le':le-1})

