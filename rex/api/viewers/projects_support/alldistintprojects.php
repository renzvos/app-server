<?php
echo '"result" : ' ;

$projects = $Db->RawSQL("SELECT DISTINCT `project_name` FROM `sessions`");



echo json_encode($projects);

?>