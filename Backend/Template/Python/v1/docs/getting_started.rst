Getting Started
===============

Installation
------------

.. code-block:: bash

   pip install v1

Or from source:

.. code-block:: bash

   git clone https://github.com/yourname/v1
   cd v1
   pip install -e .

Basic Usage
-----------

Import the package:

.. code-block:: python

   import time


   time.sleep(1)

Create a calculator instance:

.. code-block:: python

   import datetime


   now = datetime.datetime.now()
   print(f"Current time: {now}")

Dependencies
------------

This package requires:

* Python 3.8+
* No external dependencies