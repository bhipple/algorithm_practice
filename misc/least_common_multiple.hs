-- Given a list of integers, find their least common multiple
-- Aren't libraries and folds great?
lcmList xs = foldr lcm 1 xs
