-- Given k, print the first k rows of pascal's triangle
import Data.List

fact n = product [1..n]

-- zero indexed on the rth row and cth column
value r c = (fact r) `div` ((fact c) * fact (r-c))

row k c
    | c > k = []
    | otherwise = (value k c) : (row k (c+1))

triangle k = map (\i -> row i 0) [0..(k-1)]

printRow r = putStrLn row
    where row = intercalate " " $ map show r

display tri = mapM_ printRow tri


