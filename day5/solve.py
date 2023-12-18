import re

def convert_number(current_number, maps):
    for map_data in maps:
        dest_start, src_start, length = map_data
        if src_start <= current_number < src_start + length:
            current_number = dest_start + (current_number - src_start)
    return current_number

def find_location(seed, maps):
    soil_number = convert_number(seed, maps['seed_soil'])
    fertilizer_number = convert_number(soil_number, maps['soil_fertilizer'])
    water_number = convert_number(fertilizer_number, maps['fertilizer_water'])
    light_number = convert_number(water_number, maps['water_light'])
    temperature_number = convert_number(light_number, maps['light_temperature'])
    humidity_number = convert_number(temperature_number, maps['temperature_humidity'])
    location_number = convert_number(humidity_number, maps['humidity_location'])
    return location_number

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    seeds = []
    maps = {
        'seed_soil': [],
        'soil_fertilizer': [],
        'fertilizer_water': [],
        'water_light': [],
        'light_temperature': [],
        'temperature_humidity': [],
        'humidity_location': [],
    }

    current_map = None
    for line in lines:
        if line.startswith("seeds:"):
            seeds = list(map(int, line[len("seeds:"):].strip().split()))
        elif re.match(r'(.+)-to-(.+)\s*map:', line):
            map_match = re.match(r'(.+)-to-(.+)\s*map:', line)
            current_map = f"{map_match.group(1).replace(' ', '').replace('_', '-').lower()}_{map_match.group(2).replace(' ', '').replace('_', '-').lower()}"
        elif current_map:
            maps[current_map].append(tuple(map(int, line.strip().split())))

    return seeds, maps

input_file_path = 'input'
seeds, maps = read_input(input_file_path)

locations = [find_location(seed, maps) for seed in seeds]

print("Locations corresponding to the seeds:")
print(locations)
