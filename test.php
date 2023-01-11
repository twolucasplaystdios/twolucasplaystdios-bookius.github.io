<?php
    $data1 = $_GET["text_name"];
    $data2 = $_GET["text_title"];
    $data3 = $_GET["text_question"];
    echo "<table width='3' border='1'>";
    for ($i=0; $i<$columns; $i++) {
        echo "<tr>名:$data1 </tr>";
        echo "<tr>標題:$data2 </tr>";
        echo "<tr>問題/投訴:$data3 </tr>";

    }
?>