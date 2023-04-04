TEMPERATURE_SCALES = {
    'Celsius': '°C',
    'Fahrenheit': '°F',
    'Kelvin': 'K'
}

def convert_temperature(value, input_scale, output_scale):
    if input_scale == '°C':
        if output_scale == '°F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else:
            return value
    elif input_scale == '°F':
        if output_scale == '°C':
            return (value - 32) / 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_scale == '°K':
        if output_scale == '°C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value

while True:
    print('Enter your desired temperature:')
    value = float(input())
    print('Enter your temperature (°C, °F, or K):')
    input_scale = input().upper()
    print('Enter your temperature (°C, °F, or K):')
    output_scale = input().upper()


    result = convert_temperature(value, input_scale, output_scale)
    print(f'{value} {input_scale} = {result} {output_scale}')


    print('Enter e to exit, or if you want to continue press any key:')
    choice = input()
    if choice.lower() == 'e':
        break