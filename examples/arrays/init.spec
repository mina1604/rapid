func main()
{
	Int[] a;
	const Int alength;
	const Int v;

	Int i = 0;
	while(i < alength)
	{
		a[i] = v;
		i = i + 1;
	}
}

(conjecture
   (forall ((pos Int))
      (=>
         (and
            (<= 0 pos)
            (< pos alength)
            (<= 0 alength)
         )
         (= (a main_end pos) v)
      )
   )
)
