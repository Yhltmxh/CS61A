(define (ascending? s)
    (cond 
        ((<= (length s) 1) #t)
        ((<= (car s) (car (cdr s))) (ascending? (cdr s)))
        (else #f)
    )
)

(define (my-filter pred s)
    (cond
        ((null? s) s)
        ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
        (else (my-filter pred (cdr s)))
    )
)

(define (interleave lst1 lst2)
    (if (null? lst1) 
        (if (null? lst2)
            nil
            (cons (car lst2) (interleave (cdr lst2) lst1))
        )
        (cons (car lst1) (interleave lst2 (cdr lst1)))
    ) 
)

(define (no-repeats s) 
    (if (<= (length s) 1)
        s
        (cons (car s) (filter (lambda (x) (not (= x (car s)))) 
            (no-repeats (cdr s))))
    )
)
