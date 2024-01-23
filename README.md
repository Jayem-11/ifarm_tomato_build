# iFARM_TOMATO
Tomato disease classifier wih CNN

![This is an image of a Tomato plant](https://github.com/Jayem-11/ifarm_tomato_build/blob/main/pexels-janko-ferlic-2858259.jpg)
photo credits: [Janko Ferlic](https://www.pexels.com/@thepoorphotographer/)

## Description: 
The system is a tomato disease classifier that uses Convolutional Nueral Networks to detect the type of leaf disease present in a tomato plant. A user can upload a picture of a tomato to a React frontend website which sends the request to a FastAPI backend via nginx. Finally, I deployed the system to AWS ec2 webserver

## Author
- Github [@JM_Rono](https://github.com/Jayem-11)
- Linked_in [@John Michael Rono](https://www.linkedin.com/in/john-michael-rono-26a2b6183/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BGItpY4FbT0mUzd4XQz%2FwxQ%3D%3D)

## Table of Contents
[1. Machine learning](#ml) <br>
[2. Frontend](#fr) <br>
[3. Backend](#bk) <br>
[4. Deploying](#dp) <br>

## Tech Stack
- Tensorflow
- React
- FastAPI
- Nginx
- AWS Server

## 1.<span id="ml"> Machine Learning </span>

- Check-out notebook:  [@notebook](https://github.com/Jayem-11/ifarm_tomato_build/blob/main/tomato_disease_prediction.ipynb)
## 

![Jupyter notebook example](https://github.com/Jayem-11/ifarm_tomato_build/blob/main/Screenshot%20(458).png)
![Jupyter notebook example](https://github.com/Jayem-11/ifarm_tomato_build/blob/main/Screenshot%20(459).png)


## 2.<span id="fr"> Frontend </span>
- React app in `build` folder
- To run build:
```
npm install -g serve
serve -s build
```

I created a frontend site to allow a user to drag and drop images of tomato leaves. The site then sends a POST request to a FastAPI backend server.
The Frontend UI looks like this:
## 
### Before image upload
![](https://github.com/Jayem-11/ifarm_tomato_build/blob/main/Screenshot%20(460).png)

### After image upload

![](https://github.com/Jayem-11/ifarm_tomato_build/blob/main/Screenshot%20(462).png)

## 

## <span id="bk"> Backend </span>

### Running FastAPI
1. Get inside `api` file 
```
cd api
```
2. Run main.py
```
uvicorn main:app --reload
```

##

## <span id="dp"> Deploying </span>

### Setting up nginx

conf file:
```

server {
        listen 80;
        #listen [::]:80 default_server;

        root /var/www/html/build/;

        index index.html;

        server_name myserver.com;

        location /api/ {
               
                proxy_pass http://127.0.0.1:8000/;
	}
	
}
```
## 

Project is Hosted at: [my_AWS_ec2 instance](http://ec2-44-202-219-114.compute-1.amazonaws.com/)
- I will update the link incase I change the ec2 instance


