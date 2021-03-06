(set-traces 2)

func main()
{
  const Int h;
  Int l = 5;

  Int[] output;
  Int counter = 0;
  
  if (h == 1)
  {
    l = l - 1;
  }
  else
  {
    skip;
  }
  l = 4;

  output[counter] = l;
  counter = counter + 1;
}

(conjecture
  (= (l main_end t1) (l main_end t2))
)

(conjecture
  (= (counter main_end t1) (counter main_end t2))
)

(conjecture
  (=>
    (forall ((pos Int))
      (= (output l9 pos t1) (output l9 pos t2))
    )
    (forall ((pos Int))
      (= (output main_end pos t1) (output main_end pos t2))
    )
  )
)