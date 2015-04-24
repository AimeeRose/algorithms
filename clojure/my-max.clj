(def currentmax (ref 0))

(defn my-max [& nums]
  (if (> (first nums) @currentmax)
    (dosync (ref-set currentmax (first nums))))
  (if (= (count nums) 1)
    (do (println "done: " @currentmax) @currentmax)
    #(apply my-max (rest nums))))

(trampoline my-max 2 9 10 4 7)

