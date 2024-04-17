"""A script with a function for converting and classifying temperatures."""

def fahr_to_celsius(temp_fahrenheit):
    """
    Function for converting temperature in Fahrenheit to Celsius.
    
    Parameters
    ----------
    temp_fahrenheit: <numerical>
        Temperature in Fahrenhei
        
    Returns
    -------
    <float>
        Converted temperature.
    """
    temp_celsius = (temp_fahrenheit -32)/1.8 # Convert the value to Celsius
    return temp_celsius # Return the result

def temp_classifier(temp_celsius):
    """
    Function for temperature classification:
    0	The temperature is below -2 degrees Celsius
    1	The temperature is equal to or warmer than -2, but less than +2 degrees Celsius
    2	Тhe temperature is equal to or warmer than +2, but less than +15 degrees Celsius
    3	The temperature is equal to or warmer than +15 degrees Celsius
    
    Parameters
    ----------
    temp_celsius: <numerical>
        Temperature in Celsius.
        
    Returns
    -------
    <int>
        Сlassification number.
    """

    if temp_celsius < -2: # Сompare the set temperature
        return 0 # Return the result
    elif -2 <= temp_celsius < 2: # Сompare the set temperature
        return 1 # Return the result
    elif 2 <= temp_celsius < 15: # Сompare the set temperature
        return 2 # Return the result
    else:
        return 3 # Return the result