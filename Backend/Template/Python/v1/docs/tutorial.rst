Tutorial
========

This tutorial will guide you through the main features of My Package.

Basic Operations
----------------

Let's start with simple arithmetic operations:

.. code-block:: python

   from mypackage import add, multiply

   # Basic arithmetic
   sum_result = add(5, 3)        # 8
   product_result = multiply(4, 2)  # 8

Using the Calculator Class
--------------------------

The Calculator class maintains state:

.. code-block:: python

   from mypackage.core import Calculator

   # Create a calculator
   calc = Calculator(initial_value=10)

   # Perform operations
   calc.add(5)           # Value is now 15
   calc.multiply(2)      # Value is now 30
   calc.subtract(10)     # Value is now 20

   # Get the current value
   current_value = calc.get_value()  # 20

   # Reset the calculator
   calc.reset()          # Value is now 0

Error Handling
--------------

The package provides custom exceptions:

.. code-block:: python

   from mypackage.exceptions import CalculationError

   try:
       calc.divide(0)  # This will raise an error
   except CalculationError as e:
       print(f"Error: {e}")