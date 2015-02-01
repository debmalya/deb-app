<?php
    $is_printed=false;

    function fact($n) {
        if ($n < 2) {
            return 1;
        } else {
            return $n * fact($n-1);
        }
    }
    
function permute($str,$i,&$outputs) {
   
    
   $n=strlen($str);
    if ($i == $n) {
//        print "$str\n";
        $outputs[]=$str;
        
        
        
    }
   else {
       $j = $i;
        for (; $j < $n; $j++) {
          swap($str,$i,$j);
          permute($str, $i+1,$outputs);
          swap($str,$i,$j); // backtrack.
        
       }
       
       
       
   }
}
// function to swap the char at pos $i and $j of $str.
function swap(&$str,$i,$j) {
    $temp = $str[$i];
    $str[$i] = $str[$j];
    $str[$j] = $temp;
}   

$temp = fopen ("php://stdin","r");
$no_of_testcases = intval(fgets($temp));
$main_string="abcdefghij";

$inputs=array();


for ($count=0;$count<$no_of_testcases;$count=$count+1){
	$no_of_chars=intval(fgets($temp));
	if ($no_of_chars > 0){
		$current_string=substr($main_string,0,$no_of_chars);
		$inputs[]=$current_string;
	}else{
		$inputs[]="";
	}
}

for ($count=0;$count<$no_of_testcases;$count=$count+1){
    $outputs=array();
	permute($inputs[$count],0,$outputs);
    sort($outputs);
    $len=count($outputs);
    for ($j=0;$j<$len;$j=$j+1){
        print $outputs[$j]."\n";
    }
}
?>
