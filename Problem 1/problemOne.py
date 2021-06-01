import gmplot
import requests
import json
import polyline

def get_key():
    filename = './Problem 1/key.txt'
    file = open(filename, 'r')
    return file.read().strip()

# Using Distance Matrix API
def get_distance(key, origin, destination):
    url = ('https://maps.googleapis.com/maps/api/distancematrix/json?&mode=driving&language=en&units=metric'
            + '&origins={}'
            + '&destinations={}'
            + '&key={}'
            ).format(origin, destination, key)
    
    response = requests.get(url)

    try:
        response_json = response.json()
        distance_metres = response_json['rows'][0]['elements'][0]['distance']['value']
    except:
        print('ERROR: {}, {}'.format(origin, destination))
        distance_metres = 0

    return distance_metres

def get_direction(key, origin, destination, hub):
    url = ('https://maps.googleapis.com/maps/api/directions/json?'
            + '&origin={}'
            + '&destination={}'
            + '&waypoints={}'
            + '&key={}'
            ).format(origin, destination, hub, key)
    
    response = requests.get(url)

    try:
        response_json = response.json()
        encoded_polyline = response_json['routes'][0]['overview_polyline']['points']
    except:
        print('ERROR: {}, {}, {}'.format(origin, destination, hub))
        encoded_polyline = ''

    return encoded_polyline

#random input quick sort

def partition(arr, low, high):
	i = (low-1)		 
	pivot = arr[high]['total_distance']

	for j in range(low, high):

		if arr[j]['total_distance'] <= pivot:

			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:

		pi = partition(arr, low, high)

		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

def export_json(filename, data):
    file = open(filename+'.json', 'w')
    jsonFile = json.dumps(data, indent=4, separators=(",", ":"))
    file.write(jsonFile)

#PART 1: Get and mark locations.

# Create the map plotter:
apikey = get_key()

print('----PART 1----\n')

print('INFO plotting the hubs')

gmap = gmplot.GoogleMapPlotter(3.129410932454021, 101.59444290467273, 11, apikey=apikey)

gmap.marker(3.0319924887507144, 101.37344116244806, color='#00FF7F', title='City-link Express', label='C')
gmap.marker(3.112924170027219, 101.63982650389863, color='#FF8C00', title='Pos Laju', label='P')
gmap.marker(3.265154613796736, 101.68024844550233, color='#1E90FF', title='GDEX', label='G')
gmap.marker(2.9441205329488325, 101.7901521759029, color='#A52A2A', title='J&T', label='J')
gmap.marker(3.2127230893650065, 101.57467295692778, color='#FFD700', title='DHL', label='D')

print('INFO markLocation.html file created')
# Draw the map to an HTML file:
gmap.draw('markLocation.html')


#PART 2: Get the distances between origin and destination.

print('\n----PART 2----\n')

customers = [
    {
        "name": "Customer 1",
        "origin": "3.3615395462207878,101.56318183511695",
        "destination": "3.1000170516638885,101.53071480907951"
    },
    {
        "name": "Customer 2",
        "origin": "3.049398375759954,101.58546611160301",
        "destination": "3.227994355250716,101.42730357605375"
    },
    {
        "name": "Customer 3",
        "origin": "3.141855957281073,101.76158583424586",
        "destination": "2.9188704151716256,101.65251821655471"
    }
]

distances = []

for customer in customers:
    print('RETRIEVING {cusName} distance...'.format(cusName = customer['name']), end='')
    origin = customer["origin"]
    destination = customer["destination"]
    distance = get_distance(apikey, origin, destination)
    distances.append(distance)
    print('Completed\n')

print('OUTPUT:')
print(('{:^12} {:^12}').format('Customer', 'Distance (m)'))
for i in range(26):
    print('-' , end='')
print()

for distance in distances:
    print(('Customer {:<3}  {:>8}').format(distances.index(distance)+1,distance))

for i in range(26):
    print('-' , end='')
print()

#PART 3: Suggest the least distance that the parcel has to travel for each customer using every courier company.

print('\n----PART 3----\n')

couriers = [
    {
        'name':'City-link Express',
        'hub':'Port Klang',
        'coordinate':'3.0319924887507144,101.37344116244806',
        'color': '#00A651'
    },
    {
        'name':'Pos Laju',
        'hub':'Petaling Jaya',
        'coordinate':'3.112924170027219,101.63982650389863',
        'color': '#F26522'
    },
    {
        'name':'GDEX',
        'hub':'Batu Caves',
        'coordinate':'3.265154613796736,101.68024844550233',
        'color': '#04104C'
    },
    {
        'name':'J&T',
        'hub':'Kajang',
        'coordinate':'2.9441205329488325,101.7901521759029',
        'color': '#FF0014'
    },
    {
        'name':'DHL',
        'hub':'Sungai Buloh',
        'coordinate':'3.2127230893650065,101.57467295692778',
        'color': '#FFCC01'
    }
]

def get_courier_distance(origin, destination, couriers):
    courier_ranking = []

    for courier in couriers:
        print('RETRIEVING {0} distance for {1}...'.format(courier['name'], customer['name']), end='')
        fir_half = get_distance(apikey, origin, courier['coordinate'])
        sec_half =get_distance(apikey, courier['coordinate'], destination)
        total_distance = fir_half + sec_half
        new_dic = {
            'name': courier['name'],
            'total_distance': total_distance
        }
        courier_ranking.append(new_dic)
        print('Completed\n')

    return courier_ranking

for customer in customers:
    ranking_list = get_courier_distance(customer['origin'], customer['destination'], couriers)

    n = len(ranking_list)
    quickSort(ranking_list, 0, n-1)
    print("Recommended couriers for {} based on distance:".format(customer['name']))

    for i in range(n):
        print("{0}. {1:<17} {2:>8}".format(i+1, ranking_list[i]['name'], ranking_list[i]['total_distance'])),
    print('')

    customer.update( courierRanking = ranking_list)

    export_json(customer['name'], customer)
    print('INFO exported result to {}.json\n'.format(customer['name']))

#PART 4: Plot line between the destinations before and after the algorithm.

print('\n----PART 4----\n')

def get_lat(coordinate):
    x = coordinate.split(',')
    return float(x[0])

def get_long(coordinate):
    x = coordinate.split(',')
    return float(x[1])

def plot_polyline(customer):
    mapPlotter = gmplot.GoogleMapPlotter(3.129410932454021, 101.59444290467273, 11, apikey=apikey)

    mapPlotter.marker(3.0319924887507144, 101.37344116244806, color='#00FF7F', title='City-link Express', label='C')
    mapPlotter.marker(3.112924170027219, 101.63982650389863, color='#FF8C00', title='Pos Laju', label='P')
    mapPlotter.marker(3.265154613796736, 101.68024844550233, color='#1E90FF', title='GDEX', label='G')
    mapPlotter.marker(2.9441205329488325, 101.7901521759029, color='#A52A2A', title='J&T', label='J')
    mapPlotter.marker(3.2127230893650065, 101.57467295692778, color='#FFD700', title='DHL', label='D')

    mapPlotter.marker(get_lat(customer['origin']), get_long(customer['origin']), color='white', title=customer['name']+' Origin')
    mapPlotter.marker(get_lat(customer['destination']), get_long(customer['destination']), color='red', title=customer['name']+' Destination')

    for courier in couriers:
        enc_polyline = get_direction(apikey, customer['origin'], customer['destination'], courier['coordinate'])
        lat, long = zip(*polyline.decode(enc_polyline))
        mapPlotter.plot(lat, long, color= courier['color'], edge_width =7)
    mapPlotter.draw(customer['name']+':before.html')


for customer in customers:
    print('INFO plotting map:before for {cusName}...'.format(cusName = customer['name']), end='')
    plot_polyline(customer)
    print('Completed')
    print('INFO {}:before.html file created\n'.format(customer['name']))

def plot_shortest_polyline(customer, courier):
    mapPlotter = gmplot.GoogleMapPlotter(3.129410932454021, 101.59444290467273, 11, apikey=apikey)

    mapPlotter.marker(get_lat(courier['coordinate']), get_long(courier['coordinate']), color='blue', title=courier['name'])

    mapPlotter.marker(get_lat(customer['origin']), get_long(customer['origin']), color='white', title=customer['name']+' Origin')
    mapPlotter.marker(get_lat(customer['destination']), get_long(customer['destination']), color='red', title=customer['name']+' Destination')

    enc_polyline = get_direction(apikey, customer['origin'], customer['destination'], courier['coordinate'])
    lat, long = zip(*polyline.decode(enc_polyline))
    mapPlotter.plot(lat, long, color= courier['color'], edge_width =7)

    mapPlotter.draw(customer['name']+':after.html')

def get_courier(name):
    for courier in couriers:
        if courier['name'] == name:
            return courier

for customer in customers:
    print('INFO plotting map:after for {cusName}...'.format(cusName = customer['name']), end='')
    courier = get_courier(customer['courierRanking'][0]['name'])
    plot_shortest_polyline(customer, courier)
    print('Completed')
    print('INFO {}:after.html file created\n'.format(customer['name']))