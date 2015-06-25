<?php

function handle_each_input($input) {
	$n = intval($input[0]);
	$k = intval($input[1]);
// 	print $n . " " . $k . "\n";

	$array = array();
	for ($count = 1; $count <=$n; $count++){
		// fill the array;
		$array[$count]=$count - 1;
	}
	
	
	$value = 0;
	$output = array();
	for ($count = 0; $count < $n; $count++){				
		$output[$count]=array_pop($array);	
		$array=array_reverse($array);	
	}
	
	for ($count = 0; $count < $n; $count++){
		if ($output[$count]==$k){
			return $count;
		}
	}
	return $value;
	
}
$temp = fopen ("php://stdin","r");
// no of test cases.
$no_of_testcases = intval(fgets($temp));

//  if n is 3
// 0 1 2
// 2 1 0
// 2 0 1

// if n is 4
// 0 1 2 3
// 3 2 1 0
// 3 0 1 2
// 3 0 2 1

//  if n is 5
// 0 1 2 3 4
// 4 3 2 1 0
// 4 0 1 2 3
// 4 0 3 2 1
// 4 0 3 1 2
$output = array();
for ($count=0;$count<$no_of_testcases;$count=$count+1){
	// next t line contains two integer N K.
	$input = fgets($temp);
	$parts = explode(' ',$input);
	$output[$count]  = handle_each_input($parts);
	
}

for ($count=0;$count<$no_of_testcases;$count=$count+1){
	
	print $output[$count]. "\n";
	
}
?>
