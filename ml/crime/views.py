from django.shortcuts import render
from django.shortcuts import render,redirect
from . forms import TForm
from . models import User
from django.contrib import messages
from django.contrib.auth.models import auth
from django.shortcuts import render
from django.db.models import Q
from datetime import date, timedelta
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
import datetime
import urllib, base64
import statsmodels.api as sm
import seaborn as sns
from fcmeans import FCM
from sklearn.cluster import KMeans
from io import BytesIO


# Create your views here.
def home(request):
    output = None
    scatter_plot = None
    
    if request.method == 'POST':
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        output, scatter_plot = getout(longitude, latitude)
        
        context = {
            'output': output,
            'scatter_plot': scatter_plot,
            'long': longitude,
            'lat': latitude
        }
        return render(request, 'html/home.html', context)
    
    return render(request, 'html/home.html', {'output': output, 'scatter_plot': scatter_plot})


def ulogin(request):
	if request.method=="POST":
		uid=request.POST.get('username','')
		password=request.POST.get('password','')
		print(uid,password)
		user=auth.authenticate(request,username=uid,password=password)
		print(user)
		if user is not None:
			print("user successful")
			auth.login(request,user)
			return redirect("/")
		else:
			print(" unsuccessful ")
			messages.info(request,'invalid credentials')
			return redirect("ulogin")
	else:	
		return render(request,'html/User_Login.html')


def uregister(request):
    if request.method == "POST":
    	g=TForm(request.POST)
    	if g.is_valid():
    		g.save()
    		print("user created")
    		uid=request.POST.get('username','')
    		password=request.POST.get('password1','')
    		u = User.objects.get(username=uid)
    		u.save()
    		print(uid,password)
    		user=auth.authenticate(request,username=uid,password=password)
    		print(user)
    		if user is not None:
    			print("user successful")
    			auth.login(request,user)
    			return redirect("/")
    		else:
    			print(" unsuccessful ")
    			messages.info(request,'invalid credentials')
    		return redirect('home')
    	else:
    		print("user not created")
    		messages.info(request,'please give valid credentials')
    		print(g.errors)
    g=TForm()
    return render(request,'html/User_registration.html',{'form':g})

def ulogout(request):
	auth.logout(request)
	return redirect('home')


def aboutus(request):
	return render(request,'html/Aboutus.html')

def contactus(request):
	return render(request,'html/contactus.html')



def getout(long1, lang1):

    data = pd.read_csv("./crime.csv")

    data.Magnitude = data.Magnitude.replace(to_replace="ARSON", value="9")
    data['Magnitude'] = data['Magnitude'].astype(int)
    X = data[['Latitude', 'Longitude', 'Magnitude']]
    X = np.array(X)

    my_model = FCM(n_clusters=3, random_state=42)
    my_model.fit(X)
    fcm_clusters = my_model.predict(X)

    kmeans = KMeans(3, random_state=42, max_iter=20, verbose=10)
    kmeans_clusters = kmeans.fit_predict(X)

    cnt_match = np.sum(fcm_clusters == kmeans_clusters)
    res = cnt_match / len(kmeans_clusters)

    latit = float(lang1)
    longit = float(long1)
    rate = 0.0
    c = 0
    for i in range(len(X)):
        if (X[i, 0] == latit) and (X[i, 1] == longit):
            rate = X[i, 2]
            c += 1

    fig, ax = plt.subplots()
    ax.scatter(data.Latitude, data.Longitude, s=None, c=fcm_clusters, cmap=None)
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')

    buffer = BytesIO()

    fig.savefig(buffer, format='png')
    buffer.seek(0)
    scatter_plot = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close(fig)

    output_string = f"Accuracy increased by: {res}\n"
    output_string += f"This location is {100 - c}% safe\n"
    
    return output_string, scatter_plot




