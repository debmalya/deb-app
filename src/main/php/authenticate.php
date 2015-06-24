<!DOCTYPE html>
<html>
<body>

<?php
$table="user";
try {
	$conn = new PDO('sqlite:/Users/debmalyajash/database/deb.db');
	$conn->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION );
	$sql ="CREATE table if not exists $table(
     id INT( 11 ) PRIMARY KEY,
     password VARCHAR( 32 ) NOT NULL);" ;
     $conn->exec($sql);
     print("Created $table Table.\n");
     $conn->beginTransaction();

     $qry = $conn->prepare(
    'INSERT INTO user (id, password) VALUES (?, ?)');
     $id=time();
	 $res =$qry->execute(array(time(), md5("Raju")));
	 $conn->commit();
	 $statement = $conn->prepare('SELECT * from  user');


// print Authenticate($id,"Raju",$conn);
print Authenticate($id,"Raju",$conn);
// print Authenticate(1,"Raju",$conn);
// 
}catch(PDOException $e) {
    echo $e->getMessage();//Remove or change message in production code
}

echo "<BR>";
echo phpversion();

function Authenticate($id, $password, $con){
	$encrypted_password=md5($password);	
	
	$con->setAttribute( PDO::ATTR_EMULATE_PREPARES, false );
	
	$sql =$con->prepare('SELECT id, password FROM user WHERE id = :id');
	$sql->bindParam(':id',$id,PDO::PARAM_INT);
	$rows=$sql->execute();
	$no_of_records=count($rows);
	$result = $sql->fetchAll();
	
	foreach ($result as &$each) {
    	if ($each['password'] ===  $encrypted_password){
    		return 0;
    	} else {
    		return -2;
    	}
	}
	

	return -1;

}
?>

</body>
</html>
