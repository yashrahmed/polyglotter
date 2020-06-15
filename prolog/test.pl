is_father_of(jayaraj,yashraj).
is_father_of(ningaraj,jayaraj).
is_father_of(mka, ningaraj).

is_ancestor_of(X,Y) :- is_father_of(X, Z), is_father_of(Z, Y).
is_ancestor_of(X,Y) :- is_father_of(X, Z) , is_ancestor_of(Z, Y).
