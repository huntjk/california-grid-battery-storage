from geopy.distance import geodesic
import config as cfg
import collections as col

# Gets geographic distance between two points
def getDistance(coords_1, coords_2):
    return geodesic(coords_1, coords_2).miles

def getCoords(zipcode):
    return (cfg.data[zipcode][LATITUDE], cfg.data[zipcode][LONGITUDE])

# Convert array of zipcodes to array of locations (tuples of (latitude, longitude))
def getLatLong(input):
    result = col.defaultdict()
    for zipcode, val in input.items():
        result[getCoords(zipcode)] = val
    return result

def getLatLongTuple(input):
    result = col.defaultdict()
    for zipcode, val in input.items():
        result[getCoords(zipcode[0])] = val
    return result

def energyLoss(distance, energy):
    factor = (1 - cfg.k_efficiency_loss) ** distance
    return factor * energy

def inverseEnergyLoss(distance, energy):
    factor = (1 - cfg.k_efficiency_loss) ** distance
    return energy / factor

# Prints a dictionary (key: val)
def printDict(input):
    for index, v in input:
        if isinstance(v, col.Mapping):
            print '{}: {}'.format(index, dict.__repr__(v))
        else:
            print '{}: {}'.format(index, v)
    print

# Append second dictionary scores
def printDictAppend(input):
    for k, v in input.items():
        total = cfg.data[k][cfg.month_index]
        print '{}: {} / {} ({:.1%})'.format(k, int(v), int(total), (v / total))
    print

def printListDict(input, zip_map):
    for index, v in enumerate(input):
        if isinstance(v, col.Mapping):
            zip_v = col.defaultdict(float)
            for x, y in v.items():
                zip_v[zip_map[x]] = y
            print '{}: {}'.format(index, dict.__repr__(zip_v))
        else:
            print '{}: {}'.format(index, v)
    print

# Append second dictionary scores
def printListDictAppend(input, zip_demands, zip_map):
    for index, v in enumerate(input):
        total = zip_demands[index]
        print '{}: {} / {} ({:.1%})'.format(zip_map[index], int(v), int(total), (v / total))
    print

# Indexes
LATITUDE = 0
LONGITUDE = 1
SUPPLY_KW = 2
MONTH_1_KWH = 3
MONTH_2_KWH = 4
MONTH_3_KWH = 5
MONTH_4_KWH = 6
MONTH_5_KWH = 7
MONTH_6_KWH = 8
MONTH_7_KWH = 9
MONTH_8_KWH = 10
MONTH_9_KWH = 11
MONTH_10_KWH = 12
MONTH_11_KWH = 13
MONTH_12_KWH = 14
