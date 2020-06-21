--double x = x * 2
--double_min x y = (if x < y then x else y) * 2


fib :: Integral a => a -> a
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

fact :: Integral a => a -> a
fact 0 = 1
fact n = n * fact(n-1)

dot_product :: Num a => (a, a) -> (a, a) -> a
dot_product a b = (fst a * fst b) + (snd a * snd b)

third :: (a, b, c) -> c
third (_, _, z) = z

header :: [a] -> a
header [] = error "failed"
header (x:_) = x

-- even odd div3 written using only guards.
is_even_odd_div3_v1 :: Integral(a) => a -> String
is_even_odd_div3_v1 x
    | (x `rem` 2 ==0) && (x `rem` 3 ==0) = "even div3"
    | (x `rem` 2 ==0) && (x `rem` 3 /=0) = "even not-div3"
    | (x `rem` 2 /=0) && (x `rem` 3 ==0) = "odd div3" 
    | (x `rem` 2 /=0) && (x `rem` 3 /=0) = "odd not-div3"
    | otherwise                          = "Unknown"

-- even odd written div3 using guards and where binding
is_even_odd_div3_v2 :: Integral(a) =>  a -> String
is_even_odd_div3_v2 x
    | is_even && is_div3     = "even div3"
    | is_even && not is_div3 = "even not-div3"
    | not is_even && is_div3 = "odd div3"
    | not is_even && not is_div3 = "odd not-div3"
    | otherwise                   = " Unknown"
    where is_even = (x `rem` 2 == 0)
          is_div3 = (x `rem` 3 == 0)

max_value :: (Ord a) => [a] -> a
max_value x = case x of
                    [] -> error "No max value in an empty list"
                    [a] -> a
                    (h:rest) -> max h (max_value rest)


bubble :: (Ord a) => [a] -> [a]
bubble x = case x of
    [] -> []
    [a] -> [a]
    (a:b:xs) -> if a > b then b:(bubble (a:xs)) else a:(bubble (b:xs))

-- max_value []  = 
-- max_value [x] = x
-- max_value (h:rest) = max h (max_value rest)

-- fizz buzz written using guards and where binding
-- fizz_buzz :: Integral(a) => a -> String
-- fizz_buzz x = 
--     | let is_div3 = (x `rem` 3 == 0); is_div5 = (x `rem` 5 == 0);
--     | is_div3 && is_div5 = "FizzBuzz"
--     | is_div5  = "Buzz"
--     | is_div3  = "Fizz"
--     | otherwise       = ""