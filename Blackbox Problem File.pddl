(define (problem blackbox planner)
(:domain blackbox planner)
(:objects
	G H X Grid table(5x5))
(:init	
	Location: ((5,1)(5,2)(4,1)(4,2)(4,3)(3,4)(1,2)(1,5)) Inaccesable
	(G in Grid table, Location(4,4))
	(H in Grid table Location(2,1))
	(X in Grid table Location(3,3))
	(clear G)
	(clear H)
	(clear X)
)
(:goal (and (at X G ) (at G H)))
)
