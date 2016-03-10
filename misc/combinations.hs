-- How many distinct sets of size k can be chosen from n distinct elements
fact n = product [1..n]

comb :: Integer -> Integer -> Integer
comb n k = fact n `div` fact k * fact (n-k)
