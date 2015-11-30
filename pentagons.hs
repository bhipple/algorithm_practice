-- Write a function p(n) that returns the number of points
-- in the nth pentagonal number

nextP prev n = prev + 2 + n + 2 * (n-2)

p :: [(Integer, Integer)]
p = (1,1) : map f p
    where f = \(x,y) -> ((nextP x (y+1)), y+1)
