# .count() returns a value, we can assign it to a variable to use it.

letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]

num_i = letters.count("i")
print(num_i)

# We can even use .count() to count element appearances in a two-dimensional list.

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]

num_pairs = number_collection.count([100, 200])
print(num_pairs)


votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")

cassie_votes = votes.count("Cassie")

print(jake_votes)

print(cassie_votes)

print(cassie_votes + jake_votes)