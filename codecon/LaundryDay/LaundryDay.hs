#!/usr/bin/env stack
-- stack --install-ghc runghc
import Control.Monad
import Data.Char
import Data.List
import Data.Maybe
import Data.Monoid

insensitive :: String -> String -> Ordering
insensitive s1 s2 = compare (toLower <$> s1) (toLower <$> s2)

main :: IO ()
main = do
    input <- group . sortBy insensitive . lines <$> getContents
    mapM_ res input

res :: [String] -> IO ()
res rs =
    if (last . words . head $ rs) == "sock" then
        handleSocks rs
    else out (length rs) (head rs)

handleSocks :: [String] -> IO ()
handleSocks ss
    | length ss == 1 = out 0 item
    | even (length ss) = out (length ss `div` 2) item
    | otherwise = out (length ss `div` 2) item >> out 0 item
    where item = head ss

out :: Int -> String -> IO ()
out ct item = putStrLn $ show ct <> "|" <> item
