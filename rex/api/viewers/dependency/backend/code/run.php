<?php
$prod = new Production();
require $prod->appsfolder."/SQLConnector/code/run.php" ;
//require $prod->appsfolder."/api-php/code/run.php";
//require $prod->appsfolder."/rshelves-php/code/run.php";
$Db = new DBController();
class backed {


 
	
	function GetTableCount($table,$col)
	{$Db = new DBController();
		$sql = "SELECT COUNT(".$col.") AS count FROM ".$table;
		
		$result = $Db->RawSQL($sql);
		return $result[0]['count'];
		}
		

	
		
	 function Insert($table, $col,$val) {
		$Db = new DBController();
        $sql = "INSERT INTO ".$table."(".$col.") VALUES (".$val.")";
		$result = $Db->RawSQL($sql);
		$sql;

		/*

		$backup = new BackupSource();
        echo $backup->Insert($table,$col,$val);

		*/

	    return $result;
    }
	
	function GetTable($table,$wheresql,$limit)
	{	$Db = new DBController();
		$sql = "SELECT * FROM ".$table;
		
		if($wheresql != ""){
		 $sql = $sql." WHERE ".$wheresql;
		}
		
		if($limit != 0)
		{ $sql = $sql." LIMIT ".$limit;
			}
			
		$result = $Db->RawSQL($sql);
		return $result;
		
	}
	
	function GetDisticntRow($table,$row)
	{	$Db = new DBController();
		$sql = "SELECT DISTINCT `".$row."` FROM `".$table."`";
		$result = $Db->RawSQL($sql);
		return $result;
		
		}
		

		function CheckForTimeZoneDIfferenceInServer()
	{
		$Db = new DBController();
        $result = $Db->RawSQL("SELECT CURRENT_TIMESTAMP");
        $date_time = new DateTime( $result[0]['CURRENT_TIMESTAMP']);
        $difference = date_diff(new DateTime(), $date_time);
        $minutes = $difference->i;
        if($minutes >= 1)
        {
        	return false;
        }
        else
        {
        	return true;
        }
	}
	
	

}
?>