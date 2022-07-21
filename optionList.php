<?php

// GET OPTION LIST FROM DB

echo '<select id="someId" name="someName">';
echo '<option value="null" selected>Choose an option</option>';
$sql = "select * from someTable";
$stmt = mysqli_stmt_init($conn);
if(!mysqli_stmt_prepare($stmt, $sql)){
	echo 'Unable to read database.';
}
else{
	mysqli_stmt_execute($stmt);
	$result = mysqli_stmt_get_result($stmt);
	while($row = mysqli_fetch_assoc($result)){
		echo '<option value="'.$row["id"].'">'.$row["someField"].'</option>';
	}
	mysqli_free_result($result);
}
echo '</select>';

?>