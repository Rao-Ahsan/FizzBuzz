<?php

function fizzBuzz($n){
    $fizzbuzzArraz = array();
for ($i = 1; $i <= $n; $i++) {
    if($i % 3 == 0 && $i % 5 == 0){
        echo "FizzBuzz";
        echo "<br>";
        $fizzbuzzArraz[$i] = "FizzBuzz";
    }
    elseif($i % 3 == 0){
       echo "Fizz";
       echo "<br>";
       $fizzbuzzArraz[$i] = "Fizz";
    }
    elseif($i % 5 == 0){
        echo "Buzz";
        echo "<br>";
        $fizzbuzzArraz[$i] = "Buzz";
    }
    else{
        echo $i;
        echo "<br>";
        $fizzbuzzArraz[$i] = $i;
    }
    }
    return $fizzbuzzArraz;
}
fizzBuzz(15);
?>
