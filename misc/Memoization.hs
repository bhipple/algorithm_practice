#!/usr/bin/env stack
-- stack --install-ghc runghc

-- A naively implemented recursive function
slowFib :: Int -> Integer
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n-2) + slowFib (n-1)

-- Fibonacci with memoization
memoFib :: Int -> Integer
memoFib = (map fib [0..] !!)
    where fib 0 = 0
          fib 1 = 1
          fib n = memoFib (n-2) + memoFib (n-1)

main :: IO ()
main = do
    putStrLn "Slow Fib 30:"
    print (slowFib 30)

    putStrLn "memoFib 10000:"
    print (memoFib 10000)
