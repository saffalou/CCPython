#  Calculate forces
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
C = 3*10**8

# for a train scenario
# train force
def get_force(mass, acceleration):
  return mass * acceleration

get_force(train_mass, train_acceleration)

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies" + str(train_force) + " Newtons of force\n")

# train work
def get_work(force, distance):
  return train_force * train_distance

train_work = get_work(train_force, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over Y meters.\n")


# energy from a nuclear bomb blast using bomb mass and speed of light (C)
def get_energy(mass, c):
  return mass * ((C)**2)

bomb_energy = get_energy(bomb_mass, C)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules \n")

# temperature conversions
# farenhiet to celcius
f_temp = 97.54
adjustment =  32
c_temp = 33.54

CONVERSION_FACTOR_F_TO_C = 5/9
CONVERSION_FACTOR_C_TO_F = 9/5

def f_to_c(f_temp):  
  c_temp = (f_temp - adjustment) * CONVERSION_FACTOR_F_TO_C
  return c_temp

f100_in_celcius = f_to_c(f_temp)

print(str(round(f_temp, 2)) + " degrees farenheit converts to "+ str(round(f100_in_celcius,2)) +" degrees celcius\n")

# celcius to farenheit
def c_to_f(c_temp):
  f_temp = (c_temp * CONVERSION_FACTOR_C_TO_F) + adjustment
  return f_temp

c0_in_farenheit = c_to_f(c_temp)

print(str(round(c_temp, 2)) + " degrees celcius converts to " + str(round(c0_in_farenheit, 2)) +" degrees farenheit")



