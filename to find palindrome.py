# Python3 program to implement
# the above approach

# Function to find shortest string which
# not a subsequence of the given string
def ShortestSubsequenceNotPresent(Str):

	# Stores the shortest string which is
	# not a subsequence of the given string
	shortestString = ""

	# Stores length of string
	N = len(Str)

	# Stores distinct character of subsegments
	subsegments = set()

	# Traverse the given string
	for i in range(N):

		# Insert current character
		# into subsegments
		subsegments.add(Str[i])

		# If all lowercase alphabets
		# present in the subsegment
		if (len(subsegments) == 26) :

			# Insert the last character of
			# subsegment into shortestString
			shortestString += Str[i]

			# Remove all elements from
			# the current subsegment
			subsegments.clear()
		
	# Traverse all lowercase alphabets
	for ch in range(int(26)):
		
		# If current character is not
		# present in the subsegment
		if (chr(ch + 97) not in subsegments) :
			
			shortestString += chr(ch + 97)
			
			# Return shortestString
			return shortestString
	
	return shortestString

# Driver code
# Given String
Str = "hidad"

print(ShortestSubsequenceNotPresent(Str))

# This code is contributed by divyeshrabadiya07
