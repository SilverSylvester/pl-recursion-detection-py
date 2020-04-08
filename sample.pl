even(0).
even(N) :- odd(K), N is K + 1.

odd(1).
odd(N) :- even(K), N is K + 1.

a(X) :- b(X).
b(X) :- c(X).
c(X) :- a(X).

% Example from Lab 07
% Question 1: (simple solution)
second(X,[_,X|_]).

% Question 2:
tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([],[]).
listtran([H|T],[H1|T1]):-tran(H,H1),listtran(T,T1).

% Question 3 (students might struggle with 'is' vs =):
fib(0,[0]).
fib(1,[1,0]).
fib(N,[H1,H2,H3|T]):-N>1,M is N-1,fib(M,[H2,H3|T]),H1 is H2+H3.

% Question 4:
% The three horizontal cases
won(A,[A,A,A,_,_,_,_,_,_]):-A=x;A=o.
won(A,[_,_,_,A,A,A,_,_,_]):-A=x;A=o.
won(A,[_,_,_,_,_,_,A,A,A]):-A=x;A=o.

% The three vertical cases
won(A,[A,_,_,A,_,_,A,_,_]):-A=x;A=o.
won(A,[_,A,_,_,A,_,_,A,_]):-A=x;A=o.
won(A,[_,_,A,_,_,A,_,_,A]):-A=x;A=o.

% The two diagonal cases
won(A,[A,_,_,_,A,_,_,_,A]):-A=x;A=o.
won(A,[_,_,A,_,A,_,A,_,_]):-A=x;A=o.