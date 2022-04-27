<?php
header("Access-Control-Allow-Origin: *");
require "dependency/Production.php";
require "dependency/backend/code/run.php";
require "error-report.php";
$error = new ErrorReport();
// Testout Error Catching $a = 10/0;
$allow = true;


require "validation.php";
$val = new Validation();

if($val->CheckAuthentication())
{

    require "Handlers/extra-data.php";
    require "Handlers/network-location.php";
    require "Handlers/gps-location.php";
    require "Handlers/device-data.php";

    if( isset($_POST['project']) && $val->CheckExistance($_POST['project']) ) $project = $_POST['project'] ;   else{ $allow = false;  $data = $error->ReportDocument("Creating Session No Project");}
    if( isset($_POST['source'])  && $val->CheckExistance($_POST['source'])) $source =  $_POST['source'] ;  else{ $allow = false;  $data = $error->ReportDocument("Creating Session No Source");}
    if( isset($_POST['user_id']) && $val->CheckExistance($_POST['user_id'])  ) $user_id =  $_POST['user_id'];  else{ $user_id = null; }
    if( isset($_POST['version']) && $val->CheckExistance($_POST['version']) ) $version =  $_POST['version'];  else{ $allow = false;   $data = $error->ReportDocument("Creating Session No Version");}
    if( isset($_POST['entry_page']) && $val->CheckExistance($_POST['entry_page']) ) $entry = $_POST['entry_page'] ; else{ $allow = false;   $data = $error->ReportDocument("No Entry Page Given");}

}
else
{
    $allow = false;
    $data = $error->ReportDocument("REX Auth Error");
}




$ser = new backed();



if($allow)
{
//Checking for undefined source and reporting
$checksource = $Db->RawSQL("SELECT `id`  FROM `sources` WHERE `plan_name`=".$source."");
if(is_null($checksource))
{
    //No source an add Source
}

$coulmn = ' `project_name` , `source` , `user_id` ,  `extra_data` , `network_location` , `gps_location` , `project_version` ,`device` , `entry_page`' ;
$values = "'".$project."','".$source."','".$user_id."','".$data."','".$net_loc."','".$gps_loc."','".$version."','".$device."','".$entry."'";

$id = $ser->Insert("sessions",$coulmn,$values);

$output['session_id'] = $id;
echo json_encode($output);

}

else
{

$coulmn = ' `session_id`, `action` , `window` , `extra_data` ' ;
$values = "'1','Error','Server New Session','".$data."'";
$id = $ser->Insert("events",$coulmn,$values);

}









?>