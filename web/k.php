<?php
header('Content-Type:application/json');
header('Access-Control-Allow-Origin:*');
header('Access-Control-Allow-Methods:POST,GET,OPTIONS,DELETE');

$search = '';

$response = array(
    'code'=>404,
    'msg'=>''
);

if(isset($_GET['search'])){
    $search = $_GET['search'];
}else{
    echo(json_encode($response));
    exit(0);
}


$fileName = 'E:\Documents\Github\QuestionBank\总题库.txt';
if(!file_exists($fileName)){
    $response['msg'] = 'file not exist';
    echo(json_encode($response));
    exit(0);
}


// echo(substr($search, 0, strlen('甲1投篮')));
$eof = '你的答案';
$end = strlen($eof);

// exit(0);

// echo ($fileName . "\n");
// echo (file_exists($fileName) . "\n");
// exit(0);
// $i = 0;
// echo($i);
$result = '';

$file = fopen($fileName, 'r');

while (!feof($file)) {
    $content = fgets($file);
    if (strpos($content, $search) !== false) {
        // echo ($i . "\n");
        $result .= $content;
        while (!feof($file)) {
            $content = fgets($file);
            $result .= $content;
            if(isset($content[$end])&&substr($content, 0, $end)==$eof){
                break;
            }
        }
        break;
    }
}

fclose($file);

// echo($i);

// echo($result);


if(isset($result[1])){
    $response['code'] = 200;
    $response['msg'] = $result;
}

// echo("\n");

echo(json_encode($response, JSON_UNESCAPED_UNICODE));


