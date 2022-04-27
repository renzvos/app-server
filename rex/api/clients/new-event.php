<?php
header("Access-Control-Allow-Origin: *");
require "dependency/Production.php";
require "dependency/backend/code/run.php";
require "error-report.php";
$error = new ErrorReport();


$allow = true;
require "validation.php";
$val = new Validation();

if( isset($_POST['session_id']) && $val->CheckExistance($_POST['session_id']) ) $session_id = $_POST['session_id']; else{ $allow = false;  $data = $error->ReportDocument("REX No Session ID") ; $session_id = 1;}
if( isset($_POST['window']) &&  $val->CheckExistance($_POST['window'])) $window  =  $_POST['window']; else {$allow = false; $window = "No window"; $data =  $error->ReportDocument("REX No Window");}
if( isset($_POST['tail']) &&  $val->CheckExistance($_POST['tail'])) $tail  =  $_POST['tail']; else {$tail = 'NULL';}


if($val->CheckAuthentication())
{
    require "Handlers/extra-data.php";   
    // If any other required items is not there ..the data is " no required field
    if( isset($_POST['action']) &&  $val->CheckExistance($_POST['action'])) $action =  $_POST['action']; else {$allow = false;  $data = $error->ReportDocument("REX No Action");}

}
else
{
    $allow = false;
    $data = $error->ReportDocument("REX Auth Error");
}







$ser = new backed();

if($allow)
{
$coulmn = ' `session_id`, `action` , `window` , `extra_data` ,`tail`' ;
$values = "'".$session_id."','".$action."','".$window."','".$data."',".$tail."";
$id = $ser->Insert("events",$coulmn,$values);
$response['tail'] = $id;
echo json_encode($response);
}

else
{
$coulmn = ' `session_id`, `action` , `window` , `extra_data`,`tail` ' ;
$values = "'".$session_id."','Error','".$window."','".$data."',NULL";
$id = $ser->Insert("events",$coulmn,$values);
}

$response['tail'] = $id


?>