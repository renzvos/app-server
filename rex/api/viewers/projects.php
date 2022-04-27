<?php
header("Access-Control-Allow-Origin: *");
require "dependency/Production.php";
require "dependency/backend/code/run.php";
require "../clients/error-report.php";

$error = new ErrorReport();

require "../clients/validation.php";
$val = new Validation();

if($val->CheckAuthentication())
{
    echo '{ ';
    require "projects_support/alldistintprojects.php";


    echo ' }';
}
else{
    $ser = new backed();
    $data = $error->ReportDocument("REX Auth Error");
    $coulmn = ' `session_id`, `action` , `window` , `extra_data` ' ;
    $values = "'1','Error','API Viewers/Projects','".$data."'";
    $id = $ser->Insert("events",$coulmn,$values);

    $response['result'] = "error";
    $response['reason'] = "auth failed";
    echo json_encode($response);
}



?>
