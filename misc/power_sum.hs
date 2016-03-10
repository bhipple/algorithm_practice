-- Given x and n, calculate the number of ways to express
-- x as the sum of y_i^n for i in [1..]

powerset :: [Int] -> Int -> [[Int]]
powerset [] _ = [[]]
powerset (x:xs) t = xss ++ map (x:) xss
    where xss = filter (\y -> sum y <= t) (powerset xs t)

powerct :: Int -> Int -> Int
powerct x n = length ways
    where
        powers = [k^n | k <- [1..]]
        pows = takeWhile (<= x) powers
        pset = powerset pows x
        ways = filter (\s -> sum s == x) pset

main :: IO ()
main = do
        x <- getLine
        n <- getLine
        print $ powerct (read x :: Int) (read n :: Int)
