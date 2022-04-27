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

    $ser = new backed();
    $response['table'] =  $Db->RawSQL("SELECT * FROM `events` WHERE `action` = 'Error' LIMIT 50" );
    $response['result'] = "success";
    echo json_encode($response);


}
else
{
    
    $response['result'] = "error";
    $response['reason'] = "auth failed";
    echo json_encode($response);
}



?>