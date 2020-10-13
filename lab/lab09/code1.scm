(define (adde x y)
    (+ x y))
(define (a x)
    (if (< x 0)
        (- x)
        x))
(define pi 3.14)

(define (average x y)
    (/ (+ x y) 2))

(define (square x)
    (* x x))

(define (sqrt x)
    (define (update guess)
        (if (= (square guess) x)
            guess
            (update (average guess (/ x guess)))))
    (update 1))

(define plusa (lambda (x) (+ x 4)))


(define (line) (fd 50))
(define (twice fn) (fn) (fn))
(define (repeat k fn)
    (fn)
    (if (> k 1) (repeat (- k 1) fn)))
(define (tri fn)
    (repeat 3 (lambda () (fn) (lt 120))))
(define (sier d k)
    (tri (lambda () (if (= d 1) (fd k) (leg d k)))))
(define (leg d k)
    (sier (- d 1) (/ k 2))
    (penup) (fd k) (pendown))