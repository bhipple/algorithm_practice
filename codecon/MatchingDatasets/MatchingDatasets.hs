#!/usr/bin/env stack
-- stack --install-ghc runghc
import Data.List
import Data.List.Split
import Data.Ord

readInt :: IO Int
readInt = readLn

-- Takes "1,2,3" -> [1,2,3]
readDoubles :: String -> [Double]
readDoubles = fmap read . splitOn ","

main :: IO ()
main = do
    k <- readInt
    input <- lines <$> getContents
    let inp' = readDoubles <$> input
    let (orig, new) = splitAt k inp'
    fmt $ zip [0..] $ map (findClosest new) orig

findClosest :: [[Double]] -> [Double] -> Int
findClosest ys x =
    let ys' = map (euclidDist x) ys
        minIdx = fst . minimumBy (comparing snd) $ zip [0..] ys'
     in floor minIdx

euclidDist :: Floating c => [c] -> [c] -> c
euclidDist xs ys = sqrt . sum . map (^2) $ zipWith (-) xs ys

fmt :: [(Int, Int)] -> IO ()
fmt = mapM_ (\(x,y) -> putStrLn $ show x ++ "," ++ show y)
