(set-traces 2)
func main()
{
  const Int[] a;
  const Int[] b;
  const Int alength;
  const Int blength;
  const Int k;
  Int x = 0;
  Int y = 0;
  Int i = 0;

  while(i < alength)
  {
    x = x + a[i];
    i = i + 1;
  }
  x = x + k;

  i = 0;
  while(i < blength)
  {
    y = y + b[i];
    i = i + 1;
  }
  x = x + y;
}

(conjecture
  (=>
    (and
      (forall ((j Int))
        (and
          (= (a j t1) (a j t2))
          (= (b j t1) (b j t2))
        )
      )
      (= (alength t1) (alength t2))
      (= (blength t1) (blength t2))
      (= (k t1) 1)
      (= (k t2) 0)
    )
    (= (x main_end t1) (+ (x main_end t2) 1))
  )
)
