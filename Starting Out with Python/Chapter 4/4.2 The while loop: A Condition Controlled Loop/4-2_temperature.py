# This program assists a technician in the process
# of checking a substance's temperature.

MAX_TEMP = 102.5

temperature = float(input("Enter the substance's Celsius temperature: "))

while temperature > MAX_TEMP:
    print ('The temperature is too high.')
    print ('Turn the thermostat down and wait')
    print ('5 minutes. Then take the temperature')
    print ('again and enter it.')
    temperature = float(input('Enter the new Celsius temperature: '))

print('The temperature is acceptable.')
print('Check it again in 15 minutes.')