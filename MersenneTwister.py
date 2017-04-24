from datetime import datetime

M = 397 #
N = 624 # degree of recurrence. It is sufficient to observe the output of the generator n times to reconstruct the internal state array.
R = 31
W = 32
a = 2567483615
b = 2636928640
c = 4022730752
f = 1812433253
u = 11
s = 7
t = 15
l = 18
init = 1812433253 #The initialization multiplier used to seed the state sequence when a single value is used as seed.
d = (2 ** 32) - 1

# Create a length 624 list to store the state of the generator
MT = [0 for i in xrange(624)]

index = 0
# To get last 32 bits
bitmask_1 = (2 ** 32) - 1
# To get 32. bit
bitmask_2 = 2 ** 31 #0x80000000
# To get last 31 bits
bitmask_3 = bitmask_2 - 1 #0x7FFFFFFF
def initialize_generator(seed):
	"Initializing the array with a NONZERO seed"
	global MT
	global bitmask_1
	MT[0] = seed & bitmask_1
	for i in xrange(1,N):
		MT[i] = ((init * MT[i-1]) ^ ((MT[i-1] >> 30) + i)) & d
		#MT[i] = (69069 * MT[i-1]) & d

def extract_number():
	"""
	Extract a tempered pseudorandom number based on the index-th
	value, calling generate_numbers() every 624 numbers
	Before handing the next integer out, a transform is applied to each integer. This transform has 4 steps, each step involves xoring the number with a bit shifted and bit masked version of itself.
	"""
	global index
	global MT
	if index == 0:
		generate_numbers()
	y = MT[index]
	y = y ^ y >> u	# >> right shift
	y = y ^ y << s & b # >> left shift 0x9d2c5680
	y = y ^ y << t & c # >> left shift 0xefc60000
	y = y ^ y >> l # right shift
	index = (index + 1) % 624
	return y

def generate_numbers():
	"Generate an array of 624 untempered numbers"
	global MT
	for i in xrange(624):
		y = (MT[i] & bitmask_2) + (MT[(i + 1 ) % N] & bitmask_3) # // y is the first bit of the current number and the last 31 bits of the next number
		MT[i] = MT[(i + M) % N] ^ (y >> 1) #   // first bitshift y by 1 to the right and xor it with the 397th next number
		if y % 2 != 0: #// if y is odd, xor with magic number
			MT[i] ^= a # 0x9908b0df;

if __name__ == "__main__":
	now = datetime.now()
	initialize_generator(now.microsecond)
	for i in xrange(5):
		"Print 100 random numbers as an example"
		print extract_number()
