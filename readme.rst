=========
Project 1
=========
-----------------------
Basis flask application
-----------------------

Introduction
============

Dit is de eerste docker tutorial op de docker site voor python.
Het is een simpel flask programma die hello docker
terug geeft als je een GET request doet. De dockerfile
maakt een python image met de libraries in requirement.txt


Benodigde Commands
------------------

Hier wordt voor het runnnen van de app in docker

Image
`````````````
Om een image te maken moet het command

.. code-block:: console
    $ docker build --tag NAAMIMAGE .
..

Om alle images te zien die zijn gemaakt

.. code-block:: console
    $ docker images
..
Container
`````````````
Om container aan te maken voer je het run command uit met als argument de naam van de docker image.
De container heeft eigen ports en moet dus worden verbonden met een port van de localhost.
Dit doe je door de --publish ([host port]:[container port]) command toe te voegen

.. code-block:: console
    $ docker run -d -p 4000:80 NAAMIMAGE
..

Om een lijst van alle actieve containers te zien voor je dit command uit

.. code-block:: console
    $ docker ps
..
Om een lijst van alle containers te zien voor je dit command uit

.. code-block:: console
    $ docker ps -a
..


Docker in Azure
------------------
De docker container werkt lokaal. Om het in de cloud werkend te krijgen gebruiken we azure container registry en
azure container instances.

Eerst moet er worden ingelogd in azure

.. code-block:: console
    docker login LOGINSERVER
..

Vervolgens moet er een speciale tag aan de image worden gegeven met de URI van de registry

.. code-block:: console
    docker login LOGINSERVER/testflask:v1
..

Nu kan de container worden gepushed

.. code-block:: console
    docker push LOGINSERVER/testflask:v1
..


Nu moet er een container instanceworden gemaakt via de portal. In de portal kan je een container regisrty kiezen

Docker in Azure met command line
----------------------
inloggen

.. code-block:: console
    docker login azure
..

Je moet een context aanmaken hierbij zal je een resourcegroup moeten kiezen voor de container


.. code-block:: console
    docker context create aci myacicontext
..

Nu kan de container worden gepushed

.. code-block:: console
    docker push LOGINSERVER/testflask:v1
..


Nu kan je
Nu kan de container worden gepushed

.. code-block:: console
    docker --context myacicontext run -p 80:80 LOGINSERVER/testflask:v1
..


Dit kan makkelijker worden geautomatiseerd met azure dev ops
