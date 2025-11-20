import sys

# Check if user gave arguments
if len(sys.argv) > 1:
    scores = sys.argv[1:]
    print("User provided scores:")
else:
    print("No input given - using default scores:")
    scores = ["80", "90", "75", "88"]

# Convert all score values to integers
scores = [eval(x) for x in scores]

# Calculate values
total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)



# Print results
print("Scores =", scores)
print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)