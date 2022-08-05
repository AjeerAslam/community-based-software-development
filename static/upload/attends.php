<?php
session_start(); 
include("connect.php");
$WorkId=$_SESSION['WorkId'];
if(isset($_POST['Finished'])){
	$query2="SELECT ENo FROM volunteer WHERE VolStatus='Accepted'";
	$results2=mysqli_query($con,$query2);
	if(!$results2){
		echo "An error occur";
	}else{
		echo "OK";
		/*inserting attendence into attends table*/
		while($row=mysqli_fetch_assoc($results2)){
			$ENo=$row['ENo'];
			$Attendence=$_POST[$ENo];
			$query3="INSERT INTO attends(WorkId,ENo,Attendence)VALUES('$WorkId','$ENo','$Attendence')";
			$results3=mysqli_query($con,$query3);
			if(!$results3){
				header('Location: showworks.php');
			}
	}
	/*marking work as finished*/
	$query4="UPDATE work SET WorkStatus='Finished' WHERE WorkId='$WorkId'";
	$results4=mysqli_query($con,$query4);
	if(!$results4){
		echo "An error occur";
	}else{
		echo "Finished";
	}
	/*updating attendence in volunteer table*/
	$query7="SELECT ENo FROM volunteer WHERE VolStatus='Accepted'";
	$results7=mysqli_query($con,$query7);
	if(!$results7){
		echo "An error occur";
	}else{
	while($row=mysqli_fetch_assoc($results7)){
		$ENo=$row['ENo'];
		$query5="SELECT COUNT(ENo) FROM attends WHERE ENo='$ENo'";
		$query6="SELECT COUNT(ENo) FROM attends WHERE ENo='$ENo' AND Attendence='Present'";
		$results5=mysqli_query($con,$query5);
		$results6=mysqli_query($con,$query6);
		if($results5 and $results6 ){
		echo "okm";
		$row=mysqli_fetch_assoc($results5);
		$tottal=$row['COUNT(ENo)'];
		$row=mysqli_fetch_assoc($results6);
		$attended=$row['COUNT(ENo)'];
		$percentage=($attended/$tottal)*100;
		echo $percentage;
		$query8="UPDATE volunteer SET VolAttendPerc='$percentage' WHERE ENo='$ENo'";
			$results8=mysqli_query($con,$query8);
			if(!$results8){
				echo "An error occur8";
			}


	}else{
		echo "somthing wrong";
	}
}
echo<<<EOL
<script language="javascript">
window.alert("attendence marked successfully");
</script>;
EOL;


	}

	//header('Location: showworks.php');

	}
}
	
	$query="SELECT ENo,VolName FROM volunteer WHERE VolStatus='Accepted' ORDER BY ENo";
	$results=mysqli_query($con,$query);
	if(!$results){
		echo "An error occur";
	}else{
		echo "is okay";
	}
echo<<<EOL
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>attends</title>
</head>
<body bgcolor="#87CEFA">
<center>
<b><font face="arial" >WORK ID:$WorkId</font></b><br>
<b><font face="arial" color="red">ATTENDENCE TABLE</font></b>
<pre>
<table border="3px" name=table1 align="center" cellspacing="4px" cellpadding="3px">
<tr>
<td align="center"><h2>ENROLMENT NO:</h2></td>
<td align="center"><h2>VOLUNTEER NAME:</h2></td>
<td align="center"><h2>ATTENDENCE:</h2></td>

 
</tr>
EOL;
/*attends recieving in html*/
while($row=mysqli_fetch_assoc($results)){
$ENo=$row['ENo'];
$VolName=$row['VolName'];
echo<<<EOL
<tr>
<form action="attends.php" name=WorkRegistrationForm method='post'>
<td align="center"><h3><input type="number" name="ENo" value=$ENo readonly="readonly"></h3></td>
<td align="center"><h3><input type="text" name="ENo" value=$VolName readonly="readonly"></h3></td>
<td align="center"><h3>
<label>Present</label>
<input type="radio" name=$ENo value="Present" checked>
<label>Absent</label>
<input type="radio" name=$ENo value="Absent" >
</h3></td>
 

EOL;
}
echo<<<EOL
</table>
</tr>
<td align="center"><h3><input type="submit" name="Finished" value="FINISHED"></h3></td>
</form>
</pre>
</center>
</body>
</html>
EOL;
?>