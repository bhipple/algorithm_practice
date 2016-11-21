import Data.Int

-- Generate the infinite list of fibonacci numbers by creating the list
-- resulting from [0, 1, ...] 
fibList :: [Integer]
fibList = 0 : 1 : zipWith (+) fibList (tail fibList)
