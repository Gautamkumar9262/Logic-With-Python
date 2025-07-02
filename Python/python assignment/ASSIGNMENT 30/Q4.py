#you have a list of names of candidates, some of them are wearing black hat, some of them are wearing red shoes and some of them are wearing both. now you have given a list of names of candiidates wearing black hat. there is another list of anmes of candidates wearing red shoes. write a python script to find out the names of the candidates wearing black hat and red shoes.

candidates={"gautam","amit","atishay","navin","nitesh","pankaj","rohit","rahul","rausan","manish","komal"}

black_hat_candidates={"gautam","nitesh","pankaj","rohit","komal"
}

red_shoes_candidates={"amit","atishay","navin","nitesh","manish","rausan","manish","komal","gautam"

}

s1=black_hat_candidates.intersection(red_shoes_candidates)
for c in s1:
    print(c)