-- Given a list of integers, find their least common multiple
-- Aren't libraries and folds great?
lcmList = foldr lcm 1
