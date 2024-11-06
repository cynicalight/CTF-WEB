<?php
$json_data = '["3295c76acbf4caaed33c36b1b5fc2cb1","26657d5ff9020d2abefe558796b99584","73278a4a86960eeb576a8fd4c9ec6997","ec8956637a99787bd197eacd77acce5e","e2c420d928d4bf8ce0ff2ec19b371514","43ec517d68b6edd3015b3edc9a11367b","ea5d2f1c4608232e07d3aa3d998e5135","c8ffe9a587b126f152ed3d89a146b445","66f041e16a60928b05a7e228a89c3799","698d51a19d8a121ce581499d7b701668","5f93f983524def3dca464469d2cf9f3e","f0935e4cd5920aa6c7c996a5ee53a70f","9a1158154dfa42caddbd0694a4e9bdc8","72b32a1f754ba1c09b3695e0cb6cde7f","072b030ba126b2f4b2374f342be9ed44","66f041e16a60928b05a7e228a89c3799","7f39f8317fbdb1988ef4c628eba02591","6364d3f0f495b6ab9dcf8d3b5c6e0b01","6364d3f0f495b6ab9dcf8d3b5c6e0b01","d67d8ab4f4c10bf22aa353e27879133c","5fd0b37cd7dbbb00f97ba6ce92bf5add","9f61408e3afb633e50cdf1b20de6f466","e369853df766fa44e1ed0ff613f563bd","6364d3f0f495b6ab9dcf8d3b5c6e0b01","a0a080f42e6f13b3a2df133f073095dd","c8ffe9a587b126f152ed3d89a146b445","b53b3a3d6ab90ce0268229151c9bde11","1c383cd30b7c298ab50293adfecb7b18","6c8349cc7260ae62e3b1396831a8398f","da4fb5c6e93e74d3df8527599fa62642","3def184ad8f4755ff269862ea77393dd","c0c7c76d30bd3dcaefc96f40275bdc0a","3c59dc048e8850243be8079a5c74d079","a3f390d88e4c41f2747bfa2f1b5f87db","70efdf2ec9b086079795c442636b55fb","3295c76acbf4caaed33c36b1b5fc2cb1","98f13708210194c475687be6106a3b84","98f13708210194c475687be6106a3b84","98f13708210194c475687be6106a3b84","b6d767d2f8ed5d21a44b0e5886680cb9","02e74f10e0327ad868d138f2b4fdd6f0","33e75ff09dd601bbe69f351039152189","6f4922f45568161a8cdf4ad2299f6d23","1ff1de774005f8da13f42943881c655f","43ec517d68b6edd3015b3edc9a11367b"]';

$flag_hashes = json_decode($json_data);
# print_r($flag_hashes);

// $charset = array_merge(
//     range('a', 'z'), 
//     range('A', 'Z'), 
//     range('0', '9'),
//     str_split('!@#$%^&*()-_=+[]{}|;:,.<>?/~`') // 常用符号
// ); // 小写字母和数字


$charset = range(0, 255);
print_r($charset);

function force_md5($hash, $charset, $index) {
    foreach ($charset as $char) {
        if(md5($char ^ $index) == $hash) {
            return $char;
        }
    }
    return false;
}   

foreach ($flag_hashes as $index => $hash) {
    $flag = force_md5($hash, $charset, $index);
    if($flag) {
        echo $flag;
        echo ",";
    } else {
        echo "Not Found";
    }
}

// output is the ord of the flag, then use the python to convert ord to chr

// 题目：
// $flag[] = array();
// for ($ii = 0;$ii < sizeof($array);$ii++) {
//     $flag[$ii] = md5(ord($array[$ii]) ^ $ii);
// }

// echo json_encode($flag);
