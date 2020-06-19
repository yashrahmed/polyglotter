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